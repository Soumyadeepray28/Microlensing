import numpy as np
from scipy.integrate import quad

#constant
k = 4.61e-7

def tau(r, l):
    a = 5 / l
    return  1 / (a**2 + r**2)

def int(x, l):
    r0 = 8.5
    r = ((r0 / l)**2 - 2 * (r0 / l) * np.cos(np.radians(281)) * np.cos(np.radians(-32.8)) * x + x**2)**(1/2)
    return x* (1-x) * tau(r, l)

L = 55

result, err = quad(int, 0, 1, args=(L))

print(k * result)

#paper: Griest1991:
#Link: https://ui.adsabs.harvard.edu/abs/1991ApJ...366..412G/abstract