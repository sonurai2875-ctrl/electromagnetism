"""Electric field calculations and implementations."""

import numpy as np
from src.utils import distance, normalize_vector, coulombs_constant

class PointCharge:
    """Represents a point charge and its electric field."""
    
    def __init__(self, charge, position):
        """Initialize a point charge.
        
        Args:
            charge: Charge magnitude in Coulombs
            position: Position as [x, y, z] array
        """
        self.charge = charge
        self.position = np.array(position)
    
    def electric_field(self, point):
        """Calculate electric field at a given point.
        
        Args:
            point: Point where field is calculated [x, y, z]
        
        Returns:
            np.ndarray: Electric field vector [Ex, Ey, Ez]
        """
        point = np.array(point)
        r_vector = point - self.position
        r_magnitude = np.linalg.norm(r_vector)
        
        if r_magnitude < 1e-10:
            return np.array([0, 0, 0])
        
        k = coulombs_constant()
        field_magnitude = k * self.charge / (r_magnitude ** 2)
        field_vector = field_magnitude * normalize_vector(r_vector)
        
        return field_vector
    
    def potential(self, point):
        """Calculate electric potential at a given point.
        
        Args:
            point: Point where potential is calculated [x, y, z]
        
        Returns:
            float: Electric potential in Volts
        """
        r = distance(point, self.position)
        if r < 1e-10:
            return np.inf
        k = coulombs_constant()
        return k * self.charge / r

class ElectricFieldSuperposition:
    """Calculate combined electric field from multiple charges."""
    
    def __init__(self):
        """Initialize with empty charge list."""
        self.charges = []
    
    def add_charge(self, charge, position):
        """Add a point charge to the system.
        
        Args:
            charge: Charge in Coulombs
            position: Position as [x, y, z]
        """
        self.charges.append(PointCharge(charge, position))
    
    def total_field(self, point):
        """Calculate total electric field at a point.
        
        Args:
            point: Point where field is calculated [x, y, z]
        
        Returns:
            np.ndarray: Total electric field vector
        """
        total = np.array([0.0, 0.0, 0.0])
        for charge in self.charges:
            total += charge.electric_field(point)
        return total
    
    def total_potential(self, point):
        """Calculate total electric potential at a point.
        
        Args:
            point: Point where potential is calculated [x, y, z]
        
        Returns:
            float: Total potential in Volts
        """
        total = 0.0
        for charge in self.charges:
            total += charge.potential(point)
        return total
