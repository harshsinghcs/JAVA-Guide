## 🔹 Internal Git Commands

Git is built on **plumbing commands (low-level)** and **porcelain commands (high-level)**:

### 1. **Plumbing Commands (Internal)**

These are low-level commands that interact directly with Git objects. They’re not commonly used day-to-day but are the foundation of Git.

* `git hash-object` → creates SHA-1/SHA-256 hash of a file and stores it in the object database.
* `git cat-file` → shows content or type of an object (commit, tree, blob).
* `git rev-parse` → parses revision identifiers (e.g., branch names, HEAD, commit SHA).
* `git update-index` → directly updates the staging area (index).
* `git write-tree` → creates a tree object from the index.
* `git commit-tree` → creates a commit object from a tree.
* `git fsck` → checks integrity of Git objects.
* `git reflog` → records all changes to HEAD (internal history).

### 2. **Porcelain Commands (High-level)**

These are user-friendly commands built on top of plumbing commands.

* `git add` → internally uses `git update-index`.
* `git commit` → internally uses `git write-tree` + `git commit-tree`.
* `git checkout` → internally uses `git read-tree` + `git update-index`.
* `git push/pull/fetch` → internally use lower-level pack transfer commands.

---

## 🔹 Example: What happens during `git commit`?

1. `git hash-object` → Git creates a blob object for the file.
2. `git update-index` → Adds file entry into the staging area.
3. `git write-tree` → Creates a tree object from the staging area.
4. `git commit-tree` → Creates a commit object pointing to the tree.
5. Update `HEAD` → Moves the branch pointer to the new commit.

So, **`git commit` is just a wrapper** around these internal commands.

---

✅ **Interview Answer Tip:**
If asked *“What are internal Git commands?”*, you can say:

👉 *“Git has plumbing commands (like `git hash-object`, `git update-index`, `git commit-tree`) that work with Git objects directly. Most of the commands we use daily, like `git add`, `git commit`, and `git push`, are porcelain commands that internally rely on plumbing. For example, `git commit` uses `write-tree` and `commit-tree` under the hood.”*


Good question 👍
When interviewers ask about **internal Git commands**, they usually want to test if you know what’s happening *under the hood* when you use high-level commands like `git commit`, `git merge`, `git rebase`, etc.
