import sys
from minimax_lab import max_value, visited

def run_test_1():
    """Test Case 1: Simple 2x2 Tree (50 Points)"""
    visited.clear()
    tree = [[3, 5], [2, 100]]
    # Cave 1 min: 3, Cave 2 min: 2. Max of (3, 2) is 3.
    val = max_value(tree)
    
    if val == 3 and len(visited) == 4:
        print("PASS: Test Case 1 successful.")
        sys.exit(0) # Success
    else:
        print(f"FAIL: Expected val=3, visited=4. Got val={val}, visited={len(visited)}")
        sys.exit(1) # Failure

def run_test_2():
    """Test Case 2: Complex 3-Cave Tree (50 Points)"""
    visited.clear()
    # Cave 1: [10, 15], Cave 2: [1, 2], Cave 3: [5, 8]
    # Mins: 10, 1, 5. Max of (10, 1, 5) is 10.
    tree = [[10, 15], [1, 2], [5, 8]]
    val = max_value(tree)
    
    if val == 10 and len(visited) == 6:
        print("PASS: Test Case 2 successful.")
        sys.exit(0)
    else:
        print(f"FAIL: Expected val=10, visited=6. Got val={val}, visited={len(visited)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_minimax.py [1|2]")
        sys.exit(1)

    test_choice = sys.argv[1]

    if test_choice == "1":
        run_test_1()
    elif test_choice == "2":
        run_test_2()
    else:
        print("Invalid argument. Use 1 or 2.")
        sys.exit(1)
