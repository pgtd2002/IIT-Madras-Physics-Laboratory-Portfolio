import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear_func(x, a, b):
    return a * x + b


def plot_and_fit(X, Y):
    X = np.array(X)
    Y = np.array(Y)

    # Perform linear curve fitting
    popt, _ = curve_fit(linear_func, X, Y)
    a, b = popt

    # Generate fitted Y values
    Y_fit = linear_func(X, a, b)

    # Plot data points
    plt.scatter(X, Y, color='blue', label='Data points')
    # Plot fitted linear curve
    plt.plot(X, Y_fit, color='red',
             label=f'Fit: $\\beta_{{total}}\\cos(\\theta) = {a:.4f}\\cdot 4\,\\sin(\\theta) + {b:.4f}$')
    # Display fit parameters on the plot
    plt.text(0.05, 0.95, f'Slope (a) = {a:.4f}\nIntercept (b) = {b:.4f}',
             transform=plt.gca().transAxes, fontsize=12, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.xlabel(r'$4\,\sin(\theta)$')
    plt.ylabel(r'$\beta_{total}\cos(\theta)$')
    plt.title('Linear Fit of Williamson-Hall plot (Gaussian fit data set)')
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage with your data:
# X = [1.241747794, 1.091201254, 1.609559732, 2.232886484, 1.18062453, 2.082882082, 1.893235313]
# Y = [0.009015049, 0.005616019, 0.010791499, 0.008663027, 0.008904007, 0.010505343, 0.008526108]
#
# plot_and_fit(X, Y)


x1=[1.091322151, 1.241743812, 1.609536405, 2.232870845, 1.180585843, 2.082849003, 1.89332141]
Y1=[0.005991922, 0.008889292, 0.010825882, 0.007492708, 0.008428942, 0.010400804, 0.008423757]
plot_and_fit(x1,Y1)

'''
X2 = [1.09120931, 1.60957571, 1.8932184, 2.08289639]
Y2 = [0.00572012, 0.01032476, 0.00815345, 0.0102091]
plot_and_fit(X2, Y2)
'''