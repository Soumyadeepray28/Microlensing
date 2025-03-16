import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

m = 0.01

#Density formula
def rho(x):
    r0 = 8.5
    rh = 11.41
    n = 0.43
    x0 = r0 / 50
    r = 50 * (x0**2 - 2 * x * x0 * np.cos(np.radians(280)) * np.cos(np.radians(-33)) + x**2)**(1/2)
    rh =  np.exp(- (r / rh)**(1/n))
    return rh

#Main Integrand
def integrand(x, t):
    return 10.15e5 * m *  x**2 * (1 - x)**2 * rho(x) *np.exp(-x * (1 - x)* m * 1e5 / t**2) / t**4

t_values = np.arange(1, 251, 1)  # t from 5 to 250 in steps of 5
integral_values = []

for t in t_values:
    result, _ = spi.quad(integrand, 0, 1, args=(t,))
    res = 1e5 * result
    integral_values.append(res)
    

plt.plot(t_values, integral_values, marker='')
plt.xlabel("t")
plt.ylabel("1e5 * Integral Value")
plt.title("Integral of the function over x from 0 to 1")
plt.grid()

plt.show()


