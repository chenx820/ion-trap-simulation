"""
Simulate the electric potential field of a Paul trap and visualize it in 3D and cross-sectional plots.

Author: Chen Huang
Date: November 10, 2023
"""

import numpy as np
import matplotlib.pyplot as plt


def trap_potential(x, y, z, trap_param):
    """
    Simulate the electric potential field of a linear ion trap.

    Parameters:
        x (numpy array): x-coordinate array
        y (numpy array): y-coordinate array
        z (numpy array): z-coordinate array
        trap_param (numpy array): the parameters of potential

    Returns:
        numpy array: Electric potential field values array
    """
    # Extract parameters for the quadratic potential terms along each axis
    a, b, c = trap_param

    # Calculate electric potential field values array based on the linear ion trap model
    potential = a * x ** 2 + b * y ** 2 + c * z ** 2

    return potential


# Define simulation parameters for different ion traps
# According to the Laplace equation, the sum of parameters equals to zero
paul_trap = [1, 1, -2]  # Parameters for a Paul trap
linear_trap = [1, 0, -1]  # Parameters for a linear ion trap

# Generate coordinate arrays
x_values = np.linspace(-1, 1, 100)
y_values = np.linspace(-1, 1, 100)
z_values = np.linspace(-1, 1, 100)
x, y, z = np.meshgrid(x_values, y_values, z_values)

# Calculate electric potential field values array for a linear ion trap
potential_values = trap_potential(x, y, z, paul_trap)

# Set a wider figure size
fig = plt.figure(figsize=(14, 12))

# Plot the 3D electric potential field (scatter plot)
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
scatter1 = ax1.scatter3D(x, y, z, c=potential_values, cmap='coolwarm', label='Potential Energy')
ax1.set_xlabel('$X$ Position')
ax1.set_ylabel('$Y$ Position')
ax1.set_zlabel('$Z$ Position')
ax1.set_title('Ion Trap Potential Distribution')
# Add ticks to the axes
ax1.set_xticks(np.linspace(-1, 1, 5))
ax1.set_yticks(np.linspace(-1, 1, 5))
ax1.set_zticks(np.linspace(-1, 1, 5))
# Create a single colorbar for all subplots
cbar = plt.colorbar(scatter1, ax=ax1, label='Potential Energy', location='bottom')

# Plot the cross-section in the x-y plane at z=0
ax2 = fig.add_subplot(2, 2, 4)
contour2 = ax2.contourf(x_values, y_values, potential_values[:, :, 50], cmap='coolwarm',
                        vmin=potential_values.min(), vmax=potential_values.max())
ax2.set_xlabel('$X$ Position')
ax2.set_ylabel('$Y$ Position')
ax2.set_title('Cross-Section at $z=0$')
# Add ticks to the axes
ax2.set_xticks(np.linspace(-1, 1, 5))
ax2.set_yticks(np.linspace(-1, 1, 5))

# Plot the cross-section in the y-z plane at x=0
ax3 = fig.add_subplot(2, 2, 3)
contour3 = ax3.contourf(z_values, y_values, potential_values[:, 50, :], cmap='coolwarm',
                        vmin=potential_values.min(), vmax=potential_values.max())
ax3.set_xlabel('$Z$ Position')
ax3.set_ylabel('$Y$ Position')
ax3.set_title('Cross-Section at $x=0$')
# Add ticks to the axes
ax3.set_xticks(np.linspace(-1, 1, 5))
ax3.set_yticks(np.linspace(-1, 1, 5))

# Plot the cross-section in the x-z plane at y=0
ax4 = fig.add_subplot(2, 2, 2)
contour4 = ax4.contourf(x_values, z_values, potential_values[50, :, :].transpose(), cmap='coolwarm',
                        vmin=potential_values.min(), vmax=potential_values.max())
ax4.set_xlabel('$X$ Position')
ax4.set_ylabel('$Z$ Position')
ax4.set_title('Cross-Section at $y=0$')
# Add ticks to the axes
ax4.set_xticks(np.linspace(-1, 1, 5))
ax4.set_yticks(np.linspace(-1, 1, 5))

plt.show()
