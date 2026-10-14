# plot_iv_pv_distances.py
# Hard-coded I-V datasets (from provided table)
# Distances:
#   data_70cm  <- originally "left block"
#   data_80cm  <- originally "middle block"
#   data_60cm  <- originally "right block"
#
# Produces:
#   iv_curve.png   (I-V curves with Voc, Isc marked)
#   pv_curve.png   (P-V curves with Pm marked)
#
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Data arrays
data_70cm = [
    (0.54,101.5),(0.69,101.55),(0.76,102.75),(0.89,103.0),(1.04,103.1),
    (1.11,104.1),(1.24,103.3),(1.31,103.0),(1.43,103.7),(1.57,103.5),
    (1.63,103.6),(1.73,101.8),(1.86,97.9),(1.90,93.4),(1.94,85.9),
    (2.00,69.5),(2.05,45.8),(2.08,26.1),(2.09,21.0),(2.09,19.3),
    (2.10,17.6),(2.10,14.4),(2.10,13.0),(2.11,10.7),(2.11,9.0),
    (2.11,7.9),(2.11,7.0),(2.11,6.5),(2.11,5.6)
]

data_80cm = [
    (0.42,81.3),(0.59,79.9),(0.74,79.8),(0.85,79.1),(0.90,79.8),
    (0.95,79.9),(1.05,79.5),(1.10,79.6),(1.15,78.4),(1.30,79.0),
    (1.52,78.2),(1.76,76.9),(1.82,75.4),(1.88,70.7),(1.84,74.5),
    (1.86,73.4),(1.80,77.0),(1.83,75.9),(1.81,76.8),(1.98,56.4),
    (2.04,36.5),(2.06,25.0),(2.07,19.8),(2.09,12.6),(2.09,8.7),
    (2.09,7.9),(2.09,7.2),(2.10,6.6),(2.10,5.7),(2.10,5.6)
]

data_60cm = [
    (0.71,136.0),(0.90,133.9),(0.99,137.0),(1.10,136.0),(1.38,136.2),
    (1.29,137.7),(1.48,138.0),(1.40,137.5),(1.65,137.4),(1.74,138.5),
    (1.80,136.4),(1.82,137.3),(1.88,129.5),(1.85,132.6),(1.84,133.6),
    (1.81,136.9),(1.98,103.5),(1.94,117.9),(2.03,81.8),(2.08,49.8),
    (2.07,51.5),(2.08,41.7),(2.10,26.2),(2.11,19.2),(2.12,13.3),
    (2.12,10.7),(2.12,8.4),(2.12,7.3),(2.12,6.5),(2.12,5.7)
]

# ---------------------------
def to_arrays(data):
    V = np.array([pt[0] for pt in data], dtype=float)
    I = np.array([pt[1] for pt in data], dtype=float)
    P = V * I
    return V, I, P

V70, I70, P70 = to_arrays(data_70cm)
V80, I80, P80 = to_arrays(data_80cm)
V60, I60, P60 = to_arrays(data_60cm)

# ---------------------------
def interp_I_at_V0(V, I):
    idx = np.argsort(V)
    Vs, Is = V[idx], I[idx]
    return np.interp(0.0, Vs, Is, left=Is[0] + (Is[1]-Is[0])/(Vs[1]-Vs[0])*(0.0-Vs[0]),
                          right=Is[-2] + (Is[-1]-Is[-2])/(Vs[-1]-Vs[-2])*(0.0-Vs[-2]))

def interp_V_at_I0(V, I):
    idx = np.argsort(I)
    Is, Vs = I[idx], V[idx]
    return np.interp(0.0, Is, Vs, left=Vs[0] + (Vs[1]-Vs[0])/(Is[1]-Is[0])*(0.0-Is[0]),
                          right=Vs[-2] + (Vs[-1]-Vs[-2])/(Is[-1]-Is[-2])*(0.0-Is[-2]))

def analyze(name, V, I, P):
    idx = np.argmax(P)
    Vm, Im, Pm = V[idx], I[idx], P[idx]
    Isc = interp_I_at_V0(V, I)
    Voc = interp_V_at_I0(V, I)
    print(f"{name}:  I_sc ≈ {Isc:.2f} mA,  V_oc ≈ {Voc:.2f} V,  P_m = {Pm:.2f} mW @ (V={Vm:.2f} V, I={Im:.2f} mA)")
    return Vm, Im, Pm, Isc, Voc

Vm70, Im70, Pm70, Isc70, Voc70 = analyze("70 cm", V70, I70, P70)
Vm80, Im80, Pm80, Isc80, Voc80 = analyze("80 cm", V80, I80, P80)
Vm60, Im60, Pm60, Isc60, Voc60 = analyze("60 cm", V60, I60, P60)

# ---------------------------
# I–V plot
plt.figure(figsize=(8,5))
plt.plot(V70, I70, '-o', label='70 cm')
plt.plot(V80, I80, '-s', label='80 cm')
plt.plot(V60, I60, '-^', label='60 cm')

plt.scatter([0],[Isc70], color='C0', marker='x', s=80)
plt.scatter([0],[Isc80], color='C1', marker='x', s=80)
plt.scatter([0],[Isc60], color='C2', marker='x', s=80)

plt.scatter([Voc70],[0], color='C0', marker='d', s=60)
plt.scatter([Voc80],[0], color='C1', marker='d', s=60)
plt.scatter([Voc60],[0], color='C2', marker='d', s=60)

plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('I–V curves at 60, 70, 80 cm')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('iv_curve.png', dpi=300)
print("Saved iv_curve.png")

# ---------------------------
# P–V plot
plt.figure(figsize=(8,5))
plt.plot(V70, P70, '-o', label='70 cm')
plt.plot(V80, P80, '-s', label='80 cm')
plt.plot(V60, P60, '-^', label='60 cm')

for Vm, Pm, label in [(Vm70,Pm70,"70 cm"), (Vm80,Pm80,"80 cm"), (Vm60,Pm60,"60 cm")]:
    plt.scatter([Vm],[Pm], s=80, zorder=5)
    plt.annotate(f"{label}\nP_m={Pm:.1f} mW\nV={Vm:.2f} V",
                 xy=(Vm,Pm), xytext=(Vm+0.08,Pm*0.9),
                 arrowprops=dict(arrowstyle='->'), fontsize=9)

plt.xlabel('Voltage (V)')
plt.ylabel('Power (mW)')
plt.title('P–V curves at 60, 70, 80 cm (P_m marked)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('pv_curve.png', dpi=300)
print("Saved pv_curve.png")
