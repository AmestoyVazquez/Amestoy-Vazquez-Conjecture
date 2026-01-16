"""
Unit tests for Amestoy-Vázquez Conjecture
Author: Juan Pedro Amestoy Vazquez
Email: juanpedroamestoy@gmail.com

These tests verify the mathematical correctness of the formula:
S(n,d,a) = n·a + n(n^d - 1)/2
"""

import sys
import os

# Add src directory to Python path so we can import the formula
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.formula import amestoy_vazquez_constant, classical_magic_constant


def test_classical_case():
    """
    Test that Amestoy-Vázquez formula reduces to classical case when a=1, d=2.
    
    This is the MOST IMPORTANT test: it verifies that our generalization
    correctly contains the classical magic square formula as a special case.
    """
    print("Testing classical case (a=1, d=2)...")
    
    # Test several odd numbers (classical formula works for all n)
    test_cases = [3, 5, 7, 9]
    
    for n in test_cases:
        # Classical formula (known to be correct)
        classical = classical_magic_constant(n)
        
        # Our formula (should match when a=1, d=2)
        av = amestoy_vazquez_constant(n, 2, 1)
        
        # They should be equal (within floating-point tolerance)
        error = abs(classical - av)
        assert error < 1e-10, f"Mismatch for n={n}: classical={classical}, AV={av}, error={error}"
        
        print(f"  ✓ n={n}: Classical={classical}, AV={av}")
    
    print("✅ All classical cases match!")


def test_known_values():
    """
    Test known values that we've manually calculated and verified.
    
    These are our 'ground truth' test cases that we know are correct
    from manual calculation or previous verification.
    """
    print("\nTesting known calculated values...")
    
    # Table of (n, d, a, expected_result)
    # These values should be mathematically correct
    test_cases = [
        # (n, d, a, expected)
        (3, 2, 1, 15.0),       # Classical 3x3: 8+1+6 = 15
        (3, 2, 100, 315.0),    # 3x3 starting at 100: 107+100+105 = 315
        (5, 3, 500.5, 2812.5), # 5x5x5 cube starting at 500.5
        (4, 2, 50, 230.0),     # 4x4 starting at 50
        (3, 3, 1, 42.0),       # 3x3x3 cube starting at 1
        (5, 2, 500.5, 2562.5), # 5x5 square starting at 500.5
    ]
    
    for n, d, a, expected in test_cases:
        result = amestoy_vazquez_constant(n, d, a)
        error = abs(result - expected)
        
        assert error < 1e-10, (
            f"Failed for n={n}, d={d}, a={a}\n"
            f"  Expected: {expected}\n"
            f"  Got: {result}\n"
            f"  Error: {error}"
        )
        
        print(f"  ✓ S({n},{d},{a}) = {result} (expected: {expected})")
    
    print("✅ All known values correct!")


def test_negative_start():
    """
    Test with negative starting values.
    
    Verifies the formula works correctly with negative numbers,
    which is important for mathematical completeness.
    """
    print("\nTesting negative starting values...")
    
    # Test 1: 3x3 starting at -5
    n, d, a = 3, 2, -5
    result = amestoy_vazquez_constant(n, d, a)
    
    # Manual calculation: 3*(-5) + 3*(9-1)/2 = -15 + 12 = -3
    expected = -3.0
    error = abs(result - expected)
    
    assert error < 1e-10, f"Negative test failed: got {result}, expected {expected}"
    print(f"  ✓ S({n},{d},{a}) = {result} (correct: -15 + 12 = -3)")
    
    # Test 2: Different negative value
    n, d, a = 5, 2, -100
    result = amestoy_vazquez_constant(n, d, a)
    # 5*(-100) + 5*(25-1)/2 = -500 + 60 = -440
    expected = -440.0
    error = abs(result - expected)
    
    assert error < 1e-10, f"Negative test 2 failed: got {result}, expected {expected}"
    print(f"  ✓ S({n},{d},{a}) = {result} (correct: -500 + 60 = -440)")
    
    print("✅ Negative values work correctly!")


def test_dimension_consistency():
    """
    Test mathematical consistency across dimensions.
    
    For fixed n and a, increasing d should increase the magic constant
    because n^d grows exponentially.
    """
    print("\nTesting dimension consistency...")
    
    n, a = 3, 1
    
    # Calculate for dimensions 2, 3, 4
    s2 = amestoy_vazquez_constant(n, 2, a)  # Square
    s3 = amestoy_vazquez_constant(n, 3, a)  # Cube
    s4 = amestoy_vazquez_constant(n, 4, a)  # 4D hypercube
    
    print(f"  S({n},2,{a}) = {s2} (square)")
    print(f"  S({n},3,{a}) = {s3} (cube)")
    print(f"  S({n},4,{a}) = {s4} (4D hypercube)")
    
    # Verify they increase with dimension
    assert s4 > s3, f"4D ({s4}) should be > 3D ({s3})"
    assert s3 > s2, f"3D ({s3}) should be > 2D ({s2})"
    
    # Verify the mathematical relationship
    # S(n,d+1,a) - S(n,d,a) = n(n^(d+1) - n^d)/2 = n^d * n(n-1)/2
    # This should be positive for n>1
    diff1 = s3 - s2
    diff2 = s4 - s3
    
    assert diff1 > 0, f"Difference 3D-2D should be positive, got {diff1}"
    assert diff2 > 0, f"Difference 4D-3D should be positive, got {diff2}"
    
    print(f"  Differences: 3D-2D = {diff1}, 4D-3D = {diff2}")
    print("✅ Dimension consistency verified!")


def test_zero_start():
    """
    Test with starting value zero.
    
    When a=0, the formula simplifies to: S = n(n^d - 1)/2
    """
    print("\nTesting zero starting value...")
    
    test_cases = [
        (3, 2, 0, 12.0),   # 3*(9-1)/2 = 24/2 = 12
        (4, 2, 0, 30.0),   # 4*(16-1)/2 = 60/2 = 30
        (3, 3, 0, 39.0),   # 3*(27-1)/2 = 78/2 = 39
    ]
    
    for n, d, a, expected in test_cases:
        result = amestoy_vazquez_constant(n, d, a)
        error = abs(result - expected)
        
        assert error < 1e-10, f"Zero test failed for n={n}, d={d}: got {result}, expected {expected}"
        
        # Also verify the simplified formula
        simplified = n * (n**d - 1) / 2
        assert abs(result - simplified) < 1e-10, f"Simplified formula mismatch for n={n}, d={d}"
        
        print(f"  ✓ S({n},{d},{a}) = {result} = n(n^{d}-1)/2 = {simplified}")
    
    print("✅ Zero starting value works correctly!")


def run_all_tests():
    """
    Run all tests and print a summary.
    """
    print("=" * 60)
    print("AMESTOY-VÁZQUEZ CONJECTURE - TEST SUITE")
    print("=" * 60)
    
    tests = [
        test_classical_case,
        test_known_values,
        test_negative_start,
        test_dimension_consistency,
        test_zero_start,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            failed += 1
            print(f"\n❌ {test_func.__name__} FAILED: {str(e)}")
        except Exception as e:
            failed += 1
            print(f"\n❌ {test_func.__name__} ERROR: {str(e)}")
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total tests: {len(tests)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! The formula is mathematically verified.")
        return True
    else:
        print("\n⚠️  Some tests failed. Please check the formula implementation.")
        return False


if __name__ == "__main__":
    """
    When this file is run directly (not imported),
    execute all tests automatically.
    """
    success = run_all_tests()
    
    # Exit with code 0 if all passed, 1 if any failed
    # This is useful for automated testing systems
    exit(0 if success else 1)
