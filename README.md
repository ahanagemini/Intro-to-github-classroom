# Assignment 5: Informed Search (Greedy & A*)

This assignment covers **Informed Search** strategies. You will use a heuristic ($h$), which represents the straight-line distance to the goal, to make the search more efficient.

---

### 🛠️ Tasks

#### Step 1: Greedy Search (50 Points)
Implement `greedy_search`.
* **Strategy**: Priority = $h(n)$.
* **Goal**: Expand the node that appears closest to the goal.

#### Step 2: A* Search (50 Points)
Implement `astar_search`.
* **Strategy**: Priority = $g(n) + h(n)$.
* **Goal**: Find the optimal path using both actual cost and the heuristic.

---

### 🧪 How to Test Locally

**To test Greedy (Step 1):**
```bash
python test_assignment6.py 1
```

**To test A* (Step 2):**
```bash
python test_assignment6.py 2
```
