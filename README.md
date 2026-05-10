# Lab 6: Uninformed Search (BFS & UCS)

This lab covers the implementation of **Uninformed Search** strategies based on **AIMA Chapter 3**. You will build an agent that navigates the Romanian map from **Arad** to **Bucharest**.

---

### 🎯 Objectives
* Implement **Breadth-First Search (BFS)** to find the path with the fewest number of cities.
* Implement **Uniform-Cost Search (UCS)** to find the path with the lowest total distance in kilometers.
* Use the **PriorityQueue** and **List** data structures to manage the search queue.

---


### 📂 File Structure
* `search_lab.py`: Your starter code containing the map data and function templates.
* `test_lab6.py`: The autograder script used to verify your solutions.

---

### 🛠️ Tasks

#### Step 1: Breadth-First Search (50 Points)
Complete the `breadth_first_search` function. 
* **Goal**: Find the shallowest path (fewest "hops").
* **Strategy**: Use a regular Python `list` as a FIFO (First-In, First-Out) queue.
* **Expected Result**: Arad -> Sibiu -> Fagaras -> Bucharest (Cost: **450**).

#### Step 2: Uniform-Cost Search (50 Points)
Complete the `uniform_cost_search` function.
* **Goal**: Find the optimal path (cheapest total kilometers).
* **Strategy**: Use the `PriorityQueue` class to always expand the node with the lowest cumulative cost $g(n)$.
* **Expected Result**: Arad -> Sibiu -> Rimnicu -> Pitesti -> Bucharest (Cost: **418**).

---

### 🧪 How to Test Locally

Run the following commands in your terminal to check your work:

**To test BFS (Step 1):**
```bash
python test_lab6.py 1
```

**To test UCS (Step 2):**
```bash
python test_lab6.py 2
```

---

### 📝 Submission
1. Ensure both tests pass locally.
2. `git add .`, `git commit -m "complete lab 6"`, and `git push` your changes.
3. Verify your score on the GitHub Classroom dashboard.
