# Lab Module: Analytical Gradients & SymPy Symbolic Optimization

In this lab, you will manually implement the gradients of an AI loss function and verify your work programmatically using symbolic algebra.

## 📐 The Loss Landscape
We are optimizing the following multi-variable polynomial surface:
$$L(w_1, w_2) = w_1^2 + 3w_2^2$$

## 🛠️ Tasks

### Task 1: Manual Calculus Coding
Open `lab_gradient_engine.py`. Implement your hand-derived equations inside `compute_gradient_manual(w1, w2)` ($\frac{\partial L}{\partial w_1} = 2w_1$, $\frac{\partial L}{\partial w_2} = 6w_2$).

### Task 2: Automated SymPy Code
Complete `compute_gradient_and_critical_with_sympy()`. Use `sp.symbols`, `sp.diff`, and `sp.solve` to programmatically extract the derivatives and locate the system's stationary bounds.

## 🧪 Running Terminal Tests
Verify your code using your terminal command line arguments:
```bash
# Test manual gradient at origin
python test_lab.py 1

# Test manual gradient in quadrants
python test_lab.py 2

# Test SymPy derivation and solver execution
python test_lab.py 3
```
