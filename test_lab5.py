import sys
from search_lab import breadth_first_search, uniform_cost_search, MapProblem, romania_map

def run_test(step):
    # Initialize the standard Romania problem: Arad to Bucharest
    prob = MapProblem('Arad', 'Bucharest', romania_map)

    try:
        if step == "1": # 50 Points: BFS (Fewest Steps)
            print("--- Testing BFS Implementation ---")
            res = breadth_first_search(prob)
            
            if res is None:
                raise ValueError("BFS returned None. Goal not found.")
            
            # BFS path: Arad-Sibiu-Fagaras-Bucharest (Cost 450)
            if res.path_cost != 450:
                raise ValueError(f"BFS found wrong path. Expected cost 450, got {res.path_cost}")
            
            print("✅ BFS Passed: Found the path with fewest hops.")

        elif step == "2": # 50 Points: UCS (Cheapest Path)
            print("--- Testing UCS Implementation ---")
            res = uniform_cost_search(prob)
            
            if res is None:
                raise ValueError("UCS returned None. Goal not found.")
            
            # UCS path: Arad-Sibiu-Rimnicu-Pitesti-Bucharest (Cost 418)
            if res.path_cost != 418:
                raise ValueError(f"UCS found wrong path. Expected cost 418, got {res.path_cost}")
            
            print("✅ UCS Passed: Found the mathematically cheapest path.")

        else:
            print(f"Invalid choice '{step}'. Use '1' for BFS or '2' for UCS.")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Test Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_test(sys.argv[1])
    else:
        print("Usage: python test_lab6.py [1|2]")
