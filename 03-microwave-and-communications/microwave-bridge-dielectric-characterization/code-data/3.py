# sin2_fit_robust_minima.py
# Fit V(x) = A * sin^2(2π*(x - x0)/P) + C to data using robust least squares,
# plot data, fitted curve, fitted minima (red X) and nearest measured minima (green o).
#
# Requires: numpy, scipy, matplotlib, pandas (pandas optional)
# Install with: pip install numpy scipy matplotlib pandas

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from scipy.signal import find_peaks
import pandas as pd

# ------------------ Paste your data here (distance cm, voltage mV) ------------------
data = """
8	1.3
8.2	0.7
8.4	0.7
8.5	0.9
8.6	1.4
8.8	3.1
9	4.7
9.3	5.2
9.5	4.8
9.7	3.3
9.8	2.4
9.9	1.5
10	0.9
10.1	0.5
10.2	0.7
10.3	1.1
10.5	2.3
10.8	3.7
11	4.9
11.1	5.2
11.2	5.3
11.3	5.2
11.4	5
11.5	4.2
11.8	1.4
11.9	0.8
12	0.5
12.1	0.5
12.2	0.9
11.7	0.6
12.5	2.7
"""
# ------------------------------------------------------------------------------

# Parse data
xs, ys = [], []
for line in data.strip().splitlines():
    a, b = line.split()
    xs.append(float(a)); ys.append(float(b))
x = np.array(xs)
y = np.array(ys)

# Basic sanity
if len(x) != len(y):
    n = min(len(x), len(y))
    x = x[:n]; y = y[:n]
print(f"Loaded {len(x)} points: distance {x.min():.2f}–{x.max():.2f} cm")

# Optional: show data table
try:
    df = pd.DataFrame({'distance_cm': x, 'voltage_mV': y})
    print(df.to_string(index=False))
except Exception:
    pass

# Model function
def sin2_model(x, params):
    A, P, x0, C = params
    return A * np.sin(2 * np.pi * (x - x0) / P)**2 + C

# Residual function for least_squares (robust loss will be used)
def residuals(params, x, y):
    return sin2_model(x, params) - y

# ---------------- initial guesses ----------------
A0 = max(y) - min(y)
C0 = min(y)
# crude minima detection to estimate P: find minima in negative interpolated signal
x_dense_tmp = np.linspace(x.min(), x.max(), 2000)
y_interp = np.interp(x_dense_tmp, x, y)
peaks_neg, _ = find_peaks(-y_interp, distance=40, prominence=0.1)
if len(peaks_neg) >= 2:
    spacings = np.diff(x_dense_tmp[peaks_neg])
    P0 = 2.0 * np.mean(spacings)   # sin^2 minima spacing ~ P/2
else:
    P0 = (x.max() - x.min()) / 3.0  # fallback
x0_0 = x[np.argmin(y)]  # phase near first measured minimum

p0 = np.array([A0 if A0>0 else 1.0, P0 if P0>0 else 3.5, x0_0, C0])
print("\nInitial guesses:")
print(f"  A0={p0[0]:.3f}, P0={p0[1]:.3f}, x0_0={p0[2]:.3f}, C0={p0[3]:.3f}")

# bounds for parameters: A>0, P>0
lower = [0.0, 0.1, x.min()-1.0, -np.inf]
upper = [10*A0 if A0>0 else 100.0, (x.max()-x.min())*3.0, x.max()+1.0, np.inf]

# -------------- robust least-squares fit ----------------
res = least_squares(residuals, p0, args=(x, y), bounds=(lower, upper),
                    loss='soft_l1', f_scale=0.1, max_nfev=200000)
A_fit, P_fit, x0_fit, C_fit = res.x

# Estimate covariance approx (not exact for robust loss, but useful)
# Using Jacobian at solution and residual variance (approx)
try:
    J = res.jac
    # compute approx cov = inv(J^T J) * s2, where s2 = rss/(n-p)
    rss = 2 * res.cost  # cost = 0.5 * sum(r^2) so rss = sum(r^2) = 2*cost
    dof = max(1, len(y) - len(res.x))
    s2 = rss / dof
    cov = np.linalg.inv(J.T.dot(J)) * s2
    perr = np.sqrt(np.abs(np.diag(cov)))
except Exception:
    perr = np.repeat(np.nan, 4)

