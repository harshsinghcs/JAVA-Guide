![JOIN](https://img.shields.io/badge/JOIN-green?style=flat-square)


# ✅ **SQL Joins Notes**

Joins are used to combine rows from two or more tables based on a **related column** (usually a primary key ↔ foreign key relation).

---

## 🔹 1. **INNER JOIN**

* Returns only the rows that have **matching values** in both tables.
* **Most common join**.

```sql
SELECT u.name, o.amount
FROM users u
INNER JOIN orders o 
ON u.id = o.user_id;
```

✅ Only users who have placed orders will appear.

---

## 🔹 2. **LEFT JOIN (LEFT OUTER JOIN)**

* Returns **all rows from the left table**, plus matched rows from the right table.
* If there is no match, right side columns become **NULL**.

```sql
SELECT u.name, o.amount
FROM users u
LEFT JOIN orders o 
ON u.id = o.user_id;
```

✅ Shows **all users**, even those who haven’t placed an order (order amount = NULL).

---

## 🔹 3. **RIGHT JOIN (RIGHT OUTER JOIN)**

* Returns **all rows from the right table**, plus matched rows from the left table.
* If no match, left side columns become **NULL**.

```sql
SELECT u.name, o.amount
FROM users u
RIGHT JOIN orders o 
ON u.id = o.user_id;
```

✅ Shows **all orders**, even if some don’t match any user (user name = NULL).

---

## 🔹 4. **FULL JOIN (FULL OUTER JOIN)**

* Returns **all rows from both tables**.
* Matched rows appear once; unmatched rows have NULLs.
* **Not directly supported in MySQL** → must emulate using `UNION`.

```sql
SELECT u.name, o.amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.amount
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

✅ Shows everything: all users + all orders, including unmatched ones.

---

## 🔹 5. **CROSS JOIN**

* Produces a **Cartesian product** (every row from table A × every row from table B).
* No `ON` condition required.

```sql
SELECT u.name, o.amount
FROM users u
CROSS JOIN orders o;
```

✅ If users = 3 and orders = 4 → result = 12 rows.

---

## 🔹 6. **SELF JOIN**

* A table joined with **itself**.
* Useful for hierarchical data (employees, managers).

```sql
SELECT e1.name AS Employee, e2.name AS Manager
FROM employees e1
INNER JOIN employees e2 
ON e1.manager_id = e2.id;
```

✅ Shows employees and their managers from the **same table**.

---

## 🔹 7. **NATURAL JOIN**

* Joins automatically on **columns with the same name**.
* ⚠️ Risky → if unwanted same column exists, it may join incorrectly.

```sql
SELECT * 
FROM users
NATURAL JOIN orders;
```

---

## 📊 Summary Table

| Join Type   | Returns                                                          |
| ----------- | ---------------------------------------------------------------- |
| **INNER**   | Only matching rows in both tables                                |
| **LEFT**    | All rows from left table + matching right table rows, else NULL  |
| **RIGHT**   | All rows from right table + matching left table rows, else NULL  |
| **FULL**    | All rows from both tables, matched or not (UNION in MySQL)       |
| **CROSS**   | Cartesian product (all combinations)                             |
| **SELF**    | Joins table with itself (useful in hierarchy relations)          |
| **NATURAL** | Auto-join on same column names (avoid in production for clarity) |

---

👉 Pro tip for interviews:

* Use **INNER JOIN** when you only want matches.
* Use **LEFT JOIN** when left table is primary and you don’t want to lose its data.
* **FULL JOIN** is rare in MySQL (use `UNION`).

---