import numpy as np
n = 3
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])
try:
    A_inv = np.linalg.inv(A)
    print(f"原矩阵 A ({n}x{n}):")
    print(A)
    print("\n矩阵 A 的逆矩阵:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("矩阵不可逆")