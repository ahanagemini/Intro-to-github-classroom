# Homework Assignment: Building the Multi-Variable Optimization Loop

In this assignment, you will build the optimization loop that drives model learning, explore how step size changes based on surface slope, and analyze why certain hyperparameter configurations fail.

## 🛠️ Assignment Setup & Tasks

### Step 1: Copy Your Lab Code
Copy your verified `lab7.py` file from your completed lab workspace directly into this assignment folder directory. Your homework code requires your lab functions to calculate analytical partial derivatives.

### Step 2: Implement the Parameter Optimization Step
Open `calculus_assignment.py` and locate the `gradient_descent(...)` loop block. Replace the placeholder comment with the multi-variable vector update rule covered on **Slide 30**:
$$w \leftarrow w - \alpha \nabla L(w_1, w_2)$$

### Step 3: Run Visualizations
Compile your hyperparameter visual profiles to verify your paths:
```bash
python visualization_tool.py
```
Open the generated `my_optimization_profiles.png` file to check your paths.

## 🧪 Submission Verification Tests
Run the test runner using command-line system arguments to check your implementation:
```bash
# Verify stable convergence path trends
python test_assignment7.py 1

# Verify that step sizes scale down as the slope flattens
python test_assignment7.py 2
```

## 📝 Analytical Report Deliverable
Open `Analysis.md` and complete the engineering review prompts comparing the optimization paths before submitting.
