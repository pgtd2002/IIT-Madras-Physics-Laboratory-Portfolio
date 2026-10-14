# plot_iv_pv_hardcoded.py
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Hard-coded data (from user's pasted table)
# Three datasets are given column-wise in the paste; each is a list of (V [V], I [mA])
# Dataset A: left block
data_A = [
    (0.54,101.5),(0.69,101.55),(0.76,102.75),(0.89,103.0),(1.04,103.1),
    (1.11,104.1),(1.24,103.3),(1.31,103.0),(1.43,103.7),(1.57,103.5),
    (1.63,103.6),(1.73,101.8),(1.86,97.9),(1.90,93.4),(1.94,85.9),
    (2.00,69.5),(2.05,45.8),(2.08,26.1),(2.09,21.0),(2.09,19.3),
    (2.10,17.6),(2.10,14.4),(2.10,13.0),(2.11,10.7),(2.11,9.0),
    (2.11,7.9),(2.11,7.0),(2.11,6.5),(2.11,5.6)
]

# Dataset B: middle block
data_B = [
    (0.42,81.3),(0.59,79.9),(0.74,79.8),(0.85,79.1),(0.90,79.8),
    (0.95,79.9),(1.05,79.5),(1.10,79.6),(1.15,78.4),(1.30,79.0),
    (1.52,78.2),(1.76,76.9),(1.82,75.4),(1.88,70.7),(1.84,74.5),
    (1.86,73.4),(1.80,77.0),(1.83,75.9),(1.81,76.8),(1.98,56.4),
    (2.04,36.5),(2.06,25.0),(2.07,19.8),(2.09,12.6),(2.09,8.7),
    (2.09,7.9),(2.09,7.2),(2.10,6.6),(2.10,5.7),(2.10,5.6)
]

# Dataset C: right block
data_C = [
    (0.71,136.0),(0.90,133.9),(0.99,137.0),(1.10,136.0),(1.38,136.2),
    (1.29,137.7),(1.48,138.0),(1.40,137.5),(1.65,137.4),(1.74,138.5),
    (1.80,136.4),(1.82,137.3),(1.88,129.5),(1.85,132.6),(1.84,133.6),
    (1.81,136.9),(1.98,103.5),(1.94,117.9),(2.03,81.8),(2.08,49.8),
    (2.07,51.5),(2.08,41.7),(2.10,26.2),(2.11,19.2),(2.12,13.3),
    (2.12,10.7),(2.12,8.4),(2.12,7.3),(2.12,6.5),(2.12,5.7)
]

# ---------------------------
# Convert to numpy arrays and compute P = V * I (units: mW because I is in mA)
def to_arrays(data):
    V = np.array([pt[0] for pt in data], dtype=float)
    I = np.array([pt[1] for pt in data], dtype=float)
    P = V * I   # mW (V * mA)
    return V, I, P

V_A, I_A, P_A = to_arrays(data_A)
V_B, I_B, P_B = to_arrays(data_B)
V_C, I_C, P_C = to_arrays(data_C)

# ---------------------------
# Print max-power points (Vm, Im, Pm) for each dataset
def print_max_point(name, V, I, P):
    idx = np.argmax(P)
    Vm = V[idx]; Im = I[idx]; Pm = P[idx]
    print(f"{name}  Max power point: V_m = {Vm:.3f} V, I_m = {Im:.3f} mA, P_m = {Pm:.3f} mW (index {idx})")

print_max_point("Dataset A (left)", V_A, I_A, P_A)
print_max_point("Dataset B (middle)", V_B, I_B, P_B)
print_max_point("Dataset C (right)", V_C, I_C, P_C)

# ---------------------------
# Plot I-V curves
plt.figure(figsize=(8,5))
plt.plot(V_A, I_A, marker='o', linestyle='-', label='Set A (left block)')
plt.plot(V_B, I_B, marker='s', linestyle='-', label='Set B (middle block)')
plt.plot(V_C, I_C, marker='^', linestyle='-', label='Set C (right block)')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('I–V curves (hard-coded data)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('iv_curve.png', dpi=300)
print("Saved iv_curve.png")

# ---------------------------
# Plot P-V curves and mark max-power points
plt.figure(figsize=(8,5))
plt.plot(V_A, P_A, marker='o', linestyle='-', label='Set A (left)')
idxA = np.argmax(P_A)
plt.scatter(V_A[idxA], P_A[idxA], color='red', zorder=5)
plt.annotate(f"P_m={P_A[idxA]:.1f} mW\nV={V_A[idxA]:.2f} V", xy=(V_A[idxA], P_A[idxA]),
             xytext=(V_A[idxA]+0.08, P_A[idxA]*0.92), arrowprops=dict(arrowstyle='->'), fontsize=9)

plt.plot(V_B, P_B, marker='s', linestyle='-', label='Set B (middle)')
idxB = np.argmax(P_B)
plt.scatter(V_B[idxB], P_B[idxB], color='red', zorder=5)
plt.annotate(f"P_m={P_B[idxB]:.1f} mW\nV={V_B[idxB]:.2f} V", xy=(V_B[idxB], P_B[idxB]),
             xytext=(V_B[idxB]+0.08, P_B[idxB]*0.92), arrowprops=dict(arrowstyle='->'), fontsize=9)

plt.plot(V_C, P_C, marker='^', linestyle='-', label='Set C (right)')
idxC = np.argmax(P_C)
plt.scatter(V_C[idxC], P_C[idxC], color='red', zorder=5)
plt.annotate(f"P_m={P_C[idxC]:.1f} mW\nV={V_C[idxC]:.2f} V", xy=(V_C[idxC], P_C[idxC]),
             xytext=(V_C[idxC]+0.08, P_C[idxC]*0.92), arrowprops=dict(arrowstyle='->'), fontsize=9)

plt.xlabel('Voltage (V)')
plt.ylabel('Power (mW)')
plt.title('P–V curves (hard-coded data) — max-power points marked')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('pv_curve.png', dpi=300)
print("Saved pv_curve.png")

# ---------------------------
# Optionally show the figures (uncomment if running interactively)
# plt.show()
