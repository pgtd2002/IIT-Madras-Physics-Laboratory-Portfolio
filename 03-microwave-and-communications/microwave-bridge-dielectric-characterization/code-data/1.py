# sin2_fit_and_minima.py
# Requires: numpy, scipy, matplotlib, pandas (pandas optional)
# Install with: pip install numpy scipy matplotlib pandas

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import pandas as pd

# ---------- Paste your data here (distance cm, voltage mV) ----------
data = """
7.5 3.9
8.2 1.4
8.3 0.8
8.35 0.5
8.4 0.3
8.45 0.2
8.46 0.1
8.5 0.1
8.6 0.1
8.64 0.2
8.7 0.3
8.8 0.9
8.9 1.2
9 1.8
9.1 2.3
9.3 3.2
9.4 3.6
9.5 3.8
9.7 3.7
9.8 3.3
9.9 2.7
10 1.9
10.2 0.6
10.23 0.5
10.3 0.2
10.37 0.1
10.4 0.1
10.45 0.1
10.5 0.2
10.6 0.4
10.8 1.4
11 2.6
11.2 3.3
11.3 3.5
11.35 3.8
11.38 3.8
11.4 3.9
11.45 3.8
11.6 3.4
11.8 2.1
12 1
12.1 0.5
12.14 0.3
12.2 0.2
12.25 0.1
12.3 0.1
12.4 0.2
12.5 0.4
12.6 0.8
12.8 1.8
"""
# ---------------------------------------------------------------------

# Parse the data
xs, ys = [], []
for line in data.strip().splitlines():
    a, b = line.split()
    xs.append(float(a)); ys.append(float(b))
x = np.array(xs)
y = np.array(ys)

# Basic check
if len(x) != len(y):
    min_len = min(len(x), len(y))
    print(f"Warning: mismatched lengths. Truncating to {min_len} points.")
    x = x[:min_len]; y = y[:min_len]

print(f"Loaded {len(x)} data points.")

# Optional: show table (requires pandas)
try:
    print("\nFirst few rows of data:")
    print(pd.DataFrame({'distance_cm': x, 'voltage_mV': y}).head(10).to_string(index=False))
except Exception:
    pass

# Define model: A * sin(2*pi*(x - x0)/P)^2 + C
def sin2_model(x, A, P, x0, C):
    return A * np.sin(2 * np.pi * (x - x0) / P)**2 + C

# Initial parameter guesses
A0 = max(y) - min(y)
# From visual spacing, estimate P: sin^2 period ~ ~3.7 (empirical guess)
P0 = 3.7
x0_0 = x[np.argmin(y)]  # phase near first minimum
C0 = min(y)
p0 = [A0, P0, x0_0, C0]

# Bounds (A>0, P>0)
lower = [0.0, 0.1, x.min()-1.0, -np.inf]
upper = [10*A0, 20.0, x.max()+1.0, np.inf]

# Fit
popt, pcov = curve_fit(sin2_model, x, y, p0=p0, bounds=(lower, upper), maxfev=20000)
A_fit, P_fit, x0_fit, C_fit = popt
perr = np.sqrt(np.abs(np.diag(pcov)))

print("\nFitted parameters:")
print(f"  A  = {A_fit:.6f} ± {perr[0]:.6f}  (mV, amplitude)")
print(f"  P  = {P_fit:.6f} ± {perr[1]:.6f}  (cm, period of sin^2; minima spacing ≈ P/2)")
print(f"  x0 = {x0_fit:.6f} ± {perr[2]:.6f}  (cm, phase shift)")
print(f"  C  = {C_fit:.6f} ± {perr[3]:.6f}  (mV, offset)")

# Dense grid to evaluate fit
x_dense = np.linspace(x.min(), x.max(), 3000)
y_fit = sin2_model(x_dense, *popt)

# Find minima of fitted curve: peaks of -y_fit
# distance parameter helps avoid detecting very close spurious minima. Choose in samples.
min_distance_samples = int(0.3 / (x_dense[1]-x_dense[0]))  # ~0.3 cm spacing minimum
peaks_idx, _ = find_peaks(-y_fit, distance=min_distance_samples, prominence=1e-4)
min_x = x_dense[peaks_idx]
min_y = y_fit[peaks_idx]

print("\nDetected minima (from fitted curve):")
for xi, yi in zip(min_x, min_y):
    print(f"  {xi:.6f} cm, {yi:.6f} mV")

# Also map minima to nearest measured data point (useful for experimental reference)
nearest_idx = [np.argmin(np.abs(x - xi)) for xi in min_x]
print("\nNearest measured points to fitted minima:")
for idx, xi in zip(nearest_idx, min_x):
    print(f"  Measured: {x[idx]:.6f} cm, {y[idx]:.6f} mV  (nearest to fitted minima {xi:.6f} cm)")

# Plot: raw points, fit, and minima with different colors
plt.figure(figsize=(10,5))
plt.scatter(x, y, label='data points', zorder=5, s=45, edgecolor='k')         # raw points (blue default)
plt.plot(x_dense, y_fit, label='sin^2 fit', linewidth=2, zorder=3, color='tab:orange')  # fit (orange)
plt.scatter(min_x, min_y, marker='x', s=120, label='fitted minima', color='red', zorder=6)  # minima (red X)

# Annotate minima
for xi, yi in zip(min_x, min_y):
    plt.annotate(f"{xi:.3f} cm\n{yi:.3f} mV", xy=(xi, yi), xytext=(0,-18),
                 textcoords='offset points', ha='center', fontsize=9, color='red')

plt.xlabel('Distance (cm)')
plt.ylabel('Voltage (mV)')
plt.title('Distance vs Voltage — sin^2 fit (orange) and minima (red X)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save figure optionally:
# plt.savefig("distance_voltage_sin2_fit.png", dpi=300)

plt.show()
