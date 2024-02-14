# -*- coding: utf-8 -*-
"""
This script uses the forward Euler algorithm to solve the diffusion equation 
with Neumann boundary conditions.

Two different spatial discretizations will be employed. 
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0  # Length of the rod
T = 1  # Total simulation time
Nx_values = [10, 100]  # Grid points for different Delta x
K = 0.1

# Analytical solution
def analytical_solution(x, t, K):
    return np.cos(np.pi * x) * np.exp(-np.pi**2 *K* t)

# Function to perform explicit forward Euler scheme
def explicit_scheme(Nx,K):
    dx = L / Nx
    print(dx)
    dt = 0.5 * dx**2  # Stability criterion
    print(dt)
    Nt = int(T / dt)
    alpha = dt/(dx**2)
    print(alpha)
    
    # Initialize grid
    x = np.linspace(0, L, Nx+1)
    t = np.linspace(0, T, Nt+1)
    u = np.zeros((Nx+1, Nt+1))

    # Initial condition
    u[:, 0] = np.cos(np.pi * x)
    
    # Fill borders separately
    
    # Time stepping
    for n in range(0, Nt):
        for i in range(0, Nx):
            #u[i, n+1] = u[i, n] + 0.5 * (u[i+1, n] - 2*u[i, n] + u[i-1, n])
            u[i, n+1] = (K*alpha*u[i+1, n]) + ((1-2*alpha*K)*u[i, n]) + (K*alpha*u[i-1, n])
            
            # Neumann boundary conditions
            u[0, n+1] = u[1, n+1]  # Neumann condition at x = 0
            u[Nx, n+1] = u[Nx-1, n+1]  # Neumann condition at x = L
    return x, t, u

# Plot results for different Nx values
for Nx in Nx_values:

    x, t, u = explicit_scheme(Nx,K)
    
    # Plot at two time points t1 and t2
    t1_index = int(0.1 * len(t))
    t2_index = int(0.9 * len(t))
    
    plt.figure() #figsize=(10, 10)
    
    plt.subplot()
    plt.plot(x, analytical_solution(x,0.1,K), label='Analytical')
    plt.plot(x, u[:, 1], label='Numerical')
    plt.title(f'Solution at t = {t[t1_index]:.2f}')
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.legend()
    
    plt.figure() #figsize=(10, 10)
    plt.subplot()
    plt.plot(x, analytical_solution(x,0.9,K), label='Analytical')
    plt.plot(x, u[:, t2_index], label='Numerical')
    plt.title(f'Solution at t = {t[t2_index]:.2f}')
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.legend()
    
    
    plt.subplots_adjust(hspace=0.3)
    
    # Create a contour plot
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.contourf(x, t, u.T, cmap='coolwarm')
    plt.colorbar(label='u(x, t)')
    plt.title('Contour Plot of u(x, t)')
    plt.xlabel('x')
    plt.ylabel('t')
    
    
    plt.tight_layout()
    plt.show()
