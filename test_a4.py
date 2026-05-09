import sys
import numpy as np
import pandas as pd
from solver import solve_coffee_blend, train_and_predict

def run_test(step):
    try:
        if step == "1": # 50 Points: Coffee Solver
            sol = solve_coffee_blend()
            expected = np.array([0.5, 0.5])
            if not np.allclose(sol, expected, atol=1e-5):
                raise ValueError(f"Expected [0.5, 0.5], got {sol}")
            print("✅ Step 1 Passed: Coffee system solved.")

        elif step == "2": # 50 Points: Normal Equation & Prediction
            new_student = np.array([5, 2])
            weights, pred = train_and_predict('student_success.csv', new_student)
            
            # Theoretical weights for this data are [2.0, 1.0]
            # Prediction: (5*2.0) + (2*1.0) = 12.0
            if not np.allclose(weights, [2.0, 1.0], atol=1e-5):
                raise ValueError(f"Weights incorrect. Expected [2, 1], got {weights}")
            if not np.isclose(pred, 12.0):
                raise ValueError(f"Prediction incorrect. Expected 12.0, got {pred}")
            print("✅ Step 2 Passed: Weights learned and grade predicted.")

    except Exception as e:
        print(f"❌ Step {step} Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_test(sys.argv[1])
