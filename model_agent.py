import time

# Internal state: Tracks room status and the last action taken
# Do not modify this dictionary structure.
state = {'A': None, 'B': None, 'last_action': None}

def ModelBasedVacuumAgent(percept):
    """
    Input: percept - A tuple (location, status)
    Output: action - 'Suck', 'Left', 'Right', or 'Wait'
    """
    global state
    location, status = percept
    
    # 1. Update the state with the current perception (Room A or B)
    state[location] = status

    # 2. Memory Decay Logic:
    # If the last action taken was 'Wait', we must assume our knowledge 
    # of the OTHER room is now out of date. 
    # Set the status of the room the agent is NOT in back to None.
    if state['last_action'] == 'Wait':
        # TODO: Identify the other room and set its state to None
        pass

    # 3. Decision Logic:
    # TODO: Implement the following rules:
    # - If BOTH rooms A and B are 'Clean' in the state:
    #     - Print "All clean. Waiting..."
    #     - time.sleep(5)
    #     - return 'Wait'
    # - If current status is 'Dirty', return 'Suck'
    # - If current location is 'A', return 'Right'
    # - If current location is 'B', return 'Left'

    action = None # Remove this line. Your decision logic needs to set the value of variable action
    
    # Record this action in the state for the next turn
    state['last_action'] = action
    return action
