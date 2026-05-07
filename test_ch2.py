import sys
from model_agent import ModelBasedVacuumAgent, state

def reset():
    state['A'] = None
    state['B'] = None
    state['last_action'] = None

def step1(): # 20 Points
    reset()
    assert ModelBasedVacuumAgent(('A', 'Dirty')) == 'Suck'
    print("Step 1 Passed")

def step2(): # 20 Points
    reset()
    state['A'] = 'Dirty' # Pre-condition
    ModelBasedVacuumAgent(('A', 'Dirty')) 
    assert ModelBasedVacuumAgent(('A', 'Clean')) == 'Right'
    print("Step 2 Passed")

def step3(): # 20 Points
    reset()
    assert ModelBasedVacuumAgent(('B', 'Dirty')) == 'Suck'
    print("Step 3 Passed")

def step4(): # 20 Points
    reset()
    state['A'] = 'Clean'
    assert ModelBasedVacuumAgent(('B', 'Clean')) == 'Wait'
    print("Step 4 Passed")

def step5(): # 20 Points
    reset()
    state['A'] = 'Clean'
    state['B'] = 'Clean'
    ModelBasedVacuumAgent(('B', 'Clean')) # Trigger the Wait
    ModelBasedVacuumAgent(('B', 'Clean'))
    assert state['A'] is None, "Did not reset Room A after Wait"
    print("Step 5 Passed")

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "1": step1()
    elif arg == "2": step2()
    elif arg == "3": step3()
    elif arg == "4": step4()
    elif arg == "5": step5()
