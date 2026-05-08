# 🧠 Lab 3: Neural Network Input Layer (Matrix Math)

In this lab, you will implement the "Forward Pass" of a single artificial neuron. You will use **pandas** to handle data ingestion and **NumPy** to perform high-speed matrix multiplication.

This lab focuses on the fundamental linear transformation:  
**z = XW + b**

---

## 📊 Grading Rubric (100 Points Total)

This lab is split into two automated tests (50 points each):

1. **Step 1: Data Conversion (50pts)** - Successfully reading the CSV into a pandas DataFrame and converting the features into a NumPy matrix `X`.
2. **Step 2: Matrix Logic (50pts)** - Correctly implementing the dot product using the `@` operator, adding the bias, and applying the step activation.

---

## 📋 Your Task

1.  **Open** `neuron_lab.py`.
2.  **Load Data:** Use `pd.read_csv()` to load `sensor_data.csv`.
3.  **Convert:** Transform the DataFrame into a NumPy array named `X`.
4.  **Compute:** Implement the formula `z = X . W + b`. 
    *   *Note: You must use the '.dot() function to compute X.W*
5.  **Activate:** Apply a step activation function. If an element in `z` is greater than 0, the output should be `1`. Otherwise, it should be `0`.

---

## 🛠 Command Line Workflow

### 1. Clone your repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Test Locally
You can check your progress by running the test script stages:
```bash
# Test Data Loading/Conversion
python3 test_lab3.py 1

# Test Mathematical Logic
python3 test_lab3.py 2
```

### 3. Submit
```bash
git add agent.py
git commit -m "Completed Lab 3 Matrix Math"
git push origin main
```

---

## ⚠️ Requirements
- **No For Loops:** You must use vectorized NumPy operations. Manual loops will result in a point deduction.
- **Python 3.5+:** Ensure you are using a version of Python that supports the `@` operator.
