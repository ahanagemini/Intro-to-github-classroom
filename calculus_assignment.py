import numpy as np
# Import the validated functions developed during the in-class lab component
from lab7 import loss_function, compute_gradient_manual

def gradient_descent(start_w1, start_w2, alpha, num_iterations):
    """
    ASSIGNMENT TASK 1: Implement the explicit multivariable update loop.
    Follow the mathematical update rule detailed on Slide 30:
    w <- w - alpha * grad(L)
    
    Args:
        start_w1 (float): Initial starting coordinate for weight parameter 1.
        start_w2 (float): Initial starting coordinate for weight parameter 2.
        alpha (float): The learning rate hyperparameter (step size).
        num_iterations (int): Total number of optimization steps to execute.
        
    Returns:
        tuple: (weight_history, loss_history)
            - weight_history: A numpy array of shape (num_iterations+1, 2) tracking coordinates.
            - loss_history: A numpy array of shape (num_iterations+1,) tracking scalar loss values.
    """
    # Initialize the coordinate parameters as a float vector array
    w = np.array([float(start_w1), float(start_w2)])
    
    # Pre-populate history trackers with initial parameters and baseline loss values
    weight_history = [w.copy()]
    loss_history = [loss_function(w[0], w[1])]
    
    for _ in range(num_iterations):
        # 1. Fetch the analytical gradient vector from your verified lab engine
        grad = compute_gradient_manual(w[0], w[1])
        
        # 2. Scale the update steps using the learning rate parameter (alpha)
        # TODO: Replace the line below with your active parameter update vector step.
        # ---- STUDENT OPTIMIZATION STEP IMPLEMENTATION HERE ----
        pass
        # ------------------------------------------------------
        
        # Log active iterations for the visual and automated testing suites
        weight_history.append(w.copy())
        loss_history.append(loss_function(w[0], w[1]))
        
    return np.array(weight_history), np.array(loss_history)
