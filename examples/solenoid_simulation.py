"""Example: Calculate magnetic field in a solenoid."""

from src.magnetic_field import Solenoid
from src.utils import MU_0

def example_solenoid():
    """Calculate and display solenoid magnetic field properties."""
    
    # Create a solenoid with specific parameters
    radius = 0.05  # 5 cm radius
    length = 0.20  # 20 cm length
    num_turns = 500  # 500 turns
    current = 2.0  # 2 Amperes
    
    solenoid = Solenoid(radius, length, num_turns, current)
    
    print("=" * 50)
    print("SOLENOID MAGNETIC FIELD ANALYSIS")
    print("=" * 50)
    print(f"\nSolenoid Parameters:")
    print(f"  Radius: {radius * 100:.1f} cm")
    print(f"  Length: {length * 100:.1f} cm")
    print(f"  Number of turns: {num_turns}")
    print(f"  Current: {current:.2f} A")
    
    # Calculate field inside
    field_inside = solenoid.magnetic_field_inside()
    turns_per_length = num_turns / length
    
    print(f"\nMagnetic Field Inside:")
    print(f"  B = μ₀ × n × I")
    print(f"  B = {MU_0:.3e} × {turns_per_length:.1f} × {current}")
    print(f"  B = {field_inside:.6f} T")
    print(f"  B = {field_inside * 1000:.3f} mT")
    
    # Calculate field outside
    field_outside = solenoid.magnetic_field_outside()
    print(f"\nMagnetic Field Outside (ideal solenoid):")
    print(f"  B ≈ {field_outside} T (approximately zero)")
    
    # Calculate stored energy
    volume = 3.14159 * radius**2 * length
    energy_density = (field_inside**2) / (2 * MU_0)
    total_energy = energy_density * volume
    
    print(f"\nEnergy Storage:")
    print(f"  Volume: {volume:.6f} m³")
    print(f"  Energy density: {energy_density:.3f} J/m³")
    print(f"  Total stored energy: {total_energy:.6f} J")
    print(f"  Total stored energy: {total_energy * 1e6:.3f} μJ")
    
    # Calculate self-inductance
    inductance = (MU_0 * num_turns**2 * 3.14159 * radius**2) / length
    print(f"\nInductance:")
    print(f"  L = μ₀ × N² × A / l")
    print(f"  L = {inductance:.6f} H")
    print(f"  L = {inductance * 1e3:.3f} mH")
    
    # Calculate magnetic flux
    magnetic_flux = field_inside * 3.14159 * radius**2
    print(f"\nMagnetic Flux:")
    print(f"  Φ = B × A")
    print(f"  Φ = {magnetic_flux:.6f} Wb")
    print(f"  Total flux linkage (Λ = N × Φ): {num_turns * magnetic_flux:.6f} Wb")
    
    print("\n" + "=" * 50)

if __name__ == '__main__':
    example_solenoid()
