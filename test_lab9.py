import sys
import numpy as np
import forward_chaining_lab as lab

def get_lecture_kb():
    # Knowledge base representation matching Slide 28 structure:
    # P => Q; L ^ M => P; B ^ L => M; A ^ P => L; A ^ B => L
    # Known facts: A, B
    KB = {
        'clauses': [
            {'premise': ['P'], 'head': 'Q'},
            {'premise': ['L', 'M'], 'head': 'P'},
            {'premise': ['B', 'L'], 'head': 'M'},
            {'premise': ['A', 'P'], 'head': 'L'},
            {'premise': ['A', 'B'], 'head': 'L'}
        ],
        'symbols_known': ['A', 'B']
    }
    return KB

def run_test_case_1():
    print("--- Running Test Case 1: Base Initialization ---")
    KB = get_lecture_kb()
    
    # Check that code processes an empty/unrelated query without modification errors
    res = lab.pl_fc_entails(KB, 'Z')
    assert res is False, "Initialization test evaluation failure."
    print("[PASS] Test Case 1: Data storage formats match Slide 29 specs.")

def run_test_case_2():
    print("--- Running Test Case 2: Agenda Processing Steps ---")
    # Isolated KB testing a direct 1-step logic inference path
    KB = {
        'clauses': [{'premise': ['A'], 'head': 'B'}],
        'symbols_known': ['A']
    }
    res = lab.pl_fc_entails(KB, 'B')
    assert res is True, "Test Case 2 Failed: Single step agenda update did not trigger return statement."
    print("[PASS] Test Case 2: Popping and evaluation logic works accurately.")

def run_test_case_3():
    print("--- Running Test Case 3: Complete Horn KB Entailment ---")
    KB = get_lecture_kb()
    
    # Query Q should trace true via chain: A ^ B => L -> B ^ L => M -> L ^ M => P -> P => Q
    res_q = lab.pl_fc_entails(KB, 'Q')
    assert res_q is True, "Test Case 3 Failed: Unable to entail 'Q' from lecture graph."
    
    # Query M should also be valid independently
    res_m = lab.pl_fc_entails(KB, 'M')
    assert res_m is True, "Test Case 3 Failed: Unable to entail intermediate goal 'M'."
    print("[PASS] Test Case 3: Full forward chaining search path processed perfectly.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_lab.py [1, 2, or 3]")
        sys.exit(1)
        
    test_case_id = sys.argv
    if test_case_id == "1": run_test_case_1()
    elif test_case_id == "2": run_test_case_2()
    elif test_case_id == "3": run_test_case_3()
    else: sys.exit(1)
