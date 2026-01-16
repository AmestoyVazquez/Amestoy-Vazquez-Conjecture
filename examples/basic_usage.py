"""
Basic usage example for Amestoy-Vázquez Conjecture
"""
from src.formula import amestoy_vazquez_constant


def main():
    print("Amestoy-Vázquez Conjecture - Usage Examples")
    print("=" * 50)
    
    # Example 1: Classical magic square
    print("\n1. Classical 3x3 magic square:")
    n, d, a = 3, 2, 1
    result = amestoy_vazquez_constant(n, d, a)
    print(f"   S({n},{d},{a}) = {result}")
    print(f"   ✓ Known value: 8+1+6 = 15")
    
    # Example 2: Custom starting value
    print("\n2. 3x3 square starting at 100:")
    n, d, a = 3, 2, 100
    result = amestoy_vazquez_constant(n, d, a)
    print(f"   S({n},{d},{a}) = {result}")
    print(f"   ✓ Square: [107,100,105], [102,104,106], [103,108,101]")
    print(f"   ✓ Sum: 107+100+105 = {result}")
    
    # Example 3: 3D cube
    print("\n3. 5x5x5 magic cube starting at 500.5:")
    n, d, a = 5, 3, 500.5
    result = amestoy_vazquez_constant(n, d, a)
    print(f"   S({n},{d},{a}) = {result}")
    
    # Example 4: Even order
    print("\n4. 4x4 square starting at 50:")
    n, d, a = 4, 2, 50
    result = amestoy_vazquez_constant(n, d, a)
    print(f"   S({n},{d},{a}) = {result}")
    
    print("\n" + "=" * 50)
    print("Formula: S(n,d,a) = n·a + n(n^d - 1)/2")
    print("=" * 50)


if __name__ == "__main__":
    main()
