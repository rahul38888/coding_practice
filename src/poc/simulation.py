import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
M = 1.0  # Mass of the black hole
a = 0.9  # Spin parameter (0 to 1)

# Key radii
r_s = 2 * M
r_h_plus = M + np.sqrt(M ** 2 - a ** 2)  # Outer event horizon
r_erg_plus = M + np.sqrt(
    M ** 2 - a ** 2 * np.cos(0) ** 2)  # Ergosphere at equator

# Setup figure
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_aspect('equal')
ax.set_facecolor('black')

# Basic black hole features
theta = np.linspace(0, 2 * np.pi, 100)
eh_x = r_h_plus * np.cos(theta)
eh_y = r_h_plus * np.sin(theta)
erg_x = r_erg_plus * np.cos(theta)
erg_y = r_erg_plus * np.sin(theta)

event_horizon, = ax.plot(eh_x, eh_y, 'r-', label='Event Horizon')
ergosphere, = ax.plot(erg_x, erg_y, 'b-', alpha=0.3, label='Ergosphere')

# Accretion disk
disk_r = np.linspace(r_h_plus, 3 * r_h_plus, 100)
disk_theta = np.linspace(0, 2 * np.pi, 100)
disk_R, disk_Theta = np.meshgrid(disk_r, disk_theta)
disk_x = disk_R * np.cos(disk_Theta)
disk_y = disk_R * np.sin(disk_Theta)
accretion = ax.contourf(disk_x, disk_y, disk_R, levels=20, cmap='hot',
                        alpha=0.2)


# Light rays (simplified gravitational lensing)
def bend_light(r, theta, impact_param):
    deflection = 4 * M / (r * impact_param)
    x = r * np.cos(theta + deflection)
    y = r * np.sin(theta + deflection)
    return x, y


n_rays = 6
ray_r = np.linspace(1.5 * r_h_plus, 10, 50)
ray_angles = np.linspace(0, 2 * np.pi, n_rays, endpoint=False)

# Particles
n_particles = 5
particle_r = np.linspace(1.5 * r_h_plus, 4 * r_h_plus, n_particles)
particle_theta = np.random.uniform(0, 2 * np.pi, n_particles)
particles = ax.scatter([], [], c='white', s=20, label='Particles')


# Animation function
def update(frame):
    rotation = frame * 0.1

    # Update ergosphere
    erg_x_rot = r_erg_plus * np.cos(theta + rotation)
    erg_y_rot = r_erg_plus * np.sin(theta + rotation)
    ergosphere.set_data(erg_x_rot, erg_y_rot)

    # Remove old light rays (keep only accretion disk from collections)
    while len(ax.collections) > 1:  # First collection is accretion disk
        ax.collections[-1].remove()

    # Draw bent light rays with color shift
    for angle in ray_angles:
        impact_param = np.abs(2 + np.sin(angle))
        ray_x, ray_y = bend_light(ray_r, angle, impact_param)
        velocity_factor = np.sin(rotation + angle)
        if velocity_factor > 0:
            color = (0.2, 0.2, 1.0 - velocity_factor)  # Blueshift
        else:
            color = (1.0 + velocity_factor, 0.2, 0.2)  # Redshift
        ax.plot(ray_x, ray_y, color=color, alpha=0.5, linewidth=1)

    # Update particle positions
    omega = a / (r_h_plus ** 1.5 + a ** 2)
    particle_theta_new = particle_theta + omega * frame * 0.1
    particle_x = particle_r * np.cos(particle_theta_new)
    particle_y = particle_r * np.sin(particle_theta_new)
    particles.set_offsets(np.c_[particle_x, particle_y])

    return event_horizon, ergosphere, particles


# Plot setup
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title(f'Kerr Black Hole - Observer View (a/M = {a})', color='white')
ax.legend(loc='upper right')
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])

# Animation
anim = FuncAnimation(fig, update, frames=100, interval=50, blit=False)

plt.show()
