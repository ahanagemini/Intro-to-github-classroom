# Lab 8: Regression Analysis with k-NN and Linear Models

## Objectives
* Implement a $k$-Nearest Neighbors ($k$-NN) continuous regressor from scratch.
* Train a linear regression model using `scikit-learn` minimizing MSE loss.
* Run targeted verification scenarios using explicit command-line flags.

## Repository Structure
* `regression_lab.py`: Student template file.
* `test_lab.py`: Custom command-line testing harness with 4 distinct test options.

## Instructions
1. Open `regression_lab.py` and fill in the code blocks marked `## TODO`.
2. Run your local test harness using explicit task IDs:

```bash
python test_lab.py 1  # Test Case 1: Euclidean Distance Function
python test_lab.py 2  # Test Case 2: k-NN Neighborhood Selection
python test_lab.py 3  # Test Case 3: Scikit-Learn Model Fitting
python test_lab.py 4  # Test Case 4: Mean Squared Error (MSE) Evaluation
```
