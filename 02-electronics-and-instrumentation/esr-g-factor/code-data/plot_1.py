import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear_func(x, a, b):
    return a * x + b


def plot_and_fit(X, Y,z):
    X = np.array(X)
    Y = np.array(Y)

    # Perform linear curve fitting
    popt, _ = curve_fit(linear_func, X, Y)
    a, b = popt

    # Generate fitted Y values
    Y_fit = linear_func(X, a, b)
    print(a)
    # Plot data points
    plt.scatter(X, Y, color='blue', label='Data points')
    # Plot fitted linear curve
    plt.plot(X, Y_fit, color='red',
             label=f'Fit: $\\frac{{P}}{{Q}}$ = {a:.4f} $I$ + {b:.4f}')
    # Display fit parameters on the plot
    plt.text(0.05, 0.95, f'Slope (a) = {a:.4f}\nIntercept (b) = {b:.4f}',
             transform=plt.gca().transAxes, fontsize=12, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.xlabel(r'$I(mA)$')
    plt.ylabel(r'$\frac{P}{Q}$')
    plt.title(r'$\frac{P}{Q}$ vs I for frequency' + str(z) + ' MHz')
    plt.legend()
    plt.grid(True)
    plt.show()

X=[96, 123, 150, 175, 200, 123, 150, 175, 200, 248, 123, 175, 226, 273, 297, 97, 149, 200, 250, 297, 96, 147, 200, 252, 301]
Y=[3.217391, 4.111111, 4.625, 5.692308, 6.727273, 3.272727, 4, 4.8, 5.538462, 7.2, 3.130435, 4.5, 6, 7.2, 9, 3.130435, 3.789474, 5.142857, 6.545455, 9, 2.482759, 3.789474, 5.142857, 6, 8]
freq=[12.8, 15, 15.75, 16, 16.46]
for i in range(len(freq)):
    plot_and_fit(X[5*i:(5*i+5)],Y[5*i:(5*i+5)],freq[i])
    









