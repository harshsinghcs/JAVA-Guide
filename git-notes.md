# 🐙 **Git Notes**

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)

A **developer-friendly quick reference** to Git basics, workflows, and best practices — perfect for daily use and interview prep.

---

## 1️⃣ **What is Git?**

* **Git** is a **distributed version control system** for tracking changes in source code.
* Stores project history as **commits**.
* Works **locally** and can sync with **remote repositories** like GitHub, GitLab, and Bitbucket.

---

## 2️⃣ **Git Workflow**

1. **Working Directory** → Your project files.
2. **Staging Area** → Changes marked for commit.
3. **Repository** → Local `.git` history.
4. **Remote Repository** → Hosted version on a server.

---

## 3️⃣ **Basic Git Commands**

### 🔹 **Setup**

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list
```

### 🔹 **Create / Clone**

```bash
git init                 # Initialize Git in folder
git clone <url>          # Clone remote repo
```

### 🔹 **Add & Commit**

```bash
git status               # Show changes
git add file.txt         # Stage specific file
git add .                # Stage all changes
git commit -m "message"  # Commit staged changes
```

### 🔹 **Branching**

```bash
git branch               # List branches
git branch <name>        # Create branch
git checkout <name>      # Switch branch
git checkout -b <name>   # Create + switch
git merge <branch>       # Merge into current
git branch -d <name>     # Delete branch
```

### 🔹 **Remote**

```bash
git remote -v                        # View remotes
git remote add origin <url>           # Add remote
git push origin main                  # Push branch
git pull origin main                  # Fetch + merge
git fetch origin                      # Fetch only
```

### 🔹 **Undo & Reset**

```bash
git reset --soft HEAD~1    # Undo commit, keep staged
git reset --mixed HEAD~1   # Undo commit, keep unstaged
git reset --hard HEAD~1    # Undo commit, delete changes
git checkout -- file.txt   # Discard file changes
```

### 🔹 **Logs**

```bash
git log                     # Full history
git log --oneline --graph   # Compact + visual
git reflog                  # HEAD movement history
```

---

## 4️⃣ **Git Revisions & References**

* `HEAD` → Current commit
* `HEAD~1` → One commit before HEAD
* `HEAD^` → Parent commit
* `branch-name` → Latest commit on that branch
* `tag-name` → Specific tagged commit

---

## 5️⃣ **Popular Git Workflows**

* **Feature Branch Workflow** → Each feature in its own branch.
* **Gitflow Workflow** → `main` + `develop` + feature/release branches.
* **Fork & Pull Request** → Common in open-source projects.

---

## 6️⃣ **`.gitignore`**

Tell Git which files/folders to ignore:

```plaintext
node_modules/
*.log
.env
```

---

## 7️⃣ **Best Practices**

✅ Commit often with clear messages
✅ Pull before pushing to avoid conflicts
✅ Use branches for features/fixes
✅ Keep `.gitignore` updated
✅ Never commit sensitive info

---

## 8️⃣ **Interview Spotlight — Resolving Merge Conflicts**

💬 **Sample Answer**:

> A Git conflict occurs when changes in different branches affect the same part of a file.
> I resolve it by:
>
> 1. Running `git status` to identify conflicted files.
> 2. Opening the file and reviewing conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
> 3. Choosing to keep my changes, incoming changes, or merge both.
> 4. Removing markers, saving, then running `git add <file>` to mark resolved.
> 5. Committing the changes (`git commit`) or continuing (`git rebase --continue`).
>
> If the conflict is complex, I use a merge tool or IDE helper. If I need to cancel, I run `git merge --abort`.

✅ **Extra Tip for Interviews**:

* “I pull frequently to reduce conflicts.”
* “I test the project after resolving to ensure no breakages.”

---

This version is:

* **Tighter & cleaner** — no redundancy.
* **Interview-ready** — clear answers for common Git questions.
* **Easy to scan** — perfect for quick lookup while coding.
