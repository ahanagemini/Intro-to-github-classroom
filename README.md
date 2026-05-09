# 📐 Assignment 5: Linear Systems & AI Solvers

This assignment applies Linear Algebra to solve systems of equations. You will implement an exact solver for a 2x2 system and a "Normal Equation" solver for an overdetermined AI dataset.

## 📊 Grading Rubric (50 Points Each)

1. **Step 1: Coffee Optimization** - Solve the 2x2 system $Ax = b$ using the inverse method: $x = A^{-1}b$.
2. **Step 2: Grade Prediction** - Implement the **Normal Equation** to learn weights from a dataset and predict a final grade for a new student input.

---

## 📋 Instructions

### Part 1: Coffee Blend (Exact Solver)
In `solve_coffee_blend()`, represent the following system in Matrix $A$ and Vector $b$:
- $10x_1 + 6x_2 = 8$
- $120x_1 + 80x_2 = 100$
Solve for $x$ using `np.linalg.inv()`.

### Part 2: Student Success (Normal Equation)
In `train_and_predict()`, use the **Normal Equation** to find the optimal weights $w$:
- **Formula:** $w = (A^T A)^{-1} A^T b$
- After finding $w$, calculate the prediction for a new student by taking the dot product of the new features and the weights.

---

## 🛠 Command Line Workflow

### 1. Test Locally
```bash
python3 test_assignment5.py 1
python3 test_assignment5.py 2
```

### 2. Submit
```bash
git add solver.py
git commit -m "Completed AI Linear Solver"
git push origin main
```
