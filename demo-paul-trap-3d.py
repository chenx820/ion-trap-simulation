"""
This script simulates the static electric quadrupole potential in a 3D Paul trap
using numpy and matplotlib.

Author: Chen Huang
Date: 08 Nov 2023
"""

import numpy as np
import matplotlib.pyplot as plt


# Define the function for the electric quadrupole potential
# Here we assume the electrode voltage is 1V and the size of the ion trap is 1m
def potential(x, y, z):
    """
    Function to compute the electric quadrupole potential.

    Parameters:
    x : array_like
        x-coordinates at which to compute the potential.
    y : array_like
        y-coordinates at which to compute the potential.
    z : array_like
        z-coordinates at which to compute the potential.

    Returns:
    array_like
        The computed electric quadrupole potential.
    """
    return 0.5 * (x ** 2 + y ** 2 - 2 * z ** 2)


# Create a three-dimensional grid
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
z = np.linspace(-1, 1, 50)
X, Y, Z = np.meshgrid(x, y, z)

# Compute the potential distribution
V = potential(X, Y, Z)

# Visualize the potential
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c=V.flatten(), alpha=0.6)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')
plt.title('Static Quadrupole Potential of a Paul Trap')
plt.show()
