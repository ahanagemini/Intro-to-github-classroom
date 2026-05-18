import numpy as np
from sklearn.linear_model import LinearRegression

def euclidean_distance(x1, x2):
    """Calculates the Euclidean distance between two vectors."""
    ## TODO: Implement Euclidean distance formula
    pass

def knn_predict(X_train, y_train, X_query, k=3):
    """Predicts continuous targets using custom k-NN logic."""
    predictions = []
    for q in X_query:
        ## TODO: 1. Calculate distances from q to all vectors in X_train
        ## TODO: 2. Get indices of the k smallest distances
        ## TODO: 3. Average the target values of those k neighbors
        pass
    return np.array(predictions).reshape(-1, 1)

def train_and_predict_linear(X_train, y_train, X_test):
    """Fits a linear regression model using MSE criteria and predicts."""
    ## TODO: 1. Instantiate the LinearRegression model
    ## TODO: 2. Fit the model using X_train and y_train
    ## TODO: 3. Return predictions for X_test
    pass

def mean_squared_error(y_true, y_pred):
    """Calculates the mean squared error metric."""
    ## TODO: Compute and return MSE
    pass
