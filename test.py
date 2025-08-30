"""Simple script to demonstrate indexing on a random 3x2 matrix."""

import numpy as np


def main() -> None:
    """Create a 3x2 matrix, index it with tensors of various shapes, and print results."""
    np.random.seed(0)
    matrix = np.random.rand(3, 2)
    print("Random 3x2 matrix:")
    # Random 3x2 matrix:
    print(matrix)
    # [[0.5488135  0.71518937]
    #  [0.60276338 0.54488318]
    #  [0.4236548  0.64589411]]

    # 1D index tensor
    index_1d = np.array([0, 2])
    print("\n1D index tensor:", index_1d)
    # 1D index tensor: [0 2]
    print("Values indexed by 1D tensor:")
    # Values indexed by 1D tensor:
    print(matrix[index_1d])
    # [[0.5488135  0.71518937]
    #  [0.4236548  0.64589411]]

    # 2D index tensor
    index_2d = np.array([[0, 1], [2, 0]])
    print("\n2D index tensor:\n", index_2d)
    # 2D index tensor:
    # [[0 1]
    #  [2 0]]
    print("Values indexed by 2D tensor:")
    # Values indexed by 2D tensor:
    print(matrix[index_2d])
    # [[[0.5488135  0.71518937]
    #   [0.60276338 0.54488318]]
    #
    #  [[0.4236548  0.64589411]
    #   [0.5488135  0.71518937]]]

    # 3D index tensor
    index_3d = np.array([[[0, 1]], [[2, 0]]])
    print("\n3D index tensor:\n", index_3d)
    # 3D index tensor:
    # [[[0 1]]
    #
    #  [[2 0]]]
    print("Values indexed by 3D tensor:")
    # Values indexed by 3D tensor:
    print(matrix[index_3d])
    # [[[[0.5488135  0.71518937]
    #    [0.60276338 0.54488318]]]
    #
    #  [[[0.4236548  0.64589411]
    #    [0.5488135  0.71518937]]]]


if __name__ == "__main__":
    main()
