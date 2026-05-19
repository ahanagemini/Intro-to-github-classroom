# Lab: Classification Analysis with k-NN and Logistic Regression

## Objectives
* Implement a $k$-Nearest Neighbors ($k$-NN) discrete classifier from scratch.
* Perform custom majority voting using explicit for loops and primitive counts without specialized numpy methods (like `np.bincount` or `np.argmax`).
* Train and evaluate a parametric linear classifier using `scikit-learn`'s `LogisticRegression`.

## Repository Structure
* `classification_lab.py`: Student template file.
* `test_lab.py`: Custom command-line testing harness with 4 discrete test options.

## Instructions
1. Open `classification_lab.py` and fill in the code blocks marked `## TODO`.
2. Run your local test harness using explicit task IDs:

```bash
python test_lab.py 1  # Test Case 1: Euclidean Distance Function
python test_lab.py 2  # Test Case 2: k-NN Neighborhood Majority Voting
python test_lab.py 3  # Test Case 3: Logistic Regression Model Fitting
python test_lab.py 4  # Test Case 4: Classification Accuracy Evaluation
```
