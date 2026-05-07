# 🤖 Assignment: Advanced Model-Based Agent (Memory Decay)

In this assignment, you will upgrade your Vacuum Agent to be **Model-Based**. Unlike a reflex agent, this agent maintains an internal "model" of the world to track which rooms are clean, even if it isn't currently inside them.

Additionally, you will implement **Information Decay**: if the agent waits for a period of time, it must assume its knowledge of the other room is potentially out of date and reset its memory.

---

## 📊 Grading Rubric (100 Points Total)

This assignment is autograded in five steps (20 points each):

1. **Step 1: Basic Suck (20pts)** - Agent returns 'Suck' when the current room A is 'Dirty'.
2. **Step 2: Movement A (20pts)** - Agent moves 'Right' if it is in Room A and the room is 'Clean'.
3. **Step 3: Basic Suck (20pts)** - Agent returns 'Suck' when the current room B is 'Dirty'.
5. **Step 4: Wait Logic (20pts)** - Agent returns 'Wait' and sleeps for 5 seconds if its model shows BOTH rooms are 'Clean'.
6. **Step 5: Memory Decay (20pts)** - If the last action was 'Wait', the agent MUST reset the *other* room status to `None`.

---

## 📋 Your Task

1.  **Open** `agent.py`.
2.  **Update the Model:** Ensure the `state` dictionary is updated with every new percept.
3.  **Implement Memory Decay:** If `state['last_action']` is 'Wait', set the state of the room you are **not** currently in to `None`.
4.  **Implement Decision Logic:** Follow the logic in **Figure 2.12** of the AIMA textbook, but add the requirement that the agent only stops (Waits) when **both** rooms are clean in its model.

---

## 🛠 Command Line Workflow

### 1. Clone your repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Test Locally
You can test each step of your code individually:
```bash
python3 test_agent.py 1
python3 test_agent.py 2
python3 test_agent.py 3
python3 test_agent.py 4
python3 test_agent.py 5
```

### 3. Submit Your Work
```bash
git add agent.py
git commit -m "Completed Advanced Model-Based Agent"
git push origin main
```

---

## 📖 Reference Material
*   **Textbook:** Figure 2.12 (*Artificial Intelligence: A Modern Approach, 4th Edition*).
*   **Logic Link:** [AIMA Figure 2.12 Pseudocode](https://berkeley.edu) (Page 8).

---

## ✅ Submission Checklist
- [ ] My code passes all 5 steps of `test_agent.py`.
- [ ] I have implemented the 5-second `time.sleep()` for the Wait action.
- [ ] My `agent.py` file is visible on the GitHub website.
