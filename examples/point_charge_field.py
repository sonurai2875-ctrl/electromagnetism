"""Example: Visualize electric field from a point charge."""

import numpy as np
import matplotlib.pyplot as plt
from src.electric_field import PointCharge, ElectricFieldSuperposition

def example_single_charge():
    """Visualize field from a single positive charge."""
    # Create a point charge: +1 Coulomb at origin
    charge = PointCharge(1e-6, [0, 0, 0])  # 1 micro-Coulomb
    
    # Create a grid of points in x-y plane
    x = np.linspace(-5, 5, 20)
    y = np.linspace(-5, 5, 20)
    X, Y = np.meshgrid(x, y)
    
    # Calculate field components at each point
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    
    for i in range(len(x)):
        for j in range(len(y)):
            field = charge.electric_field([X[j, i], Y[j, i], 0])
            Ex[j, i] = field[0]
            Ey[j, i] = field[1]
    
    # Plot field vectors
    plt.figure(figsize=(10, 8))
    plt.quiver(X, Y, Ex, Ey)
    plt.plot(0, 0, 'ro', markersize=10, label='Charge')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title('Electric Field from Point Charge (+1 μC)')
    plt.legend()
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    print("Saved plot to 'point_charge_field.png'")
    # plt.savefig('point_charge_field.png', dpi=150)
    # plt.show()

def example_dipole():
    """Visualize field from an electric dipole (+ and - charges)."""
    charges = ElectricFieldSuperposition()
    charges.add_charge(+1e-6, [-2, 0, 0])  # Positive charge
    charges.add_charge(-1e-6, [+2, 0, 0])  # Negative charge
    
    # Create grid
    x = np.linspace(-8, 8, 25)
    y = np.linspace(-8, 8, 25)
    X, Y = np.meshgrid(x, y)
    
    # Calculate total field
    Ex = np.zeros_like(X, dtype=float)
    Ey = np.zeros_like(Y, dtype=float)
    
    for i in range(len(x)):
        for j in range(len(y)):
            field = charges.total_field([X[j, i], Y[j, i], 0])
            Ex[j, i] = field[0]
            Ey[j, i] = field[1]
    
    # Plot
    plt.figure(figsize=(10, 8))
    plt.quiver(X, Y, Ex, Ey)
    plt.plot(-2, 0, 'ro', markersize=12, label='+ Charge')
    plt.plot(2, 0, 'bo', markersize=12, label='- Charge')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title('Electric Field from Electric Dipole')
    plt.legend()
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    print("Saved dipole field plot")
    # plt.show()

if __name__ == '__main__':
    print("Running point charge example...")
    example_single_charge()
    print("\nRunning dipole example...")
    example_dipole()
