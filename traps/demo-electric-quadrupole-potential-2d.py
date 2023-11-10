"""This script simulates the electric quadrupole potential in a 2D ion trapusing numpy and matplotlib.Author: Chen HuangDate: November 08, 2023"""import numpy as npimport matplotlib.pyplot as pltdef potential(x, y):    """    Function to compute the electric quadrupole potential.    Parameters:    x : array_like        x-coordinates at which to compute the potential.    y : array_like        y-coordinates at which to compute the potential.    Returns:    array_like        The computed electric quadrupole potential.    """    return x ** 2 - y ** 2# Create a two-dimensional gridx = np.linspace(-1, 1, 100)y = np.linspace(-1, 1, 100)X, Y = np.meshgrid(x, y)# Compute the potential distributionV = potential(X, Y)# Visualize the potential using matplotlibplt.contourf(X, Y, V, levels=50, cmap='RdBu')plt.colorbar(label='Potential (V)')plt.xlabel('$x$ (m)')plt.ylabel('$y$ (m)')plt.title('Electric Quadrupole Potential')plt.show()