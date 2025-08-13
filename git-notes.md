
# 🐙 Git Notes  
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

A concise guide to **Git basics**, workflows, and best practices — perfect for quick reference during development.

---

## 1️⃣ What is Git?

- **Git** is a **distributed version control system** used to track changes in code.
- Maintains a complete history of your project as **commits**.
- Works locally but can sync with **remote repositories** (e.g., GitHub, GitLab, Bitbucket).

---

## 2️⃣ Git Workflow

1. **Working Directory** – Your actual project files.
2. **Staging Area** – Changes marked to be committed.
3. **Repository** – Your local `.git` history database.
4. **Remote Repository** – Hosted version on a server.

---

## 3️⃣ Basic Git Commands

### 🔹 Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list   # View config
````

### 🔹 Create / Clone

```bash
git init                # Initialize Git in current folder
git clone <url>         # Clone a remote repo
```

### 🔹 Add & Commit

```bash
git status              # Show changes
git add file.txt        # Stage specific file
git add .               # Stage all changes
git commit -m "message" # Commit staged changes
```

### 🔹 Branching

```bash
git branch              # List branches
git branch <name>       # Create branch
git checkout <name>     # Switch branch
git checkout -b <name>  # Create + switch branch
git merge <branch>      # Merge into current branch
git branch -d <name>    # Delete branch
```

### 🔹 Remote

```bash
git remote -v                        # View remotes
git remote add origin <url>           # Add remote
git push origin main                  # Push branch
git pull origin main                  # Fetch + merge
git fetch origin                      # Fetch without merging
```

### 🔹 Undo & Reset

```bash
git reset --soft HEAD~1    # Undo commit, keep staged
git reset --mixed HEAD~1   # Undo commit, keep unstaged
git reset --hard HEAD~1    # Undo commit, delete changes
git checkout -- file.txt   # Discard file changes
```

### 🔹 Logs

```bash
git log                     # Full history
git log --oneline --graph   # Compact + visual
git reflog                  # Show HEAD history
```

---

## 4️⃣ Git Revisions & References

* `HEAD` → Current commit
* `HEAD~1` → One commit before HEAD
* `HEAD^` → Parent commit
* `branch-name` → Latest commit on branch
* `tag-name` → Specific tagged commit

---

## 5️⃣ Common Git Workflows

* **Feature Branch Workflow** → Each feature in its own branch.
* **Gitflow Workflow** → Structured `main` + `develop` + feature/release branches.
* **Fork & Pull Request** → Common in open-source projects.

---

## 6️⃣ .gitignore

Tells Git which files/folders to ignore.

```plaintext
node_modules/
*.log
.env
```

---

## 7️⃣ Best Practices

✅ Commit often with clear messages
✅ Pull before pushing to avoid conflicts
✅ Use branches for features & fixes
✅ Keep `.gitignore` updated
✅ Never commit sensitive data

---
