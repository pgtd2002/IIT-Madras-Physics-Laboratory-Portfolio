# sin2_fit_and_minima_newdata.py
# Fit V(x) = A * sin^2(2π*(x - x0)/P) + C to the provided data,
# plot data (one color), fitted curve (different color), and mark fitted minima with a distinct marker.
#
# Requirements: numpy, scipy, matplotlib, pandas (pandas optional)
# Install: pip install numpy scipy matplotlib pandas
#
# Copy & run locally.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import pandas as pd

# ------------------ Paste data here (distance cm, voltage mV) ------------------
data = """
8    9.5
8.1  11.4
8.2  14.3
8.3  16.4
8.4  17.1
8.5  16.8
8.6  15.9
8.8  14.2
9    11.7
9.2  7.4
9.3  4.2
9.4  1.9
9.45 1.2
9.5  0.8
9.55 0.3
9.6  0.5
9.7  1.9
9.8  4.4
9.9  7.7
10   11
10.2 14.4
10.3 15.4
10.5 15.7
10.6 15
10.7 14.2
11   9.2
11.1 7.1
11.2 4.9
11.3 1.8
11.36 0.9
11.4 0.5
11.5 0.2
11.55 0.9
11.6 1.6
11.7 3.6
11.9 9.5
12.1 13.7
12.2 14.5
12.3 14.6
12.5 14.3
12.8 11.4
13   7
13.1 4
13.2 2
13.25 1.2
13.3 0.5
13.35 0.2
13.4 0.2
13.45 0.5
13.5 1.5
13.6 3.3
13.8 8.8
13.9 11.4
"""
# ------------------------------------------------------------------------------

# Parse
xs, ys = [], []
for line in data.strip().splitlines():
    a, b = line.split()
    xs.append(float(a)); ys.append(float(b))
x = np.array(xs)
y = np.array(ys)

# Sanity check
if len(x) != len(y):
    n = min(len(x), len(y))
    print(f"Warning: lengths differ, truncating to {n} points.")
    x = x[:n]; y = y[:n]

print(f"Loaded {len(x)} points (distance range {x.min():.2f}–{x.max():.2f} cm).")

# Optional: show the data as a table
try:
    df = pd.DataFrame({'distance_cm': x, 'voltage_mV': y})
    print(df.to_string(index=False))
except Exception:
    pass

# Model: A * sin(2*pi*(x - x0)/P)^2 + C
def sin2_model(x, A, P, x0, C):
    return A * np.sin(2 * np.pi * (x - x0) / P)**2 + C

# ---------- Estimate initial guesses ----------
A0 = (y.max() - y.min())            # amplitude estimate
C0 = y.min()                        # offset estimate

# crude estimate of period P:
# detect approximate minima in raw data and measure spacing
# Use a coarse dense interpolation to find minima peaks in -y
x_dense_tmp = np.linspace(x.min(), x.max(), 2000)
y_interp = np.interp(x_dense_tmp, x, y)
peaks_neg, _ = find_peaks(-y_interp, distance=50, prominence=0.1)
if len(peaks_neg) >= 2:
    # spacing between consecutive minima (average)
    spacings = np.diff(x_dense_tmp[peaks_neg])
    P0 = 2.0 * np.mean(spacings)  # sin^2 minima spacing ~ P/2 -> P ≈ 2 * spacing
else:
    P0 = 3.6  # fallback guess if minima detection fails

# phase guess near first measured minimum (smallest y)
x0_0 = x[np.argmin(y)]

print(f"\nInitial guesses: A0={A0:.3f}, P0={P0:.3f}, x0_0={x0_0:.3f}, C0={C0:.3f}")

p0 = [A0, P0, x0_0, C0]

# Bounds: A>0, P>0
lower = [0.0, 0.1, x.min()-1.0, -np.inf]
upper = [10*A0 if A0>0 else 100.0, (x.max()-x.min())*3.0, x.max()+1.0, np.inf]

# ---------- Fit ----------
popt, pcov = curve_fit(sin2_model, x, y, p0=p0, bounds=(lower, upper), maxfev=200000)
A_fit, P_fit, x0_fit, C_fit = popt
perr = np.sqrt(np.abs(np.diag(pcov)))

print("\nFitted parameters:")
print(f"  A  = {A_fit:.6f} ± {perr[0]:.6f}  (mV)")
print(f"  P  = {P_fit:.6f} ± {perr[1]:.6f}  (cm)  (minima spacing ≈ P/2)")
print(f"  x0 = {x0_fit:.6f} ± {perr[2]:.6f}  (cm)")
print(f"  C  = {C_fit:.6f} ± {perr[3]:.6f}  (mV)")

# ---------- Evaluate fitted curve and find minima ----------
x_dense = np.linspace(x.min(), x.max(), 4000)
y_fit = sin2_model(x_dense, *popt)

# find minima on fitted curve (peaks of -y_fit)
# set distance in samples corresponding to ~0.3 cm to avoid spurious nearby minima
min_distance_samples = max(3, int(0.3 / (x_dense[1]-x_dense[0])))
peaks_idx, props = find_peaks(-y_fit, distance=min_distance_samples, prominence=1e-5)
min_x = x_dense[peaks_idx]
min_y = y_fit[peaks_idx]

print("\nDetected minima (fitted curve):")
for xi, yi in zip(min_x, min_y):
    print(f"  {xi:.6f} cm, {yi:.6f} mV")

# Map minima to nearest measured points
nearest_idx = [np.argmin(np.abs(x - xi)) for xi in min_x]
print("\nNearest measured points to fitted minima:")
for idx, xi in zip(nearest_idx, min_x):
    print(f"  Measured: {x[idx]:.6f} cm, {y[idx]:.6f} mV  (nearest to {xi:.6f} cm)")

# ---------- Plot ----------
plt.figure(figsize=(10,5))

# raw data points (blue markers)
plt.scatter(x, y, label='data points', edgecolor='k', zorder=5, s=50)

# fitted sin^2 curve (distinct color)
plt.plot(x_dense, y_fit, label='sin^2 fit', linewidth=2.0, color='tab:orange', zorder=3)

# fitted minima (red X)
plt.scatter(min_x, min_y, marker='x', color='red', s=120, label='fitted minima', zorder=6)

# annotate minima
for xi, yi in zip(min_x, min_y):
    plt.annotate(f"{xi:.3f} cm\n{yi:.3f} mV",
                 xy=(xi, yi), xytext=(0,-18), textcoords='offset points',
                 ha='center', fontsize=9, color='red')

plt.xlabel('Distance (cm)')
plt.ylabel('Voltage (mV)')
plt.title('Sin^2 fit — data (points), fit (orange), minima (red X)')
plt.legend()
plt.grid(alpha=0.4, linestyle='--')
plt.tight_layout()

# Optional: save the figure and minima to CSV
# plt.savefig("sin2_fit_plot.png", dpi=300)
# import csv
# with open("fitted_minima.csv","w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["min_distance_cm","min_voltage_mV"])
#     for xi, yi in zip(min_x, min_y):
#         writer.writerow([f"{xi:.6f}", f"{yi:.6f}"])

plt.show()
