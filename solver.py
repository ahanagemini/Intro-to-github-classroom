import pandas as pd
import numpy as np

def solve_coffee_blend():
    """
    Exact 2x2 System:
    10x1 + 6x2 = 8
    120x1 + 80x2 = 100
    
    Task: Solve for x using x = inv(A) @ b
    Return: The solution vector [x1, x2]
    """
    # TODO: Define Matrix A and Vector b
    A = None
    b = None
    
    # TODO: Calculate x using np.linalg.inv() and the @ operator
    x = None
    
    return x

def train_and_predict(csv_file, new_student_features):
    """
    1. Read 'student_success.csv'
    2. Solve for weights 'w' using the Normal Equation: 
       w = inv(A.T @ A) @ A.T @ b
    3. Predict 'Final_Grade' for a new student input.
    """
    # TODO: Load the data into a pandas DataFrame
    df = None
    
    # TODO: Extract Features (A) and Target (b)
    # Hint: A should be the 'Hours_Studied' and 'Practice_Tests' columns
    A = None
    b = None
    
    # TODO: Solve for weights 'w' using the Normal Equation
    w = None
    
    # TODO: Calculate the prediction for the new student
    # Prediction = new_student_features @ weights
    prediction = None
    
    return w, prediction

if __name__ == "__main__":
    # Test the coffee solver
    print("Coffee Solution:", solve_coffee_blend())
    
    # Test the predictor
    new_data = np.array([5, 2]) # 5 hours, 2 practice tests
    weights, grade = train_and_predict('student_success.csv', new_data)
    print(f"Learned Weights: {weights}")
    print(f"Predicted Grade: {grade}")
