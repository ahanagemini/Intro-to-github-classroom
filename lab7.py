import numpy as np
import sympy as sp

# ==========================================
# Task 1: Manual Calculation Sandbox
# ==========================================
def loss_function(w1, w2):
    """Formula: L(w1, w2) = w1^2 + 3 * w2^2"""
    return w1**2 + 3 * (w2**2)

def compute_gradient_manual(w1, w2):
    """
    LAB TASK 1: Hardcode your hand-derived analytical partial derivatives.
    Returns a numpy array [dw1, dw2].
    """
    # TODO: Replace with your derived equations
    # ---- STUDENT CALCULUS LIVE-coding IMPLEMENTATION HERE ----
    dw1 = 0.0
    dw2 = 0.0
    # -----------------------------------------------------------
    return np.array([dw1, dw2])

# ==========================================
# Task 2: SymPy Symbolic Verification Engine
# ==========================================
def compute_gradient_and_critical_with_sympy():
    """
    LAB TASK 2: Use SymPy to symbolically compute the gradient 
    and locate the critical point of the loss function.
    
    Instructions:
    1. Define 'w1' and 'w2' as SymPy symbols.
    2. Define the loss equation: w1**2 + 3*w2**2
    3. Use sp.diff() to find the partial derivatives.
    4. Use sp.solve() to find where both derivatives equal 0.
    
    Returns:
        tuple: (deriv_w1, deriv_w2, critical_point_dict)
    """
    # TODO: Complete the SymPy pipeline below
    # ---- STUDENT SYMPY IMPLEMENTATION HERE ----
    # 1. Define symbols
    w1, w2 = None, None 
    
    # 2. Define expression
    loss_expr = None 
    
    # 3. Differentiate symbolically
    deriv_w1 = None 
    deriv_w2 = None 
    
    # 4. Solve system of equations for critical points: [deriv_w1, deriv_w2]
    critical_point_dict = None 
    # -------------------------------------------
    
    return deriv_w1, deriv_w2, critical_point_dict
