import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

#constant
k = 4.61e-7

def tau(r, l):
    a = 5 / l
    return  1 / (a**2 + r**2)

def int(x, l):
    r0 = 8.5
    r = ((r0 / l)**2 - 2 * (r0 / l) * np.cos(np.radians(281)) * np.cos(np.radians(-32.8)) * x + x**2)**(1/2)
    return x* (1-x) * tau(r, l)

l_val = np.arange(0.5, 50, 0.5)


int_val = []
int_val1 = []

for t in l_val:
    l = t
    res, er = quad(int, 0, 1, args=(l)) 
    result = k * res
    int_val.append(result)
    int_val1.append(l)
    

int_val = np.array(int_val)
int_val1 = np.array(int_val1)

L = 55

result1, err = quad(int, 0, 1, args=(L))

print(k * result1) 

# Create the plot
fig, ax = plt.subplots()

# Plot the data
ax.plot(l_val, int_val, label = 'By parts', color = 'orange', linestyle = ':')
#ax.plot(l_value, int_val1, label = 'Direct', color = 'green', linestyle = '--')

# Set major ticks locator and format
ax.xaxis.set_major_locator(plt.MultipleLocator(10))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2))
#ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# Customize the ticks
ax.tick_params(axis='x', which='major', length=10, width=2)
ax.tick_params(axis='x', which='minor', length=5, width=1, color='gray')

# Set labels
ax.set_xlabel('R [kpc]')
ax.set_ylabel('Opt depth')
ax.set_title('Optical depth')

# Show the grid
ax.grid(False, which='both')
plt.legend()

# Display the plot
plt.show()