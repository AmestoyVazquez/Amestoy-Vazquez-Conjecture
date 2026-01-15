# The Amestoy Vazquez Theorem: Orthogonal Invariance in N-Dimensional Systems

**Official DOI:** [10.5281/zenodo.18248839](https://doi.org/10.5281/zenodo.18248839)

Official Python implementation of the **Amestoy Vazquez Theorem** for calculating invariance constants in N-dimensional tensors.

## Overview
The algorithm reduces computational complexity from O(N^d) to **O(1)**, enabling instantaneous integrity validation for massive datasets across any dimension and any starting point.

## 🚀 Interactive Implementation

Experience the theorem's efficiency firsthand through our official interactive environments:

| Platform | Access Type | Link |
| :--- | :--- | :--- |
| **Official Web App** | **Instant Run (No login)** | [**Launch Calculator ⚡**](https://amestoy-vazquez-theorem-calculator--amestoyvazquez.replit.app/) |
| **Google Colab** | Research & LaTeX View | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xI1gWXsaahZloBEfsekv6Zn-1NRMdbLl?usp=sharing) |

> [!TIP]
> Use the **Web App** for a quick mobile-friendly test or **Google Colab** to review the mathematical documentation and step-by-step breakdown.

## Implementation Logic
The core of the theorem is implemented as follows:

```python
def amestoy_vazquez_constant(n, d, start_val=1):
    # The Amestoy Vazquez Formula
    # Instant calculation regardless of dimension or scale
    return (n * (start_val + (start_val + n**d - 1))) / 2
