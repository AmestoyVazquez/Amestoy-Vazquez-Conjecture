# The Amestoy Vazquez Theorem: Orthogonal Invariance in N-Dimensional Systems

**Official DOI:** [10.5281/zenodo.18248839](https://doi.org/10.5281/zenodo.18248839)

Official Python implementation of the **Amestoy Vazquez Theorem** for calculating invariance constants in N-dimensional tensors.

## Overview
The algorithm reduces computational complexity from O(N^d) to **O(1)**, enabling instantaneous integrity validation for massive datasets across any dimension and any starting point.

## 🚀 Run & Test it Online (No installation required)
You can test the theorem's logic and calculate constants directly in your browser using this interactive link:
👉 **[Run Amestoy Vazquez Theorem Online](https://www.online-python.com/oVz675NSCf)**

## Implementation Logic
The core of the theorem is implemented as follows:

```python
def amestoy_vazquez_constant(n, d, start_val=1):
    # The Amestoy Vazquez Formula
    # Instant calculation regardless of dimension or scale
    return (n * (start_val + (start_val + n**d - 1))) / 2
