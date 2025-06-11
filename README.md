# lbm-triangle
2d code for flow past a triangle using Lattice Boltzmann
That's a fantastic start! Based on the code you provided, here's a README that you can use.

---

# Lattice Boltzmann Simulation: Flow Past a Triangle

This project simulates fluid flow past a triangular obstacle using the Lattice Boltzmann Method (LBM). The simulation visualizes the fluid's vorticity as it interacts with the obstacle, providing insights into fluid dynamics principles.

---

## Features

* **Lattice Boltzmann Method:** Implements a D2Q9 (2-dimensional, 9-velocity) Lattice Boltzmann model for fluid simulation.
* **Triangular Obstacle:** Features a static, rotated triangular obstacle within the fluid domain.
* **Vorticity Visualization:** Renders the vorticity of the fluid, highlighting turbulence and flow patterns around the obstacle.
* **Dynamic Visualization:** Updates the simulation in real-time and saves periodic snapshots of the vorticity field.

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You'll need the following Python libraries installed:

* `matplotlib`
* `numpy`

You can install them using pip:

```bash
pip install matplotlib numpy
```

### Running the Simulation

1.  **Save the code:** Save the provided Python code as a `.py` file (e.g., `lbm_triangle.py`).
2.  **Execute:** Run the script from your terminal:

    ```bash
    python lbm_triangle.py
    ```

The simulation will start, displaying a real-time visualization of the vorticity. It will also save image files of the simulation at every 10th timestep into a directory named `lbm_figures_triangle`.

---

## How it Works

The simulation initializes a fluid domain and sets up a triangular obstacle. It then iteratively performs the following steps:

1.  **Drift (Propagation):** Fluid particles move to their neighboring lattice sites according to their velocities.
2.  **Boundary Conditions:** Implements reflective boundary conditions for the triangular obstacle, meaning particles hitting the obstacle bounce back.
3.  **Calculate Macroscopic Variables:** Computes macroscopic fluid properties like density (`rho`) and velocity (`ux`, `uy`) from the particle distribution functions.
4.  **Collision:** Particles collide locally to relax towards an equilibrium distribution, conserving mass and momentum. This is governed by the relaxation time `tau`.
5.  **Visualization:** Calculates and displays the vorticity of the fluid, providing a visual representation of the flow.

### Key Parameters

You can modify these parameters at the beginning of the script to alter the simulation behavior:

* `Nx`, `Ny`: Resolution of the simulation grid in the x and y directions.
* `rho0`: Initial average density of the fluid.
* `tau`: Relaxation time, controlling how quickly the fluid approaches equilibrium. A smaller `tau` means faster relaxation and lower viscosity.
* `Nt`: Total number of simulation timesteps.

---

## Output

The simulation will:

* Display a live plot of the vorticity.
* Create a directory named `lbm_figures_triangle/` in the same location as the script.
* Save PNG images of the vorticity plot every 10 timesteps within the `lbm_figures_triangle/` directory. These images can be stitched together to create a video of the simulation.

---

## Contributing

Feel free to explore and modify the code. If you have suggestions for improvements or new features, please consider contributing!

---

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---
