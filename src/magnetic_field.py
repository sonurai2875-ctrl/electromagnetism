"""Magnetic field calculations and implementations."""

import numpy as np
from src.utils import distance, normalize_vector, MU_0

class StraightWire:
    """Represents a straight current-carrying wire and its magnetic field."""
    
    def __init__(self, current, start_point, end_point):
        """Initialize a straight wire.
        
        Args:
            current: Current in Amperes
            start_point: Wire start position [x, y, z]
            end_point: Wire end position [x, y, z]
        """
        self.current = current
        self.start_point = np.array(start_point)
        self.end_point = np.array(end_point)
        self.wire_vector = self.end_point - self.start_point
        self.wire_length = np.linalg.norm(self.wire_vector)
    
    def magnetic_field(self, point):
        """Calculate magnetic field at a point using Biot-Savart law.
        
        Args:
            point: Point where field is calculated [x, y, z]
        
        Returns:
            np.ndarray: Magnetic field vector [Bx, By, Bz]
        """
        point = np.array(point)
        
        # Vector from wire start to evaluation point
        r = point - self.start_point
        
        # Distance from point to wire (perpendicular)
        cross_product = np.cross(self.wire_vector, r)
        d = np.linalg.norm(cross_product) / self.wire_length
        
        if d < 1e-10:
            return np.array([0.0, 0.0, 0.0])
        
        # Unit vector along wire
        wire_unit = normalize_vector(self.wire_vector)
        
        # Components for field calculation
        cos_theta1 = np.dot(r, wire_unit) / np.linalg.norm(r)
        cos_theta2 = np.dot(-(point - self.end_point), wire_unit) / np.linalg.norm(point - self.end_point)
        
        # Magnetic field magnitude using Ampère-Biot-Savart approximation
        field_magnitude = (MU_0 * self.current / (2 * np.pi * d)) * (cos_theta1 + cos_theta2)
        
        # Direction: perpendicular to both wire and point
        direction = normalize_vector(np.cross(wire_unit, normalize_vector(r)))
        
        return field_magnitude * direction

class Solenoid:
    """Represents a solenoid and its magnetic field."""
    
    def __init__(self, radius, length, num_turns, current):
        """Initialize a solenoid.
        
        Args:
            radius: Radius in meters
            length: Length in meters
            num_turns: Number of turns
            current: Current in Amperes
        """
        self.radius = radius
        self.length = length
        self.num_turns = num_turns
        self.current = current
        self.center = np.array([0, 0, 0])
    
    def magnetic_field_inside(self):
        """Calculate magnetic field inside ideal solenoid.
        
        Returns:
            float: Magnetic field magnitude in Tesla
        """
        return MU_0 * (self.num_turns / self.length) * self.current
    
    def magnetic_field_outside(self):
        """Calculate magnetic field outside ideal solenoid.
        
        Returns:
            float: Approximately zero for ideal solenoid
        """
        return 0.0
