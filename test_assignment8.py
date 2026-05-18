import sys
import numpy as np
import gradient_descent as lab

def get_housing_dataset():
    np.random.seed(42)
    X = np.random.uniform(500, 3500, size=(40, 1))
    true_w1, true_w0 = 0.232, 246.0
    noise = np.random.normal(0, 50, size=(40, 1))
    # Keep vectors structurally separated to preserve shapes without ravel iterations
    y = true_w1 * X[:, 0] + true_w0 + noise[:, 0]
    return X, y

def run_test_case_1():
    print("--- Running Test Case 1: Matrix Prediction ---")
    X, _ = get_housing_dataset()
    w = np.array([0.232])
    w0 = 246.0
    
    preds = lab.compute_predictions(X, w, w0)
    assert preds.shape == (40,), f"Expected flat 1D array of length 40, got {preds.shape}"
    expected = (X @ w) + w0
    assert np.allclose(preds, expected), "Prediction matrix calculation error."
    print("[PASS] Test Case 1: Matrix predictions match expectations.")

def run_test_case_2():
    print("--- Running Test Case 2: Explicit Slide Update Rules ---")
    X, y = get_housing_dataset()
    
    w_next, w0_next = lab.train_gradient_descent(X, y, learning_rate_w=1e-8, learning_rate_w0=1e-4, epochs=1)
    
    # Validation step based strictly on initial zero matrices
    initial_errors = y - ((X @ np.zeros(1)) + 0.0)
    expected_w0 = 0.0 + 1e-4 * np.sum(initial_errors)
    expected_w1 = 0.0 + 1e-8 * np.sum(initial_errors * X[:, 0])
    
    assert np.isclose(w0_next, expected_w0), f"Bias w0 update error. Expected {expected_w0}, got {w0_next}"
    assert np.isclose(w_next[0], expected_w1), f"Weight matrix w update error. Expected {expected_w1}, got {w_next[0]}"
    print("[PASS] Test Case 2: Discrete update steps match slide rules exactly.")

def run_test_case_3():
    print("--- Running Test Case 3: Complete Optimization Convergence ---")
    X, y = get_housing_dataset()
    
    w_opt, w0_opt = lab.train_gradient_descent(X, y, learning_rate_w=1e-8, learning_rate_w0=1e-4, epochs=30000)
    
    assert w_opt[0] > 0.1 and w_opt[0] < 0.4, f"Slope matrix parameter failed to converge. Got {w_opt[0]}"
    assert w0_opt > 10.0, f"Standalone bias failed to shift positively. Got {w0_opt}"
    print("[PASS] Test Case 3: Matrix weights and bias successfully optimized.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_gradient.py [1, 2, or 3]")
        sys.exit(1)
        
    test_case_id = sys.argv[1]
    if test_case_id == "1": run_test_case_1()
    elif test_case_id == "2": run_test_case_2()
    elif test_case_id == "3": run_test_case_3()
    else: sys.exit(1)
