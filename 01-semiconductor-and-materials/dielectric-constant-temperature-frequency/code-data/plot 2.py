import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# --- 20 kHz data ---
temp_20 = np.array([40, 50, 60, 70, 80, 90, 100, 110, 120, 130,
                    140, 145, 150, 155, 160, 170])
epsilon_20 = np.array([2547.034, 2508.012, 2532.844, 2557.676, 2642.814,
                       2717.309, 2979.817, 3096.881, 3440.979, 3937.615,
                       4224.955, 4185.933, 3902.141, 3547.401, 3352.294, 2859.205])

# --- 40 kHz data ---
temp_40 = np.array([40, 50, 60, 70, 80, 90, 100, 110, 120, 130,
                    140, 145, 150, 155, 160])
epsilon_40 = np.array([2511.56, 2483.181, 2493.823, 2532.844, 2649.908,
                       2710.214, 2901.774, 3103.976, 3370.031, 3973.089,
                       4139.817, 4044.037, 3714.129, 3533.211, 3320.367])

# --- Interpolation (cubic spline) ---
temp_20_fine = np.linspace(temp_20.min(), temp_20.max(), 500)
spline_20 = make_interp_spline(temp_20, epsilon_20, k=3)
epsilon_20_smooth = spline_20(temp_20_fine)

temp_40_fine = np.linspace(temp_40.min(), temp_40.max(), 500)
spline_40 = make_interp_spline(temp_40, epsilon_40, k=3)
epsilon_40_smooth = spline_40(temp_40_fine)

# --- Plot both in one figure ---
plt.figure(figsize=(8,6))
# Raw data points
plt.plot(temp_20, epsilon_20, 'o', label="20 kHz data", markersize=6)
plt.plot(temp_40, epsilon_40, 's', label="40 kHz data", markersize=6)
# Smooth curves
plt.plot(temp_20_fine, epsilon_20_smooth, '-', label="20 kHz spline")
plt.plot(temp_40_fine, epsilon_40_smooth, '-', label="40 kHz spline")

plt.xlabel("Temperature (°C)")
plt.ylabel("Dielectric constant (εr)")
plt.title("Dielectric Constant vs Temperature at 20 kHz and 40 kHz")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
