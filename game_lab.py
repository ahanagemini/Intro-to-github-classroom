# List to track the order of exploration
visited = []

def max_value(state):
    """The Maximizer (You)"""
    if isinstance(state, int):
        visited.append(state)
        return state
    
    v = -float('inf')
    for successor in state:
        # TODO: Update v to be the MAX of itself and the result of min_value(successor)
        pass
    return v

def min_value(state):
    """The Minimizer (Guardian)"""
    if isinstance(state, int):
        visited.append(state)
        return state
    
    v = float('inf')
    for successor in state:
        # TODO: Update v to be the MIN of itself and the result of max_value(successor)
        pass
    return v
