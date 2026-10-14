import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_func(x, a, b):
    return a * x + b

# Given data
Y1 = [-1.7076, -1.71775, -1.73837, -1.75943, -1.79186, -1.82255, -1.86007, -1.90519, -1.95892, -2.00884, -2.08321, -2.13219, -2.19185, -2.26407, -2.32772, -2.40075, -2.47408, -2.54735, -2.62011, -2.70541, -2.77636, -2.85273, -2.91833, -3.00688, -3.08385, -3.15642, -3.24636, -3.30699, -3.38495, -3.44052, -3.51463, -3.59467, -3.62857, -3.68168, -3.74743, -3.78704, -3.86037, -3.93248, -4.00515]
X1 = [0.003343, 0.00331, 0.003277, 0.003245, 0.003214, 0.003183, 0.003153, 0.003124, 0.003095, 0.003066, 0.003038, 0.003011, 0.002984, 0.002957, 0.002931, 0.002906, 0.002881, 0.002856, 0.002832, 0.002808, 0.002784, 0.002761, 0.002739, 0.002716, 0.002694, 0.002673, 0.002651, 0.002631, 0.00261, 0.00259, 0.00257, 0.00255, 0.002531, 0.002512, 0.002493, 0.002474, 0.002456, 0.002438, 0.00242]
X2 = [0.00245, 0.002468, 0.002487, 0.002505, 0.002524, 0.002544, 0.002563, 0.002583, 0.002603, 0.002624, 0.002644, 0.002666, 0.002687, 0.002709, 0.002731, 0.002754, 0.002777, 0.0028, 0.002824, 0.002848, 0.002872, 0.002897, 0.002923, 0.002949, 0.002975, 0.003002, 0.003029, 0.003057, 0.003085, 0.003114]
Y2 = [-3.84527, -3.76902, -3.70933, -3.6217, -3.56835, -3.48731, -3.42212, -3.34651, -3.27622, -3.2015, -3.11637, -3.03887, -2.96517, -2.88746, -2.81077, -2.72757, -2.64624, -2.56803, -2.48776, -2.41397, -2.34191, -2.28184, -2.20422, -2.13994, -2.06861, -2.01226, -1.95244, -1.896, -1.84547, -1.81128]

# Trim data for heating (X1 in 0.0026 to 0.0030)
X1 = np.array(X1)
Y1 = np.array(Y1)
mask1 = (X1 >= 0.0026) & (X1 <= 0.00296)
X1_trimmed = X1[mask1]
Y1_trimmed = Y1[mask1]

# Linear fit for heating
popt1, _ = curve_fit(linear_func, X1_trimmed, Y1_trimmed)
a1, b1 = popt1

# Trim data for cooling (X2 in 0.00255 to 0.0029)
X2 = np.array(X2)
Y2 = np.array(Y2)
mask2 = (X2 >= 0.00255) & (X2 <= 0.0029)
X2_trimmed = X2[mask2]
Y2_trimmed = Y2[mask2]

# Linear fit for cooling
popt2, _ = curve_fit(linear_func, X2_trimmed, Y2_trimmed)
a2, b2 = popt2

# Plot heating fit
plt.figure(figsize=(8, 5))
plt.scatter(X1_trimmed, Y1_trimmed, color='red', label='Heating data')
plt.plot(X1_trimmed, linear_func(X1_trimmed, a1, b1), color='darkred', label=f'Fit: $\\ln(\\rho_c)$= {a1:.2f} $\\frac{{1}}{{T}}$ + {b1:.2f}')
plt.xlabel(r'$1/T \ (K^{-1})$')
plt.ylabel(r'$\ln(\rho_c)$')
plt.title(f'Heating Plot with Fit\n $\\ln(\\rho_c)$ = {a1:.2f} $\\frac{{1}}{{T}}$ + {b1:.2f}')
plt.legend()
plt.grid(True)
plt.show()

# Plot cooling fit
plt.figure(figsize=(8, 5))
plt.scatter(X2_trimmed, Y2_trimmed, color='blue', label='Cooling data')
plt.plot(X2_trimmed, linear_func(X2_trimmed, a2, b2), color='darkblue', label=f'Fit: $\\ln(\\rho_c)$ = {a2:.2f} $\\frac{{1}}{{T}}$ + {b2:.2f}')
plt.xlabel(r'$1/T \ (K^{-1})$')
plt.ylabel(r'$\ln(\rho_c)$')
plt.title(f'Cooling Plot with Fit\n $\\ln(\\rho_c)$ = {a2:.2f} $\\frac{{1}}{{T}}$ + {b2:.2f}')
plt.legend()
plt.grid(True)
plt.show()
