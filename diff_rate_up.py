import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define the rho(x) function
def rho(x):
    r0 = 8.5
    rh = 11.41
    n = 0.43
    x0 = r0 / 50
    r = 50 * (x0**2 - 2 * x * x0 * np.cos(np.radians(280)) * np.cos(np.radians(-33)) + x**2)**(1/2)
    rh = np.exp(- (r / rh)**(1/n))
    return rh

# Define the integrand function
def integrand(x, t, m):
    return 10.15e5 * m * x**2 * (1 - x)**2 * rho(x) * np.exp(-x * (1 - x) * m * 1e5 / t**2) / t**4

# Define mass values and temperatures
m_values = [0.01, 0.1, 0.3, 1]
#m_values = [1]


t_values = np.logspace(0.4, 3, 100)  # Log-spaced temperature values
#t_values = np.arange(1, 800, 1)  # t from 5 to 250 in steps of 5
#colors = ['purple', 'blue', 'green', 'red']

# Create the figure
plt.figure(figsize=(8, 5))

# Iterate over different mass values
for m in (m_values):
    integral_values = []
    for t in t_values:
        result, _ = quad(integrand, 0, 1, args=(t, m))
        res = 1e5 * result
        integral_values.append(res)
    
    # Plot with logarithmic scales
    plt.plot(t_values, integral_values, label=f"$M = {m} M_\\odot$")


ticks = [5, 10, 50, 100, 500, 1000]


# Set logarithmic scales
plt.xscale('log')
plt.yscale('log')

#Limits on axis
plt.xlim(2.5, 1000)
plt.ylim(0.001, 100)

# Labels and legend
plt.xlabel("$t = 2t_e$")
plt.ylabel("$10^5 d \\Gamma / dt$")
plt.xticks(ticks, ticks)
plt.legend()
#plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Show plot
plt.show()