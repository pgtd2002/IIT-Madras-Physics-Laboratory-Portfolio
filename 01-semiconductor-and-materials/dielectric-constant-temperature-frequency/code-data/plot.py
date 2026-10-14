import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, make_interp_spline

# --- Data (from your table) ---
freq = np.array([1, 3, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50])  # in kHz
epsilon_r = np.array([2944.343, 2589.603, 2518.655, 2586.055, 2483.181,
                      2532.844, 2504.465, 2508.012, 2483.181, 2589.603,
                      2415.78, 2421.101, 2444.159])
dispersion = np.array([0.011995, 0.031648, 0.051302, 0.073745, 0.048381,
                       0.067293, 0.079847, 0.088844, 0.092363, 0.096321,
                       0.102692, 0.096486, 0.086582])

# --- Interpolation grid (fine) ---
# For freq-domain plots
freq_fine = np.linspace(freq.min(), freq.max(), 500)

# For ln(freq) plot: compute ln for the given freq array and make a fine grid in ln-space
ln_freq = np.log(freq)
ln_freq_fine = np.linspace(ln_freq.min(), ln_freq.max(), 500)

# --- Create cubic spline interpolators ---
# Use make_interp_spline for a smooth cubic spline (can produce overshoot if data wiggles)
spline_eps_vs_freq = make_interp_spline(freq, epsilon_r, k=3)     # εr vs freq
spline_disp_vs_freq = make_interp_spline(freq, dispersion, k=3)    # dispersion vs freq

# For epsilon vs ln(freq), interpolate in ln-space
spline_eps_vs_ln = make_interp_spline(ln_freq, epsilon_r, k=3)

# Evaluate splines on fine grids
epsilon_vs_freq_smooth = spline_eps_vs_freq(freq_fine)
dispersion_vs_freq_smooth = spline_disp_vs_freq(freq_fine)
epsilon_vs_ln_smooth = spline_eps_vs_ln(ln_freq_fine)

# --- Plot settings (reuse style) ---
plt.rcParams.update({
    "figure.figsize": (8,5),
    "axes.grid": True,
    "lines.linewidth": 2,
    "lines.markeredgewidth": 0
})

# 1) epsilon_r vs freq
plt.figure()
plt.plot(freq, epsilon_r, 'o', label='data points', markersize=6)
plt.plot(freq_fine, epsilon_vs_freq_smooth, '-', label='cubic spline (interp)', linewidth=2)
plt.xlabel('Frequency (kHz)')
plt.ylabel('Dielectric constant ($ε_r$)')
plt.title('Dielectric constant vs Frequency (with cubic spline interpolation)')
plt.legend()
plt.tight_layout()
plt.savefig('Dielectric constant vs Frequency', dpi=300, bbox_inches='tight')
plt.show()




# 2) epsilon_r vs ln(freq)
plt.figure()
plt.plot(ln_freq, epsilon_r, 'o', label='data points', markersize=6)
plt.plot(ln_freq_fine, epsilon_vs_ln_smooth, '-', label='cubic spline (interp)', linewidth=2)
plt.xlabel('ln(Frequency)')
plt.ylabel('Dielectric constant ($ε_r$)')
plt.title('Dielectric constant vs ln(Frequency) (with cubic spline interpolation)')
plt.legend()
plt.tight_layout()
plt.savefig('Dielectric constant vs log_Frequency', dpi=300, bbox_inches='tight')
plt.show()

# 3) dispersion factor vs freq
plt.figure()
plt.plot(freq, dispersion, 'o', label='data points', markersize=6)
plt.plot(freq_fine, dispersion_vs_freq_smooth, '-', label='cubic spline (interp)', linewidth=2)
plt.xlabel('Frequency (kHz)')
plt.ylabel('Dispersion factor')
plt.title('Dispersion factor vs Frequency (with cubic spline interpolation)')
plt.legend()
plt.tight_layout()
plt.savefig('Dispersion factor vs Frequency', dpi=300, bbox_inches='tight')
plt.show()
