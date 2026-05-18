import numpy as np

def compute_predictions(X, w, w0):
    """
    Computes predictions using matrix multiplication and a standalone bias.
    X: 2D numpy array of shape (N, 1) containing house sizes.
    w: 1D numpy array of shape (1,) representing the feature weight matrix [w1].
    w0: Float scalar representing the standalone bias.
    Returns a 1D numpy array of predictions of shape (N,).
    """
    ## TODO: Compute predictions using matrix multiplication (X @ w) and adding the bias w0
    pass

def train_gradient_descent(X, y, learning_rate_w=1e-8, learning_rate_w0=1e-4, epochs=20000):
    """
    Runs batch gradient descent over the whole training dataset at once.
    X is shape (N, 1), y is shape (N,).
    """
    N = len(X)
    w = np.zeros(1)
    w0 = 0.0
    
    for epoch in range(epochs):
        # 1. Generate full dataset predictions
        ## TODO: Generate predictions array for the current epoch using X, w, and w0
        preds = None
        
        # 2. Compute error difference vector (y - predictions)
        errors = y - preds
        
        # 3. Apply the exact batch update equations from Slide 16
        ## TODO: Update the bias scalar w0 using the sum of errors
        w0 = None
        
        ## TODO: Update the feature weight matrix w using the sum of errors and features
        w = None
        
    return w, w0
