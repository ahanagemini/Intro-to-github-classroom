# Assignment: Alpha-Beta Pruning Optimization

## The Goal
Optimize your working Minimax code by adding `alpha` and `beta` boundaries. The goal is to dynamically cut off branches of the tree as soon as you mathematically prove they cannot affect the final outcome. 

## Grading (100 Points Total)
Your code must pass two separate test criteria:
1. **Test Case 1 (50 Points):** Basic pruning detection. 
   - Command: `python test_alphabeta.py 1`
2. **Test Case 2 (50 Points):** Multi-cave pruning and edge case evaluation.
   - Command: `python test_alphabeta.py 2`

**Note:** Unlike the Minimax lab, these test cases will fail if your `visited` node list contains nodes that should have been pruned!
