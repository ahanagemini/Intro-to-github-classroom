import sys
import numpy as np
import lab10 as lab

def get_seismic_dataset():
    # Inspired by Slide 27: body wave magnitude (x1) and surface wave magnitude (x2)
    # Class 0: Earthquakes, Class 1: Nuclear Explosions
    X = np.array([
        [4.5, 4.0], [5.0, 4.5], [5.5, 5.0],  # Earthquakes (Class 0)
        [6.0, 4.2], [6.2, 4.4], [5.8, 3.8]   # Explosions (Class 1)
    ])
    y = np.array([0, 0, 0, 1, 1, 1])
    return X, y

def run_test_case_1():
    print("--- Running Test Case 1: Euclidean Distance Function ---")
    v1 = np.array([1.0, 2.0])
    v2 = np.array([4.0, 6.0])
    dist = lab.euclidean_distance(v1, v2)
    assert np.isclose(dist, 5.0), f"Test Case 1 Failed. Expected 5.0, got {dist}"
    print("[PASS] Test Case 1: Euclidean distance calculation is correct.")

def run_test_case_2():
    print("--- Running Test Case 2: k-NN Neighborhood Majority Voting ---")
    X_train, y_train = get_seismic_dataset()
    X_query = np.array([[4.8, 4.2], [6.1, 4.1]])  # Query 1 near Earthquakes, Query 2 near Explosions
    
    preds = lab.knn_classify(X_train, y_train, X_query, k=3)
    assert preds.shape == (2,), f"Expected shape (2,), got {preds.shape}"
    assert int(preds[0]) == 0, f"Expected index 0 to be Class 0, got {preds[0]}"
    assert int(preds[1]) == 1, f"Expected index 1 to be Class 1, got {preds[1]}"
    print("[PASS] Test Case 2: k-NN loops accurately resolve class counts and majority winners.")

def run_test_case_3():
    print("--- Running Test Case 3: Logistic Regression Model Fitting ---")
    X_train, y_train = get_seismic_dataset()
    X_test = np.array([[4.6, 4.1], [5.9, 4.0]])
    
    preds = lab.train_and_predict_logistic(X_train, y_train, X_test)
    assert preds.shape == (2,), f"Expected shape (2,), got {preds.shape}"
    assert int(preds[0]) == 0, f"Expected linear separator class 0, got {preds[0]}"
    assert int(preds[1]) == 1, f"Expected linear separator class 1, got {preds[1]}"
    print("[PASS] Test Case 3: Logistic Regression classifier separates patterns cleanly.")

def run_test_case_4():
    print("--- Running Test Case 4: Classification Accuracy Evaluation ---")
    y_true = np.array([0, 1, 0, 1, 1])
    y_pred = np.array([0, 1, 0, 0, 1])  # 4 out of 5 correct -> 0.8 accuracy
    acc = lab.accuracy_score(y_true, y_pred)
    assert np.isclose(acc, 0.8), f"Test Case 4 Failed. Expected 0.8, got {acc}"
    print("[PASS] Test Case 4: Manual loop classification accuracy metric is correct.")

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
