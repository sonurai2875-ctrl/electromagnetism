"""Example: Simulate electromagnetic wave propagation."""

import numpy as np
import matplotlib.pyplot as plt
from src.electromagnetic_wave import ElectromagneticWave
from src.utils import C, wavelength_from_frequency, frequency_from_wavelength

def example_em_wave_properties():
    """Display properties of an electromagnetic wave."""
    
    # Create a visible light wave (middle of visible spectrum)
    frequency = 5e14  # 500 THz (green light)
    amplitude = 1000  # V/m
    
    wave = ElectromagneticWave(frequency, amplitude)
    
    print("=" * 60)
    print("ELECTROMAGNETIC WAVE PROPERTIES")
    print("=" * 60)
    print(f"\nWave Parameters:")
    print(f"  Frequency: {frequency:.2e} Hz ({frequency/1e12:.0f} THz)")
    print(f"  Wavelength: {wave.wavelength:.2e} m ({wave.wavelength*1e9:.0f} nm)")
    print(f"  Speed: {C:.2e} m/s")
    print(f"  Amplitude (E-field): {amplitude:.0f} V/m")
    
    print(f"\nWave Characteristics:")
    print(f"  Wavenumber (k): {wave.wavenumber:.2e} rad/m")
    print(f"  Angular frequency (ω): {wave.angular_frequency:.2e} rad/s")
    print(f"  Period: {1/frequency:.2e} s ({1/frequency*1e15:.2f} fs)")
    
    print(f"\nEnergy Properties:")
    intensity = wave.intensity()
    print(f"  Average Intensity: {intensity:.2e} W/m²")
    print(f"  Average Intensity: {intensity:.0f} W/m²")
    
    # Different types of EM radiation
    print(f"\n" + "=" * 60)
    print("ELECTROMAGNETIC SPECTRUM EXAMPLES")
    print("=" * 60)
    
    spectrum = [
        (1e3, "Radio waves"),
        (1e6, "Microwaves"),
        (5e14, "Visible light (green)"),
        (1e16, "UV light"),
        (1e20, "Gamma rays"),
    ]
    
    for freq, name in spectrum:
        wavelength = wavelength_from_frequency(freq)
        wave_test = ElectromagneticWave(freq, 1000)
        intensity_test = wave_test.intensity()
        print(f"\n{name}:")
        print(f"  Frequency: {freq:.2e} Hz")
        print(f"  Wavelength: {wavelength:.2e} m")
        print(f"  Intensity (1000 V/m): {intensity_test:.2e} W/m²")

def example_em_wave_snapshot():
    """Visualize a snapshot of EM wave in space."""
    
    # Radio wave for visualization
    frequency = 1e9  # 1 GHz radio wave
    amplitude = 1000
    
    wave = ElectromagneticWave(frequency, amplitude, direction='z')
    
    # Position along z-axis
    z = np.linspace(0, 2*wave.wavelength, 1000)
    
    # Electric field at t=0
    E_field = [wave.electric_field([0, 0, zi], 0) for zi in z]
    
    # Magnetic field at t=0
    B_field = [wave.magnetic_field([0, 0, zi], 0) for zi in z]
    
    print(f"\n" + "=" * 60)
    print("Plotting EM wave snapshot at t=0...")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Electric field plot
    ax1.plot(z*1e9, E_field, 'b-', linewidth=2, label='E-field')
    ax1.set_ylabel('Electric Field (V/m)', fontsize=12)
    ax1.set_title(f'EM Wave Snapshot at t=0 (f={frequency/1e9:.1f} GHz)', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Magnetic field plot
    ax2.plot(z*1e9, np.array(B_field)*1e6, 'r-', linewidth=2, label='B-field')
    ax2.set_xlabel('Position (nm)', fontsize=12)
    ax2.set_ylabel('Magnetic Field (μT)', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    print("EM wave visualization ready")
    # plt.show()

if __name__ == '__main__':
    example_em_wave_properties()
    example_em_wave_snapshot()
