import pandas as pd
import numpy as np

def calculate_neuron_output(csv_file):
    # 1. TODO: Load the data from csv_file into a pandas DataFrame
    df = None 
    
    # 2. TODO: Convert the DataFrame to a NumPy array (X)
    X = None 
    
    # 3. Define Weights (W) and Bias (b)
    W = np.array([0.5, -0.2])
    b = 1.0
    
    # 4. TODO: Calculate z = XW + b 
    # Hint: Use the  .dot() method for multiplication
    z = None 
    
    # 5. TODO: Apply Step Activation
    # Return 1 if z > 0, else 0
    
    return X, z
