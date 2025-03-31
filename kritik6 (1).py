import numpy as np
import matplotlib.pyplot as plt

def normal_density(mean, variance, x):
    coefficient = 1 / np.sqrt(2 * np.pi * variance)
    exponent = -((x - mean) ** 2) / (2 * variance)
    return coefficient * np.exp(exponent)

# time to plot the ndf!!
x_values = np.linspace(-10, 10, 1000)
plt.figure(figsize=(10, 6))
plt.plot(x_values, normal_density(0, 1, x_values), label='μ=0, σ²=1')
plt.plot(x_values, normal_density(2, 0.5, x_values), label='μ=2, σ²=0.5')
plt.plot(x_values, normal_density(-1, 2, x_values), label='μ=-1, σ²=2')
plt.title('Normal Distribution Density Functions')
plt.xlabel('x')
plt.ylabel('f_X(x)')
plt.legend()
plt.grid(True)
plt.show()

# using the trapezoidal rule for numerical integration as per the textbook.
# recall: it uses trapezoids instead of rectangles (like in the riemann sum) for a better estimate (solving the 'area problem"!)

def integrate_normal_density(mean, variance, a, b, num_points=1000):
    x_values = np.linspace(a, b, num_points)
    y_values = normal_density(mean, variance, x_values)
    return np.trapz(y_values, x_values)

# Calculating the probability for male heights
mean_height = 171
variance_height = 7.1 ** 2
a = 162
b = 190

probability = integrate_normal_density(mean_height, variance_height, a, b)
print(f"The probability that a random man has a height between {a}cm and {b}cm is: {probability:.4f}")

import numpy as np

# Define the normal probability distribution function :D
def normal_density(mean, variance, x):
    coefficient = 1 / np.sqrt(2 * np.pi * variance)
    exponent = -((x - mean) ** 2) / (2 * variance)
    return coefficient * np.exp(exponent)

# Define the dosage function
def dosage(x):
    return 2.38 * x ** 2

# Defining the function being integrated (the 'integrand' if we're being fancy)
def integrand(x, mean, variance):
    return dosage(x) * normal_density(mean, variance, x)

# Trapezoidal rule for numerical integration
def trapezoidal_rule(func, a, b, num_points, mean, variance):
    x_values = np.linspace(a, b, num_points)
    y_values = func(x_values, mean, variance)
    h = (b - a) / (num_points - 1)
    return h * (0.5 * y_values[0] + 0.5 * y_values[-1] + np.sum(y_values[1:-1]))

# Parameters
mean = 171
variance = 7.1 ** 2
sigma = np.sqrt(variance)

# limits of the integral in question (approximating infinity with μ ± 5σ)
a = mean - 5 * sigma
b = mean + 5 * sigma

# points for trapezoidal rule
num_points = 10000

# finishing and estimating
expected_dosage = trapezoidal_rule(integrand, a, b, num_points, mean, variance)
print(f"Expected dosage: {expected_dosage:.2f}")