# Lab: Recursive Minimax (No Pruning)

## The Scenario
You are a treasure hunter in a two-level game tree:
1. **Level 0 (MAX):** You are at the entrance. You choose which **Cave** to enter.
2. **Level 1 (MIN):** Each cave has a **Guardian**. The guardian chooses which **Chest** you get.
3. **Level 2 (Leaves):** The actual gold values inside the chests.

## The Goal
Implement the recursive `max_value` and `min_value` functions to find the best possible value you can guarantee, assuming the guardian always picks the smallest value chest in their cave.

## Tree Structure Example
A tree represented as `[[3, 5], [2, 100]]` means:
- **Cave 1** contains chests with values **3** and **5**.
- **Cave 2** contains chests with values **2** and **100**.
