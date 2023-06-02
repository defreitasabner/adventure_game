import numpy as np
from numpy import ndarray

class MatrixGenerator:
    def __init__(self) -> None:
        pass

    def generate_random_matrix(self, size: int) -> ndarray[int, int]:
        return np.array([np.random.randint(2, size=size) for _ in range(size)], dtype=int)