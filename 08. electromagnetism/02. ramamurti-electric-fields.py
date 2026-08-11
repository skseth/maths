# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# Lecture Notes:
#
#
# - Coulomb's law does not work when charges are moving, because of the delay in propogation of the change in the electric field takes time. 
#
# - Electric field concept is "local" and more general. It is always true, locally, that $F = qE$.
#   
# - In relativity, we break forces into 2 parts - a charge creates a field, the field then propogates and actually impacts other charges. Because no signal can travel faster than light.
#
# I can represented as vector fields. We can also use "lines of force" but these lines lose information on length - however the density of electric field lines tells you the strength of the field at a point.
#
# Lines of force between a - and a + charge - field of a dipole
#
# 2 +vs charges, 2q & -q, 2 elecric plates
#
# Field of a dipole along the axis varies as inverse cube of r at significant distance from dipole. dipole moment p = 2aq
#
# Response to electric field between 2 plates. TV Screens.
#
# Force of an electric field on a dipole ( eg microwave)
#
# torue & pot energy of dipole in a field e
#

# %%
import numpy as np
import matplotlib.pyplot as plt

# 1. Setup the 2D grid mesh
x = np.linspace(-4, 4, 200)
y = np.linspace(-4, 4, 200)
X, Y = np.meshgrid(x, y)

# 2. Define charge properties (positions and magnitudes)
# Dipole: Equal and opposite charges separated by space
q_pos, pos_pos = 1.0, np.array([-1.0, 0.0])  # Positive charge at (-1, 0)
q_neg, pos_neg = -1.0, np.array([1.0, 0.0])  # Negative charge at (1, 0)

# 3. Calculate distances from the grid points to each charge
r_pos_x, r_pos_y = X - pos_pos[0], Y - pos_pos[1]
r_neg_x, r_neg_y = X - pos_neg[0], Y - pos_neg[1]

R_pos_mag = np.hypot(r_pos_x, r_pos_y)
R_neg_mag = np.hypot(r_neg_x, r_neg_y)

# 4. Calculate Electric Field components (E = k * q * r_vector / r^3)
# (Ignoring 1/(4*pi*epsilon_0) constant factor as it scales the vector uniformly)
Ex = q_pos * r_pos_x / R_pos_mag**3 + q_neg * r_neg_x / R_neg_mag**3
Ey = q_pos * r_pos_y / R_pos_mag**3 + q_neg * r_neg_y / R_neg_mag**3

# 5. Plotting the field lines
plt.figure(figsize=(8, 8))

# Draw the streamlines (density controls how many field lines are drawn)
plt.streamplot(X, Y, Ex, Ey, color='gainsboro', linewidth=1.2, density=1.5, arrowstyle='->', arrowsize=1.2)

# Highlight specific field lines with a distinct color for better visual depth
plt.streamplot(X, Y, Ex, Ey, color='royalblue', linewidth=1.5, density=0.6, arrowstyle='->')

# Plot the point charges
plt.scatter(pos_pos[0], pos_pos[1], color='crimson', s=200, label='Positive Charge (+q)', zorder=5)
plt.scatter(pos_neg[0], pos_neg[1], color='darkblue', s=200, label='Negative Charge (-q)', zorder=5)

# Aesthetics
plt.title('Electric Field Lines of a Dipole', fontsize=14, fontweight='bold')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.axhline(0, color='black', alpha=0.2, linestyle='--')
plt.axvline(0, color='black', alpha=0.2, linestyle='--')
plt.legend(loc='upper right')
plt.gca().set_aspect('equal')

plt.show()

