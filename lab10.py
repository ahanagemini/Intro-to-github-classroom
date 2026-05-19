import numpy as np
from sklearn.linear_model import LogisticRegression

def euclidean_distance(x1, x2):
    """Calculates the Euclidean distance between two numeric vectors."""
    ## TODO: Implement Euclidean distance formula
    pass

def knn_classify(X_train, y_train, X_query, k=3):
    """
    Predicts categorical class labels (0 or 1) for query points using k-NN majority voting.
    Processes ties and label counts manually using standard loop iterations.
    """
    predictions = []
    for q in X_query:
        # 1. TODO: Calculate distances from query point to all training points
        distances = []
       
            
        # 2. TODO: Extract indices of the k smallest distances
       
        
        # 3. TODO: Explicitly count class frequencies among the k nearest neighbors using a loop
        count_0 = 0
        count_1 = 0
        
            
        # 4. Resolve the majority label using explicit conditional checks
        ## TODO: Compare counts and append the winning integer label (0 or 1) to predictions
       
        
    return np.array(predictions)

def train_and_predict_logistic(X_train, y_train, X_test):
    """Instantiates a LogisticRegression model, fits it to the training data, and predicts labels."""
    ## TODO: 1. Instantiate the LogisticRegression model
    ## TODO: 2. Fit the model using X_train and y_train
    ## TODO: 3. Return discrete class predictions for X_test
    pass

def accuracy_score(y_true, y_pred):
    """Calculates the classification accuracy score using an explicit counting loop."""
    ## TODO: Compute accuracy by iterating and checking matches between arrays manually
    pass
