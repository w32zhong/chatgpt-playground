"""Simple script to generate and display a random 3x2 matrix."""

import numpy as np


def main() -> None:
    """Create a 3x2 matrix with random values and print it."""
    matrix = np.random.rand(3, 2)
    print("Random 3x2 matrix:")
    print(matrix)


if __name__ == "__main__":
    main()
