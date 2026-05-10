import sys
from search_assignment import greedy_search, astar_search, MapProblem, romania_map, h_bucharest

def run_test(step):
    prob = MapProblem('Arad', 'Bucharest', romania_map)

    try:
        if step == "1": # 50 Points: Greedy
            print("--- Testing Step 1: Greedy Search ---")
            res = greedy_search(prob, h_bucharest)
            if res is None: raise ValueError("Greedy returned None.")
            
            # Greedy on this map finds Arad-Sibiu-Fagaras-Bucharest (450)
            if res.path_cost != 450:
                raise ValueError(f"Greedy found wrong path cost. Expected 450, got {res.path_cost}")
            print("✅ Step 1 Passed: Greedy found the path.")

        elif step == "2": # 50 Points: A*
            print("--- Testing Step 2: A* Search ---")
            res = astar_search(prob, h_bucharest)
            if res is None: raise ValueError("A* returned None.")
            
            # A* finds the optimal path (418)
            if res.path_cost != 418:
                raise ValueError(f"A* found wrong path cost. Expected 418, got {res.path_cost}")
            print("✅ Step 2 Passed: A* found the optimal path.")

    except Exception as e:
        print(f"❌ Step {step} Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_test(sys.argv[1])
