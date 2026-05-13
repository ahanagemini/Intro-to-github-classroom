# List to track the order of exploration
visited = []

def max_value(state, alpha, beta):
    """The Maximizer (Updating Alpha)"""
    if isinstance(state, int):
        visited.append(state)
        return state
    
    v = -float('inf')
    for successor in state:
        # Update v by evaluating the child node
        v = max(v, min_value(successor, alpha, beta))
        
        # ---------------------------------------------------------
        # TODO 1: THE BETA PRUNE
        # Look at the AIMA pseudocode. If v relates to beta in a specific way,
        # return v immediately to stop searching remaining branches.
        # Your code here:

        # ---------------------------------------------------------
        
        # TODO 2: UPDATE ALPHA
        # Keep track of the best choice found for MAX so far.
        # Your code here:

        # ---------------------------------------------------------
        
    return v

def min_value(state, alpha, beta):
    """The Minimizer (Updating Beta)"""
    if isinstance(state, int):
        visited.append(state)
        return state
    
    v = float('inf')
    for successor in state:
        # Update v by evaluating the child node
        v = min(v, max_value(successor, alpha, beta))
        
        # ---------------------------------------------------------
        # TODO 3: THE ALPHA PRUNE
        # If v relates to alpha in a specific way, return v immediately
        # to stop searching remaining branches.
        # Your code here:

        # ---------------------------------------------------------
        
        # TODO 4: UPDATE BETA
        # Keep track of the best choice found for MIN so far.
        # Your code here:

        # ---------------------------------------------------------
        
    return v
