# lbm-triangle
2d code for flow past a triangle using Lattice Boltzmann

---

## Features

* **Lattice Boltzmann Method:** Implements a D2Q9 (2-dimensional, 9-velocity) Lattice Boltzmann model for fluid simulation.
* **Triangular Obstacle:** Features a static, rotated triangular obstacle within the fluid domain.
* **Vorticity Visualization:** Renders the vorticity of the fluid, highlighting turbulence and flow patterns around the obstacle.
* **Dynamic Visualization:** Updates the simulation in real-time and saves periodic snapshots of the vorticity field.

---


## How it Works

The simulation initializes a fluid domain and sets up a triangular obstacle. It then iteratively performs the following steps:

1.  **Drift (Propagation):** Fluid particles move to their neighboring lattice sites according to their velocities.
2.  **Boundary Conditions:** Implements reflective boundary conditions for the triangular obstacle, meaning particles hitting the obstacle bounce back.
3.  **Calculate Macroscopic Variables:** Computes macroscopic fluid properties like density (`rho`) and velocity (`ux`, `uy`) from the particle distribution functions.
4.  **Collision:** Particles collide locally to relax towards an equilibrium distribution, conserving mass and momentum. This is governed by the relaxation time `tau`.
5.  **Visualization:** Calculates and displays the vorticity of the fluid, providing a visual representation of the flow.


## Output

The simulation will:

* Display a live plot of the vorticity.
* Create a directory named `lbm_figures_triangle/` in the same location as the script.
* Save PNG images of the vorticity plot every 10 timesteps within the `lbm_figures_triangle/` directory. These images can be stitched together to create a video of the simulation.

---


