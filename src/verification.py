"""
Verification system for Amestoy-Vázquez Conjecture
Author: Juan Pedro Amestoy Vazquez
"""
import numpy as np
import time
from .formula import amestoy_vazquez_constant


def generate_magic_square_odd(n: int, start: float = 1.0) -> np.ndarray:
    """
    Generate magic square using Siamese method (odd n only).
    
    Parameters:
    -----------
    n : int
        Order of square (must be odd)
    start : float
        Starting value
        
    Returns:
    --------
    np.ndarray
        n x n magic square
    """
    if n % 2 == 0:
        raise ValueError("Siamese method requires odd n")
    
    square = np.zeros((n, n), dtype=float)
    i, j = 0, n // 2
    current = float(start)
    
    for _ in range(n * n):
        square[i, j] = current
        current += 1.0
        
        new_i = (i - 1) % n
        new_j = (j + 1) % n
        
        if square[new_i, new_j] != 0:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    
    return square


def verify_square(square: np.ndarray) -> tuple[bool, float]:
    """
    Verify a square is magic and return constant.
    
    Parameters:
    -----------
    square : np.ndarray
        Square to verify
        
    Returns:
    --------
    (bool, float)
        (is_magic, constant)
    """
    n = square.shape[0]
    constant = np.sum(square[0, :])
    
    # Check rows
    if not np.allclose(np.sum(square, axis=1), constant):
        return False, 0.0
    
    # Check columns
    if not np.allclose(np.sum(square, axis=0), constant):
        return False, 0.0
    
    # Check diagonals
    if not np.isclose(np.trace(square), constant):
        return False, 0.0
    
    if not np.isclose(np.trace(np.fliplr(square)), constant):
        return False, 0.0
    
    return True, constant


def run_verification_tests() -> dict:
    """
    Run comprehensive verification tests.
    
    Returns:
    --------
    dict
        Test results
    """
    print("Amestoy-Vázquez Conjecture Verification")
    print("=" * 50)
    
    test_cases = [
        (3, 1.0, "Classical 3x3"),
        (3, 100.0, "3x3 starting at 100"),
        (5, 500.5, "5x5 starting at 500.5"),
        (7, 0.0, "7x7 starting at 0"),
    ]
    
    results = {
        "total": len(test_cases),
        "passed": 0,
        "failed": 0,
        "details": []
    }
    
    for n, a, description in test_cases:
        try:
            # Generate actual magic square
            square = generate_magic_square_odd(n, a)
            
            # Verify it's magic
            is_magic, actual = verify_square(square)
            
            if not is_magic:
                print(f"✗ {description}: Generated square is not magic")
                results["failed"] += 1
                continue
            
            # Calculate predicted value
            predicted = amestoy_vazquez_constant(n, 2, a)
            
            # Check match
            match = np.isclose(actual, predicted, rtol=1e-10)
            
            if match:
                print(f"✓ {description}: Actual={actual}, Predicted={predicted}")
                results["passed"] += 1
            else:
                print(f"✗ {description}: Mismatch (Actual={actual}, Predicted={predicted})")
                results["failed"] += 1
                
            results["details"].append({
                "n": n, "a": a, "description": description,
                "actual": actual, "predicted": predicted,
                "match": match
            })
            
        except Exception as e:
            print(f"✗ {description}: Error - {str(e)}")
            results["failed"] += 1
    
    print("\n" + "=" * 50)
    print(f"Total tests: {results['total']}")
    print(f"Passed: {results['passed']}")
    print(f"Failed: {results['failed']}")
    
    if results["failed"] == 0:
        print("\n✅ All tests passed! Conjecture verified.")
    else:
        print("\n⚠️ Some tests failed.")
    
    return results


if __name__ == "__main__":
    results = run_verification_tests()
    exit(0 if results["failed"] == 0 else 1)
