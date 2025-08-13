# **JDBC – Java Database Connectivity**
<a href="#">
  <img src="https://img.shields.io/badge/JDBC-007396?style=for-the-badge&logo=java&logoColor=white" alt="JDBC" width="120"/>
</a>

---

## **1. Introduction**

* **Definition**: JDBC is an API that allows Java applications to interact with databases.
* **Purpose**:

  * Send SQL queries from Java code to a database.
  * Retrieve and manipulate data from relational databases.
* **Key Point**: JDBC is **database independent** — you can use the same Java code with different databases by changing the driver.

---

## **2. JDBC Architecture**

JDBC follows a **two-tier architecture**:

1. **Java Application** – Your program that contains JDBC code.
2. **JDBC Driver** – Translates Java calls into database-specific calls.

**Flow**:

```
Java Application → JDBC API → JDBC Driver Manager → JDBC Driver → Database
```

---

## **3. JDBC Components**

### **(A) DriverManager**

* Manages a list of database drivers.
* Selects an appropriate driver based on database URL.

### **(B) Driver**

* Interface that all database drivers must implement.
* Converts JDBC calls into DB-specific calls.

### **(C) Connection**

* Represents a connection session with the database.

### **(D) Statement**

* Sends SQL queries to the database.
* Types:

  * **Statement** – For simple queries.
  * **PreparedStatement** – Precompiled queries with parameters (recommended).
  * **CallableStatement** – For executing stored procedures.

### **(E) ResultSet**

* Stores data returned by a `SELECT` query.
* Methods: `next()`, `getString()`, `getInt()`, etc.

---

## **4. JDBC Steps**

### **Basic Example**

```java
import java.sql.*;

class JDBCExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/testdb";
        String user = "root";
        String password = "password";

        try {
            // Step 1: Load Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Step 2: Establish Connection
            Connection con = DriverManager.getConnection(url, user, password);

            // Step 3: Create Statement
            String query = "SELECT * FROM employees";
            Statement stmt = con.createStatement();

            // Step 4: Execute Query
            ResultSet rs = stmt.executeQuery(query);

            // Step 5: Process Results
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " " + rs.getString("name"));
            }

            // Step 6: Close resources
            rs.close();
            stmt.close();
            con.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

## **5. Types of JDBC Drivers**

| Driver Type                   | Description                                        | Example                          | Pros                    | Cons                       |
| ----------------------------- | -------------------------------------------------- | -------------------------------- | ----------------------- | -------------------------- |
| **Type 1** – JDBC-ODBC Bridge | Converts JDBC calls into ODBC calls.               | sun.jdbc.odbc.JdbcOdbcDriver     | Easy to use             | Requires ODBC driver, slow |
| **Type 2** – Native API       | Converts JDBC calls to native DB API calls.        | Oracle OCI driver                | Faster than Type 1      | Requires native library    |
| **Type 3** – Network Protocol | Uses middleware server.                            | net.sourceforge.jtds.jdbc.Driver | Works with multiple DBs | Requires middleware        |
| **Type 4** – Thin Driver      | Pure Java, converts calls directly to DB protocol. | MySQL Connector/J                | Fast, portable          | DB-specific                |

**Best Choice Today:** **Type 4 Driver** (pure Java).

---

## **6. PreparedStatement vs Statement**

| Feature     | Statement                   | PreparedStatement      |
| ----------- | --------------------------- | ---------------------- |
| Compilation | Compiled every time         | Precompiled            |
| Performance | Slower                      | Faster                 |
| Security    | Vulnerable to SQL injection | Prevents SQL injection |
| Parameters  | No                          | Yes (`?` placeholders) |

Example:

```java
String query = "INSERT INTO users (name, age) VALUES (?, ?)";
PreparedStatement ps = con.prepareStatement(query);
ps.setString(1, "Harsh");
ps.setInt(2, 24);
ps.executeUpdate();
```

---

## **7. Handling Transactions**

By default, JDBC uses **auto-commit mode** (commits after each statement).
You can disable auto-commit to handle transactions manually:

```java
con.setAutoCommit(false);
// Execute queries
con.commit();   // Save changes
con.rollback(); // Undo changes if needed
```

---

## **8. Exception Handling**

Common JDBC exceptions:

* `SQLException` – General DB errors.
* `SQLTimeoutException` – Query took too long.
* `SQLSyntaxErrorException` – Wrong SQL syntax.

---

## **9. Best Practices**

✅ Use **PreparedStatement** for queries.
✅ Always close `ResultSet`, `Statement`, `Connection` (or use **try-with-resources**).
✅ Use **connection pooling** (e.g., HikariCP) for better performance.
✅ Handle transactions carefully (disable auto-commit if needed).
✅ Use batch processing for large inserts.

---

## **10. JDBC Interview Questions**

1. What is JDBC?
2. Explain the steps to connect to a database using JDBC.
3. Difference between Statement, PreparedStatement, and CallableStatement.
4. What are JDBC driver types? Which one is best?
5. How do you handle transactions in JDBC?
6. How to prevent SQL injection in JDBC?

---

