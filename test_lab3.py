import sys
import numpy as np
import pandas as pd
from lab_neuron import calculate_neuron_output

# Helper to capture the internal X matrix from the student's function
# This assumes the function is structured as we designed.
def test_conversion(): # 50 Points
    try:
        df = pd.read_csv('sensor.csv')
        # We check if they at least return the right type and shape
        X, z = calculate_neuron_output('sensor.csv')
        assert isinstance(X, np.ndarray), "Result must be a NumPy array."
        assert X.shape == (3,2), f"Expected shape (3,2), got {X.shape}"
        print("✅ Step 1 Passed: Data loaded and converted correctly.")
    except Exception as e:
        print(f"❌ Step 1 Failed: {e}")
        sys.exit(1)

def test_math(): # 50 Points
    expected = np.array([1, 1, 1])
    try:
        X, z = calculate_neuron_output('sensor.csv')
        if np.array_equal(z, expected):
            print("✅ Step 2 Passed: Matrix math and activation are correct.")
        else:
            print(f"❌ Step 2 Failed: Expected {expected}, got {z}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Step 2 Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "1"
    if arg == "1":
        test_conversion()
    elif arg == "2":
        test_math()
