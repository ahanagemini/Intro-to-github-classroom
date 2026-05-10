import sys
from queue import PriorityQueue

# --- INFRASTRUCTURE (Do Not Edit) ---

class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost

    def expand(self, problem):
        return [Node(next_s, self, self.path_cost + cost)
                for next_s, cost in problem.get_successors(self.state)]
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost

class MapProblem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph
    def get_successors(self, state):
        return self.graph.get(state, [])
    def is_goal(self, state):
        return state == self.goal

# --- DATASET & HEURISTICS ---

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

# Straight-line distance to Bucharest (Heuristic 'h')
h_bucharest = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253,
    'Fagaras': 176, 'Rimnicu': 193, 'Craiova': 160, 'Pitesti': 100,
    'Timisoara': 329, 'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242,
    'Bucharest': 0
}

# --- STUDENT TASKS ---

def greedy_search(problem, h):
    """
    Step 1 (50 Points): Use the heuristic 'h' to head straight for the goal.
    
    Instructions:
    1. Initialize 'queue' as a PriorityQueue().
    2. Start node priority = h[start_node.state].
    3. Put (priority, start_node) into the queue.
    4. Maintain a 'visited' set.
    """
    # TODO: YOUR CODE HERE
    pass

def astar_search(problem, h):
    """
    Step 2 (50 Points): Combine path cost (g) and heuristic (h).
    
    Instructions:
    1. Initialize 'queue' as a PriorityQueue().
    2. Start node priority = 0 + h[start_node.state].
    3. WHILE queue is not empty:
       - Get cheapest: (f_score, node) = queue.get()
       - IF goal: return node
       - IF not visited:
         - Expand and add children using f = g + h
    """
    # TODO: YOUR CODE HERE
    pass
