import numpy as np
from numpy import ndarray

class MatrixGenerator:
    def __init__(self) -> None:
        pass

    def generate_random_matrix(self, size: int) -> ndarray[int, int]:
        return np.array([np.random.randint(2, size=size) for _ in range(size)], dtype=int)
    
    def generate_simple_arena(self, size: int) -> ndarray[int, int]:
        matrix = np.array([
                np.ones(size, dtype=int) if i == 0 or i == (size - 1) 
                    else np.zeros(size, dtype=int) 
                for i in range(size)
                ])
        for i in range(size):
            matrix[i][0] = 1
            matrix[i][-1] = 1
        return matrix