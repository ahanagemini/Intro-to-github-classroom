import sys
import numpy as np
import sympy as sp
from lab7 import compute_gradient_manual, compute_gradient_and_critical_with_sympy

def test_1_minimum():
    print("▶ Running Test Case 1: Checking manual gradient at global minimum (0,0)...")
    grad = compute_gradient_manual(0.0, 0.0)
    if np.allclose(grad, [0.0, 0.0]):
        print("✅ TEST 1 PASSED: Manual gradient at minimum is exactly [0.0, 0.0].")
        return True
    print(f"❌ TEST 1 FAILED: Expected [0.0, 0.0], got {list(grad)}.")
    return False

def test_2_quadrants():
    print("▶ Running Test Case 2: Checking manual gradient value scaling...")
    grad_pos = compute_gradient_manual(2.0, 1.0)
    grad_neg = compute_gradient(-3.0, -2.0)
    
    if np.allclose(grad_pos, [4.0, 6.0]) and np.allclose(grad_neg, [-6.0, -12.0]):
        print("✅ TEST 2 PASSED: Manual quadrant scaling evaluations are accurate.")
        return True
    print("❌ TEST 2 FAILED: Value scaling rules or negative signs are incorrect.")
    return False

def test_3_sympy_verification():
    print("▶ Running Test Case 3: Testing SymPy analytic symbolic engine output...")
    try:
        deriv_w1, deriv_w2, crit_dict = compute_gradient_and_critical_with_sympy()
        
        # Test 3a: Verify symbolic expressions
        w1_sym, w2_sym = sp.symbols('w1 w2')
        if deriv_w1 != 2*w1_sym or deriv_w2 != 6*w2_sym:
            print(f"❌ TEST 3 FAILED: SymPy derivatives incorrect. Got dL/dw1={deriv_w1}, dL/dw2={deriv_w2}")
            return False
            
        # Test 3b: Verify critical point solving logic
        if crit_dict != {w1_sym: 0, w2_sym: 0}:
            print(f"❌ TEST 3 FAILED: Critical point solver incorrect. Got: {crit_dict}")
            return False
            
        print("✅ TEST 3 PASSED: SymPy successfully derived and localized the critical point at (0,0)!")
        return True
    except Exception as e:
        print(f"❌ TEST 3 FAILED with exception error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Error: Missing test case selection argument.\nUsage:\n  python test_lab.py 1\n  python test_lab.py 2\n  python test_lab.py 3")
        sys.exit(1)
        
    choice = sys.argv[1]
    if choice == "1": success = test_1_minimum()
    elif choice == "2": success = test_2_quadrants()
    elif choice == "3": success = test_3_sympy_verification()
    else:
        print("❌ Invalid selection. Use arguments '1', '2', or '3'.")
        sys.exit(1)
        
    sys.exit(0 if success else 1)
