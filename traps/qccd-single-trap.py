"""
Simulate the electric potential field of a Quantum Charge-Coupled Device (QCCD) and visualize it in 3D and cross-sectional plots.

Author: Chen Huang
Date: November 11, 2023
"""

import numpy as np
import matplotlib.pyplot as plt


def single_trap_potential(x, y, z, dc_position):
    """
    Simulate the electric potential field of a linear ion trap.

    Parameters:
        x (numpy array): x-coordinate array
        y (numpy array): y-coordinate array
        z (numpy array): z-coordinate array
        dc_position (float): Position of dc electrode

    Returns:
        numpy array: Electric potential field values array
    """

    # Calculate electric potential field values array based on the linear ion trap model
    # The potential is composed of RF and DC components
    potential_rf = 5 * abs(x * z)  # RF potential
    potential_dc = -0.1 * (1 / np.sqrt((x - dc_position) ** 2 + z ** 2) + 1 / np.sqrt(
        (x + dc_position) ** 2 + z ** 2))  # DC potential

    return potential_rf + potential_dc  # Total potential is the sum of RF and DC components


dc_position = 1.1  # Position of dc electrode

# Generate coordinate arrays for x, y, and z directions
x_values = np.linspace(-1, 1, 100)
y_values = np.linspace(-1, 1, 100)
z_values = np.linspace(-1, 1, 100)
x, y, z = np.meshgrid(x_values, y_values, z_values)

# Calculate electric potential field values array for a linear ion trap
potential_values = single_trap_potential(x, y, z, dc_position)

# Set a wider figure size
fig = plt.figure(figsize=(14, 12))

# Plot the 3D electric potential field (scatter plot)
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
scatter1 = ax1.scatter3D(x, y, z, c=potential_values, cmap='coolwarm', vmin=potential_values.min(),
                         vmax=potential_values.max(), label='Potential Energy')
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

# Plot the cross-section in the x-z plane at y=0
ax2 = fig.add_subplot(2, 2, 2)
contour2 = ax2.contourf(x_values, z_values, potential_values[50, :, :].transpose(), cmap='coolwarm',
                        vmin=potential_values.min(), vmax=potential_values.max())
ax2.set_xlabel('$X$ Position')
ax2.set_ylabel('$Z$ Position')
ax2.set_title('Cross-Section at $y=0$')  # Corrected the title
# Add ticks to the axes
ax2.set_xticks(np.linspace(-1, 1, 5))
ax2.set_yticks(np.linspace(-1, 1, 5))
# Plot the electric field lines in the x-z plane at y=0

# Plot the cross-section in the y-z plane at x=0
ax3 = fig.add_subplot(2, 2, 3)
contour3 = ax3.contourf(z_values, y_values, potential_values[:, 50, :], cmap='coolwarm',
                        vmin=potential_values.min(), vmax=potential_values.max())
ax3.set_xlabel('$Z$ Position')
ax3.set_ylabel('$Y$ Position')
ax3.set_title('Cross-Section at $x=0$')  # Corrected the title
# Add ticks to the axes
ax3.set_xticks(np.linspace(-1, 1, 5))
ax3.set_yticks(np.linspace(-1, 1, 5))

# Plot the cross-section in the x-y plane at z=0
ax4 = fig.add_subplot(2, 2, 4)
contour4 = ax4.contourf(x_values, y_values, potential_values[:, :, 50], cmap='coolwarm',
                        vmin=potential_values.min(), vmax=potential_values.max())
ax4.set_xlabel('$X$ Position')
ax4.set_ylabel('$Y$ Position')
ax4.set_title('Cross-Section at $z=0$')  # Corrected the title
# Add ticks to the axes
ax4.set_xticks(np.linspace(-1, 1, 5))
ax4.set_yticks(np.linspace(-1, 1, 5))

plt.show()
