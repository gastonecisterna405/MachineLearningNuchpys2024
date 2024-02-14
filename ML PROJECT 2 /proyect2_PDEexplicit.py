# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:59:50 2024

@author: squev
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
    return np.sin(np.pi * x) * np.exp(-np.pi**2 *K* t)

# Function to perform explicit forward Euler scheme
def explicit_scheme(Nx,K):
    dx = L / Nx
    dt = 0.5 * dx**2  # Stability criterion
    Nt = int(T / dt)
    alpha = K * dt/(dx**2)
    
    # Initialize grid
    x = np.linspace(0, L, Nx+1)
    t = np.linspace(0, T, Nt+1)
    u = np.zeros((Nx+1, Nt+1))

    # Initial condition
    u[:, 0] = np.sin(np.pi * x)

    # Time stepping
    for n in range(0, Nt):
        for i in range(1, Nx):
            #u[i, n+1] = u[i, n] + 0.5 * (u[i+1, n] - 2*u[i, n] + u[i-1, n])
            u[i, n+1] = (alpha*u[i+1, n]) + ((1-2*alpha)*u[i, n]) + (alpha*u[i-1, n])
            
    return x, t, u

# Plot results for different Nx values
for Nx in Nx_values:
    x, t, u = explicit_scheme(Nx,K)

    # Plot at two time points t1 and t2
    t1_index = int(0.1 * len(t))
    t2_index = int(0.9 * len(t))

    plt.figure(figsize=(10, 5))

    plt.subplot(2, 2, 1)
    plt.plot(x, u[:, t1_index], label=f't = {t[t1_index]:.2f}')
    plt.title(f'Solution at t = {t[t1_index]:.2f}')
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(x, u[:, t2_index], label=f't = {t[t2_index]:.2f}')
    plt.title(f'Solution at t = {t[t2_index]:.2f}')
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.legend()
    
    plt.subplot(2, 2, 3)
    plt.plot(x, analytical_solution(x,0.1,K), label=f't = {t[t1_index]:.2f}')
    plt.title(f'Analytical solution at t = {t[t1_index]:.2f}')
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(x, analytical_solution(x,0.9,K), label=f't = {t[t2_index]:.2f}')
    plt.title(f'Analytical solution at t = {t[t2_index]:.2f}')
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
