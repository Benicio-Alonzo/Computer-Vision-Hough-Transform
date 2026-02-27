"""
For points (10, 10), (20, 20), and (30, 30) in the image space, plot the corresponding
sinusoid waves in the Hough space, and visualize how their intersection point defines
the line
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

points = [(10, 5), (15, 10), (20, 15)]

# Initiate plot
fig, ax = plt.subplots(figsize=(5, 5))

""" COMPLETE """
theta = np.linspace(0, 2*np.pi, 1000)
for x0, y0 in points:
    # Calculate rho for each theta using the normal form equation:
    rho = x0 * np.cos(theta) + y0 * np.sin(theta)
    ax.plot(theta, rho, label=f'Point ({x0},{y0})')

ax.grid(True)
ax.set_xlabel('θ (radians)')
ax.set_ylabel('ρ (distance)')

# Set major ticks every 0.25π (e.g., 0, 0.25π, 0.5π, 0.75π, ...)
ax.xaxis.set_major_locator(tck.MultipleLocator(base=0.25 * np.pi))
ax.yaxis.set_major_locator(tck.MultipleLocator(base=5))

# Format tick labels to display the pi symbol (π)
ax.xaxis.set_major_formatter(tck.FuncFormatter(
    lambda val, pos: '{:.3g}$\pi$'.format(val / np.pi) if val != 0 else '0'
))

""" COMPLETE """
intersection_theta = 0.75 * np.pi
intersection_rho = points[0][0] * np.cos(intersection_theta) + points[0][1] * np.sin(intersection_theta)
ax.plot(intersection_theta, intersection_rho, 'ro', 
         label=r'Intersection point')

plt.legend()
plt.savefig('q2_1_plot.png', bbox_inches='tight')
print("Success: Plot saved as q2_1_plot.png")