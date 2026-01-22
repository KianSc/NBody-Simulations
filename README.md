# 3D N-Body Gravity Simulation

<div align="center">
  <img src="nbody_simulation.gif" width="600" />
  <p><em>A simulation of N = 600 bodies interacting under Newtonian gravity, visualized in real-time.</em></p>
</div>

## Overview
This project is a Python-based simulation of the N-Body problem, calculating the gravitational interactions between multiple masses in 3D space. It uses **Matplotlib** for visualization and **NumPy** for vectorized vector calculations.

I created this to explore numerical integration methods and chaotic systems. The simulation allows users to modify initial conditions to observe different orbital configurations.
The gif displayed above was initialized with the following arguments: N = 600, G = 5, rad = 10, dt = 0.025, epsilon = rad.

## Features
* **Real-time 3D Visualization:** Uses `matplotlib.animation` to render orbital paths.
* **Verlet Integration:** Implements the Velocity Verlet algorithm for energy-stable orbit propagation.
* **Vectorized Physics:** Uses NumPy array operations for efficient force calculation $O(N^2)$.
* **Customizable Initial Conditions:** Easy-to-tweak parameters for mass and number of bodies.

##  Usage

### 1. Prerequisites
You will need Python installed along with the following libraries:
```bash
pip install numpy matplotlib
