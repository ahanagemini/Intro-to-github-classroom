import sys
from alphabeta_assign import max_value, visited

def run_test_1():
    """Test Case 1: Standard Pruning Check (50 Points)"""
    visited.clear()
    tree = [
        [3, 5],    # Cave 1 -> Sets alpha = 3
        [2, 100]   # Cave 2 -> Min sees 2. Since 2 <= 3, it should prune immediately!
    ]
    
    val = max_value(tree, -float('inf'), float('inf'))
    
    # Validation
    correct_val = (val == 3)
    # Correct pruning path: 3, 5, 2. The 100 node MUST be skipped.
    correct_prune = (len(visited) == 3 and 100 not in visited)
    
    if correct_val and correct_prune:
        print("PASS: Test Case 1 successful. Node 100 was correctly pruned.")
        sys.exit(0)
    else:
        print(f"FAIL: Expected val=3, visited_len=3. Got val={val}, visited={visited}")
        sys.exit(1)

def run_test_2():
    """Test Case 2: Deep 3-Cave Pruning (50 Points)"""
    visited.clear()
    tree = [
        [10, 20],  # Cave 1 -> Sets alpha = 10
        [5, 50],   # Cave 2 -> Min sees 5. 5 <= 10 -> Prunes 50!
        [12, 1]    # Cave 3 -> Min sees 12, then 1 -> Returns 1. No prune here.
    ]
    
    val = max_value(tree, -float('inf'), float('inf'))
    
    # Validation
    correct_val = (val == 10)
    # Node 50 must be skipped entirely.
    correct_prune = (len(visited) == 5 and 50 not in visited)
    
    if correct_val and correct_prune:
        print("PASS: Test Case 2 successful. Node 50 was correctly pruned.")
        sys.exit(0)
    else:
        print(f"FAIL: Expected val=10, visited_len=5. Got val={val}, visited={visited}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_alphabeta.py [1|2]")
        sys.exit(1)

    test_choice = sys.argv[1]

    if test_choice == "1":
        run_test_1()
    elif test_choice == "2":
        run_test_2()
    else:
        print("Invalid argument. Use 1 or 2.")
        sys.exit(1)
