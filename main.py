def amestoy_vazquez_constant(n, d, start_val=1):
    """
    Calculates the orthogonal invariance constant for an N-dimensional hypercube.
    n: side length
    d: dimensions
    start_val: starting number of the sequence
    """
    # The Amestoy Vazquez Formula
    return (n * (start_val + (start_val + n**d - 1))) / 2

def main():
    print("--- Amestoy Vazquez Theorem Tool ---")
    try:
        n = int(input("Enter side length (n): "))
        d = int(input("Enter dimensions (d): "))
        start = float(input("Enter starting value (default 1): ") or 1)
        
        result = amestoy_vazquez_constant(n, d, start)
        
        print(f"\n[Result] The Invariance Constant is: {result}")
        print("-" * 36)
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
