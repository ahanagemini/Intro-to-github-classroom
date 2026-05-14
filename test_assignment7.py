import sys
import numpy as np
from calculus_assignment import gradient_descent

def test_1_convergence():
    print("▶ Running Test Case 1: Checking convergence vector trends with balanced alpha=0.1...")
    # Run loop starting from far coordinates with safe balanced step size
    weight_history, loss_history = gradient_descent(start_w1=2.5, start_w2=2.0, alpha=0.1, num_iterations=10)
    
    initial_dist = np.linalg.norm([2.5, 2.0])
    final_dist = np.linalg.norm(weight_history[-1])
    
    # Assertive check 1: Loss must display down-slope decay
    if not all(x >= y for x, y in zip(loss_history, loss_history[1:])):
        print("❌ TEST 1 FAILED: Loss values failed to decrease monotonically during downward steps.")
        return False
        
    # Assertive check 2: Coordinates must reside structurally closer to the target minimum
    if final_dist >= initial_dist:
        print(f"❌ TEST 1 FAILED: Coordinates migrated away from target. Initial distance {initial_dist:.2f} -> Final {final_dist:.2f}")
        return False

    print("✅ TEST 1 PASSED: Gradient descent safely and stably converges weights to the loss minimum.")
    return True

def test_2_step_decay():
    print("▶ Running Test Case 2: Checking physical step decay characteristics (Slide 34)...")
    # Run static loop configurations
    weight_history, _ = gradient_descent(start_w1=3.0, start_w2=3.0, alpha=0.05, num_iterations=5)
    
    # Compute Euclidean jump length across the initial and final step intervals
    step_1_span = np.linalg.norm(weight_history[1] - weight_history[0])
    step_4_span = np.linalg.norm(weight_history[4] - weight_history[3])
    
    # Because the slope drops near zero, spatial step distances MUST systematically shrink over time
    if step_4_span >= step_1_span:
        print(f"❌ TEST 2 FAILED: Step size didn't drop. Step 1 span: {step_1_span:.4f} | Step 4 span: {step_4_span:.4f}")
        print("💡 Hint: Verify you are updating coordinates using 'w = w - alpha * grad' and not applying static step steps.")
        return False

    print("✅ TEST 2 PASSED: Local steps successfully scale down as function slope approaches zero flat zones.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Error: Missing test case parameter.\nUsage:\n  python test_homework.py 1\n  python test_homework.py 2")
        sys.exit(1)
        
    choice = sys.argv[1]
    if choice == "1": success = test_1_convergence()
    elif choice == "2": success = test_2_step_decay()
    else:
        print("❌ Invalid selection parameter flag. Please choose argument option '1' or '2'.")
        sys.exit(1)
        
    sys.exit(0 if success else 1)