print("\nFitted parameters (robust fit):")
print(f"  A  = {A_fit:.6f} ± {perr[0]:.6f}  (mV)")
print(f"  P  = {P_fit:.6f} ± {perr[1]:.6f}  (cm)  (minima spacing ≈ P/2)")
print(f"  x0 = {x0_fit:.6f} ± {perr[2]:.6f}  (cm)")
print(f"  C  = {C_fit:.6f} ± {perr[3]:.6f}  (mV)")

# ---------------- find minima on fitted curve ----------------
x_dense = np.linspace(x.min(), x.max(), 4000)
y_fit = sin2_model(x_dense, res.x)

# find minima (peaks in -y_fit). Tune distance to avoid spurious minima.
min_distance_samples = max(3, int(0.25 / (x_dense[1]-x_dense[0])))
peaks_idx, props = find_peaks(-y_fit, distance=min_distance_samples, prominence=1e-6)
fitted_min_x = x_dense[peaks_idx]
fitted_min_y = y_fit[peaks_idx]

print("\nFitted minima (from fitted curve):")
for xi, yi in zip(fitted_min_x, fitted_min_y):
    print(f"  {xi:.6f} cm, {yi:.6f} mV")

# Map fitted minima to nearest measured points
nearest_idx = [np.argmin(np.abs(x - xi)) for xi in fitted_min_x]
nearest_measured = [(x[idx], y[idx]) for idx in nearest_idx]
print("\nNearest measured points to fitted minima:")
for (xm, ym), xi in zip(nearest_measured, fitted_min_x):
    print(f"  measured {xm:.6f} cm, {ym:.6f} mV  (nearest to fitted {xi:.6f} cm)")

# Also compute measured local minima directly from raw data (for comparison)
# We consider measured minima as points that are lower than their neighbors.
measured_min_indices = []
for i in range(1, len(y)-1):
    if y[i] < y[i-1] and y[i] <= y[i+1]:
        measured_min_indices.append(i)
# include boundary if needed
measured_min_x = x[measured_min_indices]
measured_min_y = y[measured_min_indices]
if len(measured_min_x) > 0:
    print("\nMeasured local minima (raw data):")
    for xm, ym in zip(measured_min_x, measured_min_y):
        print(f"  {xm:.6f} cm, {ym:.6f} mV")

# ---------------- Plot ----------------
plt.figure(figsize=(10,5))
# raw data (blue default)
plt.scatter(x, y, label='measured points', edgecolor='k', zorder=5, s=50)

# fitted curve (orange)
plt.plot(x_dense, y_fit, label='sin^2 fit (robust)', linewidth=2, color='tab:orange', zorder=3)

# fitted minima (red X)
plt.scatter(fitted_min_x, fitted_min_y, marker='x', s=130, color='red', label='fitted minima', zorder=7)

# nearest measured points to fitted minima (green circle)
for (xm, ym) in nearest_measured:
    plt.scatter(xm, ym, marker='o', s=100, facecolors='none', edgecolors='green', linewidths=2,
                label='nearest measured to fitted minima' if 'nearest_measured_marker' not in globals() else "")
    globals()['nearest_measured_marker'] = True

# measured raw minima (solid green dot)
if len(measured_min_x) > 0:
    plt.scatter(measured_min_x, measured_min_y, marker='o', s=90, color='green', alpha=0.7, label='measured local minima', zorder=6)

# annotate fitted minima
for xi, yi in zip(fitted_min_x, fitted_min_y):
    plt.annotate(f"{xi:.3f} cm\n{yi:.3f} mV", xy=(xi, yi), xytext=(0,-18), textcoords='offset points',
                 ha='center', fontsize=9, color='red')

plt.xlabel('Distance (cm)')
plt.ylabel('Voltage (mV)')
plt.title('Sin^2 robust fit — data (points), fit (orange), fitted minima (red X)')
plt.legend(loc='best')
plt.grid(alpha=0.4, linestyle='--')
plt.tight_layout()

# Optional: save figure and minima CSV (uncomment to enable)
# plt.savefig("sin2_robust_fit_lifted_minima.png", dpi=300)
# import csv
# with open("fitted_minima.csv","w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["min_distance_cm","min_voltage_mV"])
#     for xi, yi in zip(fitted_min_x, fitted_min_y):
#         writer.writerow([f"{xi:.6f}", f"{yi:.6f}"])

plt.show()
