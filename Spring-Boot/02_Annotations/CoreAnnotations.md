````markdown
# Core Annotations in Git

Git itself doesn’t have "annotations" like Java or Spring, but in Git terminology, 
we use **annotations** mostly in the context of **annotated tags**.

---

## 🔹 Annotated Tags
- Annotations are used to **tag a specific commit** with extra metadata.
- Contains: 
  - Tagger name & email
  - Date
  - Message
  - Optional GPG signature (for verification)

### Create an Annotated Tag
```bash
git tag -a v1.0 -m "Version 1.0 release"
````

### View Tags

```bash
git tag
git show v1.0
```

### Push Tags to Remote

```bash
git push origin v1.0
```

---

## 🔹 Lightweight vs Annotated Tags

| Type            | Description                              | Metadata Included? |
| --------------- | ---------------------------------------- | ------------------ |
| **Lightweight** | Just a pointer to a commit               | ❌ No               |
| **Annotated**   | Contains message, tagger info, date, GPG | ✅ Yes              |

---

## 🔹 When to Use?

* Use **lightweight tags** for temporary bookmarks.
* Use **annotated tags** for official release versions.



