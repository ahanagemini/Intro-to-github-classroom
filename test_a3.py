import sys, os, pandas as pd, numpy as np
from data_prep import clean_and_prepare_data, plot_histogram, plot_scatter

def run_test(step):
    # Setup: Ensure raw_data.csv exists
    if not os.path.exists('raw_data.csv'):
        print("❌ Error: raw_data.csv missing")
        sys.exit(1)

    df = clean_and_prepare_data('raw_data.csv')
    
    if step == "1": # 20 pts
        assert not df['Age'].isnull().any(), "Age still has NaNs"
    elif step == "2": # 20 pts
        assert len(df) == 3, f"Expected 3 rows after dropna, got {len(df)}"
    elif step == "3": # 20 pts
        assert np.isclose(df['Fare'].mean(), 0, atol=1e-7), "Mean of Fare is not 0"
    elif step == "4": # 20 pts
        assert any('Embarked_' in col for col in df.columns), "No One-Hot columns found"
    elif step == "5": # 10 pts
        if os.path.exists('age_hist.png'): os.remove('age_hist.png')
        plot_histogram(df)
        assert os.path.exists('age_hist.png'), "age_hist.png not found"
    elif step == "6": # 10 pts
        if os.path.exists('age_fare_scatter.png'): os.remove('age_fare_scatter.png')
        plot_scatter(df)
        assert os.path.exists('age_fare_scatter.png'), "age_fare_scatter.png not found"
        
    print(f"✅ Step {step} Passed")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_test(sys.argv)
