"""Unit tests for electromagnetism modules."""

import numpy as np
import sys
sys.path.insert(0, '..')

from src.electric_field import PointCharge, ElectricFieldSuperposition
from src.magnetic_field import StraightWire, Solenoid
from src.electromagnetic_wave import ElectromagneticWave
from src.utils import (
    distance, normalize_vector, coulombs_constant,
    wavelength_from_frequency, frequency_from_wavelength,
    impedance_of_free_space, C
)

def test_distance():
    """Test distance calculation."""
    p1 = [0, 0, 0]
    p2 = [3, 4, 0]
    assert abs(distance(p1, p2) - 5.0) < 1e-10, "Distance calculation failed"
    print("✓ Distance calculation test passed")

def test_normalize_vector():
    """Test vector normalization."""
    v = [3, 4, 0]
    normalized = normalize_vector(v)
    magnitude = np.linalg.norm(normalized)
    assert abs(magnitude - 1.0) < 1e-10, "Vector normalization failed"
    print("✓ Vector normalization test passed")

def test_coulombs_constant():
    """Test Coulomb's constant."""
    k = coulombs_constant()
    assert 8.9e9 < k < 9e9, "Coulomb's constant out of range"
    print(f"✓ Coulomb's constant test passed (k ≈ {k:.2e})")

def test_wavelength_frequency_conversion():
    """Test wavelength-frequency conversion."""
    freq = 5e14  # 500 THz (green light)
    wavelength = wavelength_from_frequency(freq)
    freq_back = frequency_from_wavelength(wavelength)
    assert abs(freq - freq_back) / freq < 1e-10, "Conversion failed"
    print(f"✓ Wavelength-frequency conversion test passed")
    print(f"  {freq:.2e} Hz → {wavelength*1e9:.0f} nm → {freq_back:.2e} Hz")

def test_point_charge_field():
    """Test point charge electric field."""
    charge = PointCharge(1e-6, [0, 0, 0])
    field_at_distance = charge.electric_field([1, 0, 0])
    field_magnitude = np.linalg.norm(field_at_distance)
    
    k = coulombs_constant()
    expected_magnitude = k * 1e-6 / 1.0
    
    assert abs(field_magnitude - expected_magnitude) / expected_magnitude < 1e-10
    print(f"✓ Point charge field test passed")
    print(f"  Field magnitude at 1m: {field_magnitude:.0f} V/m")

def test_solenoid_field():
    """Test solenoid magnetic field."""
    solenoid = Solenoid(0.05, 0.2, 500, 2.0)
    field = solenoid.magnetic_field_inside()
    
    # B should be positive and reasonable
    assert field > 0, "Magnetic field should be positive"
    assert field < 0.1, "Magnetic field seems unreasonably large"
    print(f"✓ Solenoid field test passed")
    print(f"  Field inside: {field*1000:.3f} mT")

def test_em_wave_velocity():
    """Test that EM wave properties are consistent with c."""
    freq = 5e14
    wave = ElectromagneticWave(freq, 1000)
    
    velocity = wave.frequency * wave.wavelength
    assert abs(velocity - C) / C < 1e-10, "Wave velocity doesn't equal c"
    print(f"✓ EM wave velocity test passed")
    print(f"  v = f × λ = {velocity:.2e} m/s (should equal c)")

def test_impedance_of_free_space():
    """Test characteristic impedance of free space."""
    Z = impedance_of_free_space()
    assert 370 < Z < 380, "Impedance out of expected range"
    print(f"✓ Impedance of free space test passed")
    print(f"  Z₀ ≈ {Z:.1f} Ω")

def run_all_tests():
    """Run all unit tests."""
    print("\n" + "=" * 60)
    print("RUNNING ELECTROMAGNETISM MODULE TESTS")
    print("=" * 60 + "\n")
    
    tests = [
        test_distance,
        test_normalize_vector,
        test_coulombs_constant,
        test_wavelength_frequency_conversion,
        test_point_charge_field,
        test_solenoid_field,
        test_em_wave_velocity,
        test_impedance_of_free_space,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {str(e)}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"TESTS COMPLETED: {passed} passed, {failed} failed")
    print("=" * 60 + "\n")

if __name__ == '__main__':
    run_all_tests()
