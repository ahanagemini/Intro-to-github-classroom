# Assignment 01: Intro to GitHub Classroom

The goal of this assignment is to practice the basic Git workflow: **Clone, Edit, Commit, and Push.**

---

## 🚀 Part 1: Setup
1. **Accept the Assignment:** Click the invite link provided in class.
2. **Open your Repo:** Once GitHub creates it, click the link to go to your personal repository.
3. **Copy the URL:** Click the green **Code** button and copy the HTTPS link.

---

## 💻 Part 2: Terminal Commands

Open your terminal or command prompt and run these commands in order:

### 1. Clone the repository
```bash
git clone <PASTE_YOUR_URL_HERE>
cd <YOUR_REPO_NAME>
```

### 2. Make your changes
*   Create a new file called `hello.txt`
*   Open the file `hello.txt` in your text editor (VS Code, Notepad, etc.).
*   Type your **Full Name** and **GitHub Username**.
*   **Save the file.**

### 3. Stage and Commit
```bash
# Check that your change was detected
git status

# Prepare the file for upload
git add hello.txt

# Create a permanent save point
git commit -m "Completed first assignment"
```

### 4. Push to GitHub
```bash
git push origin main
```

---

## ✅ Part 3: Verify Your Submission
1. Go back to your repository page on **GitHub.com**.
2. **Refresh the page.**
3. Open `hello.txt`. If your name is there, you are **finished!**

---

## 🆘 Troubleshooting

**"Git doesn't know who I am"**
If you get an error about your identity, run these two commands:
* `git config --global user.email "your_email@example.com"`
* `git config --global user.name "Your Name"`

**"Permission Denied"**
Ensure you have set up a **Personal Access Token (PAT)** or an **SSH Key**. GitHub no longer accepts your standard password in the terminal.

**"Main vs Master"**
If `push origin main` fails, try:
`git push origin master`
