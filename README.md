# Assignment 8: Matrix Gradient Descent with Standalone Bias

## Objectives
* Implement Batch Gradient Descent using a feature weight matrix `w` and a standalone scalar bias `w0`.
* Compute predictions using matrix multiplication (`@`) combined with the scalar bias.
* Individually update parameters using the exact summation formulas from Slide 16.

## Mathematical Formulas
$$w_0 \leftarrow w_0 + \alpha_{w0} \sum_{j=1}^{N} (y_j - \hat{y}_j)$$
$$w_1 \leftarrow w_1 + \alpha_{w} \sum_{j=1}^{N} (y_j - \hat{y}_j) \cdot x_j$$

## Repository Structure
* `gradient_descent_lab.py`: Student template file.
* `test_gradient.py`: Custom command-line testing harness.

## Instructions
Execute the test harness with different arguments to verify individual portions:
```bash
python test_gradient.py 1  # Test Case 1: Matrix Prediction
python test_gradient.py 2  # Test Case 2: Explicit Slide Update Rules
python test_gradient.py 3  # Test Case 3: Optimization Convergence
```
