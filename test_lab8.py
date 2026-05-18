import sys
import numpy as np
import regression_lab as lab

def get_housing_dataset():
    np.random.seed(42)
    X = np.random.uniform(500, 3500, size=(40, 1))
    true_w1, true_w0 = 0.232, 246.0
    noise = np.random.normal(0, 50, size=(40, 1))
    y = true_w1 * X + true_w0 + noise
    return X, y

def run_test_case_1():
    print("--- Running Test Case 1: Euclidean Distance Function ---")
    v1 = np.array([1.0, 2.0])
    v2 = np.array([4.0, 6.0])
    dist = lab.euclidean_distance(v1, v2)
    assert np.isclose(dist, 5.0), f"Test Case 1 Failed. Expected distance 5.0, got {dist}"
    print("[PASS] Test Case 1: Euclidean distance calculation is correct.")

def run_test_case_2():
    print("--- Running Test Case 2: k-NN Neighborhood Selection ---")
    X_train = np.array([[1000.0], [2000.0], [3000.0]])
    y_train = np.array([[400.0], [600.0], [800.0]])
    X_query = np.array([[1100.0]])
    
    pred_k1 = lab.knn_predict(X_train, y_train, X_query, k=1)
    assert np.isclose(float(pred_k1[0][0]), 400.0), f"Test Case 2 (k=1) Failed. Expected 400.0, got {pred_k1}"
    
    pred_k2 = lab.knn_predict(X_train, y_train, X_query, k=2)
    assert np.isclose(float(pred_k2[0][0]), 500.0), f"Test Case 2 (k=2) Failed. Expected 500.0, got {pred_k2}"
    print("[PASS] Test Case 2: k-NN predictions match neighborhood averages.")

def run_test_case_3():
    print("--- Running Test Case 3: Scikit-Learn Model Fitting & Prediction ---")
    X_train = np.array([[1000.0], [2000.0], [3000.0]])
    y_train = np.array([[400.0], [600.0], [800.0]])
    X_test = np.array([[1500.0], [2500.0]])
    
    preds = lab.train_and_predict_linear(X_train, y_train, X_test)
    expected_preds = np.array([[500.0], [700.0]])
    assert np.allclose(preds, expected_preds, atol=1e-3), f"Test Case 3 Failed. Expected {expected_preds.tolist()}, got {preds.tolist()}"
    print("[PASS] Test Case 3: Linear regression model parameters fitted and evaluated correctly.")

def run_test_case_4():
    print("--- Running Test Case 4: Mean Squared Error (MSE) Evaluation ---")
    y_true = np.array([[400.0], [600.0]])
    y_pred = np.array([[402.0], [599.0]]) 
    mse = lab.mean_squared_error(y_true, y_pred)
    assert np.isclose(mse, 2.5), f"Test Case 4 Failed. Expected MSE 2.5, got {mse}"
    print("[PASS] Test Case 4: Mean Squared Error loss calculation is correct.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_lab.py [1, 2, 3, or 4]")
        sys.exit(1)
        
    test_case_id = sys.argv[1]
    if test_case_id == "1": run_test_case_1()
    elif test_case_id == "2": run_test_case_2()
    elif test_case_id == "3": run_test_case_3()
    elif test_case_id == "4": run_test_case_4()
    else: sys.exit(1)
