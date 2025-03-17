import numpy as np
from scipy.integrate import quad
import scipy.constants as const
import matplotlib.pyplot as plt

k = 4 * 22 * 4.301 * 0.01992e9 / (7 * const.c**2)  # G = 4.301e-6
L = 50
#Integrand
def int(x, l):
    r0 = 8.5
    rh = 11.41
    n = 0.43
    x0 = r0 / l
    r = l * (x0**2 - 2 * x * x0 * np.cos(np.radians(280)) * np.cos(np.radians(-33)) + x**2)**(1/2)
    rho =  np.exp(- (r / rh)**(1/n))
    return rho * x * (1-x) 

l_val = np.arange(0.5, 50, 0.5)

int_val = []

for l in l_val:
    res, er = quad(int, 0, 1, args=(l)) 
    result = k * l**2 * res
    int_val.append(result)
   
# Create the plot
fig, ax = plt.subplots()

# Plot the data
ax.plot(l_val, int_val)

# Set major ticks locator and format
ax.xaxis.set_major_locator(plt.MultipleLocator(10))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2))

# Customize the ticks
ax.tick_params(axis='x', which='major', length=10, width=2)
ax.tick_params(axis='x', which='minor', length=5, width=1, color='gray')

# Set labels
ax.set_xlabel('R [kpc]')
ax.set_ylabel('$Optical depth \\tau (d) [10^-7]$')
ax.set_title('Optical depth')

# Show the grid
ax.grid(False, which='both')

# Display the plot
plt.show()