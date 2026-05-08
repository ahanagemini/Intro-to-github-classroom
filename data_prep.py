import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clean_and_prepare_data(filename):
    """
    Reads a CSV and performs imputation, cleaning, 
    standardization, and encoding.
    """
    df = pd.read_csv(filename)

    # Step 1: TODO: Fill missing Age values with the mean
    
    # Step 2: TODO: Drop rows where 'Fare' or 'Embarked' is missing
    
    # Step 3: TODO: Standardize 'Fare' column: (x - mean) / std
    
    # Step 4: TODO: One-Hot Encode 'Embarked' using pd.get_dummies()
    df_final = None 
    
    return df_final

def plot_histogram(df):
    """
    TODO: Create a histogram of the 'Age' column.
    Save as 'age_hist.png' and close the plot.
    """
    pass

def plot_scatter(df):
    """
    TODO: Create a scatter plot of 'Age' vs 'Fare'.
    Save as 'age_fare_scatter.png' and close the plot.
    """
    pass

if __name__ == "__main__":
    df_clean = clean_and_prepare_data('raw_data.csv')
    if df_clean is not None:
        plot_histogram(df_clean)
        plot_scatter(df_clean)
        print("Processing and plotting complete.")
