import sys
import numpy as np
from linalg_lab import vector_math, normalize_vector, matrix_ops, is_orthogonal, rotate_90

def run_test(step):
    if step == "1": # Vector Math (20 pts)
        a, b = np.array([1, 2]), np.array([3, 4])
        res = vector_math(a, b)
        assert np.array_equal(res[0], [4, 6]), "Sum failed"
        assert res[2] == 11, "Dot product failed"
        print("✅ Step 1 Passed")

    elif step == "2": # Normalization (20 pts)
        v = np.array([3, 4])
        assert np.allclose(normalize_vector(v), [0.6, 0.8]), "Normalization failed"
        print("✅ Step 2 Passed")

    elif step == "3": # Matrix Multiplication (20 pts)
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[1, 0], [0, 1]])
        assert np.array_equal(matrix_ops(A, B), A), "Matrix multiplication failed"
        print("✅ Step 3 Passed")

    elif step == "4": # Orthogonality (20 pts)
        assert is_orthogonal(np.array([1, 0]), np.array([0, 1])) == True
        assert is_orthogonal(np.array([1, 2]), np.array([1, 1])) == False
        print("✅ Step 4 Passed")

    elif step == "5": # Rotation (20 pts)
        v = np.array([1, 0])
        # R @ [1,0] should be [0,1]
        assert np.allclose(rotate_90(v), [0, 1]), "90-degree rotation failed"
        print("✅ Step 5 Passed")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_test(sys.argv[1])
