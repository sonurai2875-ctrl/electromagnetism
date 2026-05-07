"""Utility functions for electromagnetism calculations."""

import numpy as np
from scipy import constants

# Physical constants
EPSILON_0 = constants.epsilon_0  # Permittivity of free space (F/m)
MU_0 = constants.mu_0  # Permeability of free space (H/m)
C = constants.c  # Speed of light (m/s)
E_CHARGE = constants.e  # Elementary charge (C)

def distance(point1, point2):
    """Calculate Euclidean distance between two points.
    
    Args:
        point1: Coordinates as array-like [x1, y1, z1]
        point2: Coordinates as array-like [x2, y2, z2]
    
    Returns:
        float: Distance between points
    """
    return np.linalg.norm(np.array(point2) - np.array(point1))

def normalize_vector(vector):
    """Normalize a vector to unit length.
    
    Args:
        vector: Array-like vector
    
    Returns:
        np.ndarray: Unit vector in same direction
    """
    mag = np.linalg.norm(vector)
    if mag == 0:
        return np.array(vector)
    return np.array(vector) / mag

def coulombs_constant():
    """Get Coulomb's constant k = 1/(4*pi*epsilon_0).
    
    Returns:
        float: Coulomb's constant in SI units
    """
    return 1 / (4 * np.pi * EPSILON_0)

def wavelength_from_frequency(frequency):
    """Calculate wavelength from frequency.
    
    Args:
        frequency: Frequency in Hz
    
    Returns:
        float: Wavelength in meters
    """
    return C / frequency

def frequency_from_wavelength(wavelength):
    """Calculate frequency from wavelength.
    
    Args:
        wavelength: Wavelength in meters
    
    Returns:
        float: Frequency in Hz
    """
    return C / wavelength

def impedance_of_free_space():
    """Get characteristic impedance of free space.
    
    Returns:
        float: Impedance in Ohms (approximately 377 Ω)
    """
    return np.sqrt(MU_0 / EPSILON_0)
