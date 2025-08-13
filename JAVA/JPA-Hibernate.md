# **JPA & Hibernate Notes**
<a href="#">
  <img src="https://img.shields.io/badge/JPA%20%2F%20Hibernate-59666C?style=for-the-badge&logo=hibernate&logoColor=white" alt="JPA / Hibernate" width="300"/>
</a>

---

## **1. Introduction**

* **JPA (Java Persistence API)**:

  * A specification for ORM (Object Relational Mapping) in Java.
  * Maps Java objects to database tables.
  * Standardized API for data persistence.
* **Hibernate**:

  * Popular **implementation of JPA**.
  * Handles SQL generation, caching, and transaction management.

**Key Point:** JPA is **specification**, Hibernate is **framework/implementation**.

---

## **2. JPA vs Hibernate**

| Feature     | JPA                     | Hibernate                                          |
| ----------- | ----------------------- | -------------------------------------------------- |
| Type        | Specification           | Framework / Implementation                         |
| Vendor      | Standardized            | Hibernate ORM Provider                             |
| Features    | Basic ORM mapping       | Advanced features: caching, lazy loading, filters  |
| Portability | High (any JPA provider) | Hibernate specific features may reduce portability |

---

## **3. Core Concepts**

* **Entity**: Java class mapped to a DB table (`@Entity`).
* **Primary Key**: Unique identifier (`@Id`, `@GeneratedValue`).
* **Persistence Unit**: Logical group of entities (defined in `persistence.xml`).
* **Entity Manager**: Interface to perform CRUD operations (`persist`, `merge`, `remove`, `find`).

---

## **4. Annotations**

### **Entity Mapping**

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "username", nullable = false, length = 50)
    private String username;

    private int age;

    // getters and setters
}
```

### **Relationships**

| Relationship | Annotation    | Description                            |
| ------------ | ------------- | -------------------------------------- |
| One-to-One   | `@OneToOne`   | One entity relates to one other entity |
| One-to-Many  | `@OneToMany`  | One entity relates to many entities    |
| Many-to-One  | `@ManyToOne`  | Many entities relate to one entity     |
| Many-to-Many | `@ManyToMany` | Many entities relate to many entities  |

**Example – One-to-Many**

```java
@Entity
public class Department {
    @Id
    private Long id;

    @OneToMany(mappedBy = "department", cascade = CascadeType.ALL)
    private List<Employee> employees;
}
```

---

## **5. Hibernate Features**

* **Automatic Table Creation**: `hibernate.hbm2ddl.auto = update`
* **Lazy & Eager Loading**:

  * `FetchType.LAZY` – Load when needed
  * `FetchType.EAGER` – Load immediately
* **Caching**:

  * First-level cache – Session-level (default)
  * Second-level cache – Across sessions (optional)
* **HQL (Hibernate Query Language)**:

  * Object-oriented query language (works with entities, not tables)

  ```java
  String hql = "FROM User WHERE age > 20";
  Query query = session.createQuery(hql);
  List<User> users = query.list();
  ```

---

## **6. Entity Manager Methods (JPA)**

| Method            | Description                    |
| ----------------- | ------------------------------ |
| `persist(obj)`    | Insert new entity              |
| `merge(obj)`      | Update existing entity         |
| `remove(obj)`     | Delete entity                  |
| `find(Class, id)` | Retrieve entity by primary key |
| `createQuery()`   | Create JPQL / HQL queries      |

---

## **7. Transaction Management**

```java
EntityTransaction transaction = entityManager.getTransaction();
transaction.begin();

entityManager.persist(user);

transaction.commit();
```

* Always wrap CRUD operations in **transactions**.
* Rollback if exceptions occur.

---

## **8. Advantages of JPA/Hibernate**

* Less boilerplate code (no need for manual SQL).
* Database-independent (works with MySQL, Oracle, PostgreSQL, etc.).
* Supports caching & lazy loading for performance.
* Built-in transaction management.
* Clean mapping between objects and relational tables.

---

## **9. Best Practices**

✅ Use **`@Entity` classes** for all tables.
✅ Avoid **eager loading** for large collections.
✅ Use **JPQL / Criteria API** instead of native SQL for portability.
✅ Always **close EntityManager** to avoid memory leaks.
✅ Use **second-level cache** for frequently accessed data.

---

## **10. Common Interview Questions**

1. Difference between JPA and Hibernate.
2. What are EntityManager and Session in Hibernate?
3. Difference between `persist` and `merge`.
4. What is lazy vs eager loading?
5. Explain Hibernate caching levels.
6. How to map One-to-Many and Many-to-Many relationships?
