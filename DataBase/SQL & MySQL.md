# ✅ **SQL and MySQL Notes**
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

---

## 🔹 What is SQL?

**SQL (Structured Query Language)** is a standard language for accessing and manipulating relational databases.

### ✅ Uses of SQL:

* Querying data
* Inserting, updating, and deleting records
* Creating and modifying database schemas
* Managing permissions

---

## 🔹 What is MySQL?

**MySQL** is an open-source **Relational Database Management System (RDBMS)** based on SQL. It's widely used with web applications (e.g., PHP + MySQL, Java Spring Boot + MySQL).

---

## 🗂️ Types of SQL Statements

| Category | Keywords                                        |
| -------- | ----------------------------------------------- |
| **DDL**  | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` |
| **DML**  | `INSERT`, `UPDATE`, `DELETE`                    |
| **DQL**  | `SELECT`                                        |
| **DCL**  | `GRANT`, `REVOKE`                               |
| **TCL**  | `COMMIT`, `ROLLBACK`, `SAVEPOINT`               |

---

## 🔸 Data Types in MySQL

| Category    | Examples                                        |
| ----------- | ----------------------------------------------- |
| Numeric     | `INT`, `BIGINT`, `FLOAT`, `DECIMAL`             |
| Date & Time | `DATE`, `DATETIME`, `TIMESTAMP`, `TIME`, `YEAR` |
| String      | `VARCHAR`, `CHAR`, `TEXT`, `BLOB`               |

---

## 🔸 DDL Commands (Data Definition Language)

*Used to define or change the structure of the database (tables, schema, etc.).*

### 🔹 `CREATE` – Creates new tables, databases, or objects.

```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 🔹 `ALTER` – Modifies an existing table (add, delete, or modify columns).

```sql
ALTER TABLE users ADD COLUMN age INT;
```

### 🔹 `DROP` – Deletes an existing table or database permanently.

```sql
DROP TABLE users;
```

### 🔹 `TRUNCATE` – Removes all records from a table but keeps the structure.

```sql
TRUNCATE TABLE users;
```

---

## 🔸 DML Commands (Data Manipulation Language)

*Used to insert, modify, or delete data inside tables.*

### 🔹 `INSERT` – Adds new records into a table.

```sql
INSERT INTO users (name, email) VALUES ('Harsh', 'harsh@example.com');
```

### 🔹 `UPDATE` – Modifies existing records in a table.

```sql
UPDATE users SET name = 'Harsh Singh' WHERE id = 1;
```

### 🔹 `DELETE` – Removes records from a table.

```sql
DELETE FROM users WHERE id = 1;
```

---

## 🔸 DQL Command (Data Query Language)

*Used to retrieve data from the database.*

### 🔹 `SELECT` – Fetches records from one or more tables.

**Basic:**

```sql
SELECT * FROM users;
```

**With WHERE clause (filtering):**

```sql
SELECT * FROM users WHERE age > 25;
```

**Sorting results:**

```sql
SELECT * FROM users ORDER BY name ASC;
```

**Selecting specific columns:**

```sql
SELECT name, email FROM users WHERE email LIKE '%gmail.com';
```

**Using Aggregate Functions (summary data):**

```sql
SELECT COUNT(*), AVG(age), MAX(age) FROM users;
```


---

## 🔸 Constraints

| Constraint    | Description                             |
| ------------- | --------------------------------------- |
| `PRIMARY KEY` | Uniquely identifies each row            |
| `FOREIGN KEY` | References primary key of another table |
| `UNIQUE`      | Ensures unique values                   |
| `NOT NULL`    | Prevents NULL values                    |
| `CHECK`       | Validates data based on a condition     |
| `DEFAULT`     | Assigns default value                   |

---

## 🔸 Joins
[![JOIN](https://img.shields.io/badge/JOIN-green?style=flat-square)](/DataBase/joins.md)


| Type           | Description & Syntax     |
| -------------- | ------------------------ |
| **INNER JOIN** | Returns matching records |

```sql
SELECT u.name, o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

\| **LEFT JOIN** | All from left + matched right |
\| **RIGHT JOIN**| All from right + matched left |
\| **FULL JOIN** | All from both sides (not in MySQL, emulate with UNION) |

---

## 🔸 GROUP BY and HAVING

```sql
SELECT age, COUNT(*) 
FROM users 
GROUP BY age 
HAVING COUNT(*) > 1;
```

---

## 🔸 Subqueries

```sql
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE amount > 1000);
```

---

## 🔸 Indexes

```sql
CREATE INDEX idx_email ON users(email);
```

---

## 🔸 Views

```sql
CREATE VIEW user_summary AS
SELECT name, email FROM users;
```

---

## 🔸 Transactions

```sql
START TRANSACTION;
UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;  -- or ROLLBACK;
```

---

## 🔸 Stored Procedure

```sql
DELIMITER //
CREATE PROCEDURE GetAllUsers()
BEGIN
  SELECT * FROM users;
END //
DELIMITER ;
```

---

## 🔸 MySQL Admin Commands

| Task               | Command                    |
| ------------------ | -------------------------- |
| Show all databases | `SHOW DATABASES;`          |
| Use DB             | `USE db_name;`             |
| Show tables        | `SHOW TABLES;`             |
| Describe table     | `DESC table_name;`         |
| Create DB          | `CREATE DATABASE db_name;` |
| Drop DB            | `DROP DATABASE db_name;`   |

---

## 🔸 Best Practices

* Always use `WHERE` with `DELETE` or `UPDATE` to avoid full-table changes.
* Use `LIMIT` with `SELECT` for large tables.
* Use `Prepared Statements` to avoid SQL injection (esp. in Java).
* Normalize database to avoid redundancy.