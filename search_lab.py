import sys
from queue import PriorityQueue

# --- INFRASTRUCTURE (Do Not Edit) ---

class Node:
    """A node in a search tree. Contains a state, parent, and the cost g(n)."""
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost

    def expand(self, problem):
        """Returns a list of reachable nodes in one step from this node."""
        return [Node(next_s, self, self.path_cost + cost)
                for next_s, cost in problem.get_successors(self.state)]
    
    def __lt__(self, other):
        """Allows PriorityQueue to compare two nodes if their costs are equal."""
        return self.path_cost < other.path_cost

class MapProblem:
    """Defines the state space, initial state, and goal condition."""
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def get_successors(self, state):
        return self.graph.get(state, [])

    def is_goal(self, state):
        return state == self.goal

# --- ROMANIAN MAP DATA ---

romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Craiova': [('Rimnicu', 146), ('Pitesti', 138), ('Drobeta', 120)],
    'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)]
}

# --- STUDENT TASKS ---

def breadth_first_search(problem):
    """
    Step 1 (50 Points): Find the path with the FEWEST number of cities.
    
    Instructions:
    1. Create a Node for the starting state (problem.initial).
    2. Initialize your 'queue' as a regular list: queue = [start_node]
    3. Create a set called 'visited' to track states you have seen.
    4. WHILE the queue has items:
       - Pop the OLDEST node from the front: node = queue.pop(0)
       - IF the node's state is the goal: return the node.
       - IF the state is not in 'visited':
         - Add it to 'visited', expand the node, and add children to the BACK of the queue.
    """
    # TODO: YOUR CODE HERE
    pass

def uniform_cost_search(problem):
    """
    Step 2 (50 Points): Find the path with the LOWEST total kilometers.
    
    Instructions:
    1. Create a Node for the starting state.
    2. Initialize your 'queue' using PriorityQueue().
    3. Put the start node into the queue with a priority of 0.
       Format: queue.put((0, start_node))
    4. WHILE the queue is not empty:
       - Get the cheapest node: (cost, node) = queue.get()
       - IF it is the goal: return the node.
       - IF the state is not in 'visited':
         - Add to visited, expand, and add children to queue using child.path_cost as priority.
    """
    # TODO: YOUR CODE HERE
    pass

if __name__ == "__main__":
    # Local Test
    prob = MapProblem('Arad', 'Bucharest', romania_map)
    
    print("Testing BFS...")
    res_bfs = breadth_first_search(prob)
    if res_bfs: print(f"BFS Path Cost: {res_bfs.path_cost}")
    
    print("\nTesting UCS...")
    res_ucs = uniform_cost_search(prob)
    if res_ucs: print(f"UCS Path Cost: {res_ucs.path_cost}")
