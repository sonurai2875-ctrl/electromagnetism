"""Electromagnetic wave calculations and simulations."""

import numpy as np
from src.utils import C, MU_0, EPSILON_0, wavelength_from_frequency

class ElectromagneticWave:
    """Represents a plane electromagnetic wave."""
    
    def __init__(self, frequency, amplitude, polarization='linear', direction='z'):
        """Initialize an electromagnetic wave.
        
        Args:
            frequency: Wave frequency in Hz
            amplitude: Electric field amplitude in V/m
            polarization: 'linear' or 'circular'
            direction: Propagation direction ('x', 'y', or 'z')
        """
        self.frequency = frequency
        self.amplitude = amplitude
        self.polarization = polarization
        self.direction = direction
        self.wavelength = wavelength_from_frequency(frequency)
        self.wavenumber = 2 * np.pi / self.wavelength
        self.angular_frequency = 2 * np.pi * frequency
    
    def electric_field(self, position, time):
        """Calculate electric field at position and time.
        
        Args:
            position: Position [x, y, z] in meters
            time: Time in seconds
        
        Returns:
            float: Electric field amplitude
        """
        if self.direction == 'z':
            z = position[2]
            phase = self.wavenumber * z - self.angular_frequency * time
        elif self.direction == 'x':
            x = position[0]
            phase = self.wavenumber * x - self.angular_frequency * time
        else:  # 'y'
            y = position[1]
            phase = self.wavenumber * y - self.angular_frequency * time
        
        return self.amplitude * np.cos(phase)
    
    def magnetic_field(self, position, time):
        """Calculate magnetic field at position and time.
        
        Args:
            position: Position [x, y, z] in meters
            time: Time in seconds
        
        Returns:
            float: Magnetic field amplitude in Tesla
        """
        # In EM wave: B = E/c
        e_field = self.electric_field(position, time)
        return e_field / C
    
    def intensity(self):
        """Calculate average intensity (power per unit area).
        
        Returns:
            float: Intensity in W/m²
        """
        impedance = np.sqrt(MU_0 / EPSILON_0)
        return (self.amplitude ** 2) / (2 * impedance)
    
    def poynting_vector_magnitude(self, position, time):
        """Calculate magnitude of Poynting vector (energy flow).
        
        Args:
            position: Position [x, y, z]
            time: Time in seconds
        
        Returns:
            float: Poynting vector magnitude in W/m²
        """
        e_field = self.electric_field(position, time)
        b_field = self.magnetic_field(position, time)
        impedance = np.sqrt(MU_0 / EPSILON_0)
        return (e_field * b_field) / MU_0
