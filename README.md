# 📊 Assignment 4: Data Preparation & Visualization

Prepare a raw, "dirty" dataset for a machine learning model and verify the results visually using exploratory data analysis (EDA).

---

## 📊 Grading Rubric (100 Points Total)

This assignment is autograded across 6 stages:
1. **Step 1: Imputation (20pts)** - Fill missing `Age` with the mean.
2. **Step 2: Cleaning (20pts)** - Drop rows missing `Fare` or `Embarked`.
3. **Step 3: Normalization (20pts)** - Standardize `Fare` (mean=0, std=1).
4. **Step 4: Encoding (20pts)** - One-Hot Encode the `Embarked` column.
5. **Step 5: Histogram (10pts)** - Generate `age_hist.png`.
6. **Step 6: Scatter Plot (10pts)** - Generate `age_fare_scatter.png`.

---

## 🛠 Command Line Workflow

### 1. Run Local Tests
You can check your progress by running the test script stages individually:
```bash
python3 test_assignment.py 1
python3 test_assignment.py 2
python3 test_assignment.py 3
python3 test_assignment.py 4
python3 test_assignment.py 5
python3 test_assignment.py 6
```

### 2. Submit Your Work
```bash
git add data_prep.py
git commit -m "Finalized data prep and EDA plots"
git push origin main
```

---

## ⚠️ Requirements
- **No For Loops:** Use pandas built-in functions (e.g., `.fillna()`, `.dropna()`, `pd.get_dummies()`).
- **Close Plots:** Always use `plt.close()` after saving images to avoid overlapping data in your files.
