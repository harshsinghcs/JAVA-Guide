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


## Questions ke answers...!!

### **1. Difference between JPA and Hibernate**

* **JPA (Java Persistence API):**

  * A **specification** (interface) for ORM (Object Relational Mapping).
  * Defines how Java objects map to database tables, but does not provide implementation.
  * Examples of JPA providers: Hibernate, EclipseLink, OpenJPA.

* **Hibernate:**

  * A **framework/implementation** of JPA.
  * Provides actual ORM functionality like SQL generation, caching, dirty checking, etc.
  * Hibernate adds extra features beyond JPA (e.g., `Criteria API`, `Session`, caching strategies).

👉 **Interview Answer:**
*"JPA is just a standard/specification, while Hibernate is an actual ORM framework that implements JPA and also provides additional features."*

---

### **2. EntityManager vs Session in Hibernate**

* **EntityManager (JPA):**

  * Defined by JPA.
  * Provides APIs like `persist()`, `merge()`, `remove()`, `find()`.
  * Thread-safe and works in JPA-compliant way.

* **Session (Hibernate):**

  * Hibernate-specific.
  * Provides APIs like `save()`, `update()`, `saveOrUpdate()`, etc.
  * More powerful with extra features (batch processing, criteria queries, native SQL, etc.).

👉 **Interview Answer:**
*"EntityManager is the JPA standard API, whereas Session is Hibernate’s native API. Internally, Hibernate’s Session implements the JPA EntityManager."*

---

### **3. Difference between `persist()` and `merge()`**

* **persist()**

  * Makes a **transient** entity → **managed**.
  * If the entity already exists, throws `EntityExistsException`.
  * Does **not return** anything.

* **merge()**

  * Copies the state of a **detached** entity into a **managed** entity.
  * Returns the managed instance.
  * Useful when you fetch an entity, modify outside session, then update DB.

👉 **Interview Answer:**
*"Use `persist()` for new entities. Use `merge()` when you already have a detached entity and want to reattach it to persistence context."*

---

### **4. Lazy vs Eager Loading**

* **Lazy Loading (default for collections):**

  * Data is loaded **only when accessed**.
  * Uses proxy objects.
  * Improves performance but can cause `LazyInitializationException` if accessed outside session.

* **Eager Loading:**

  * Data is loaded **immediately with parent entity**.
  * Ensures availability but can cause **performance overhead** (fetching large unnecessary data).

👉 **Interview Answer:**
*"Lazy loads data only when required, improving performance. Eager fetches data immediately, which ensures availability but may load unnecessary data."*

---

### **5. Hibernate Caching Levels**

* **First-Level Cache (Session cache):**

  * Default, enabled automatically.
  * Stores entities within the current `Session`.
  * Cache is cleared when session closes.

* **Second-Level Cache (SessionFactory cache):**

  * Optional, must configure explicitly (Ehcache, Infinispan, etc.).
  * Shared across sessions, improves performance by reducing DB calls.

* **Query Cache:**

  * Caches query results (depends on second-level cache).
  * Stores IDs, not entities.

👉 **Interview Answer:**
*"Hibernate has 3 levels of caching: first-level (session-specific, mandatory), second-level (sessionFactory-level, optional but powerful), and query cache (stores query results)."*

---

### **6. Mapping One-to-Many & Many-to-Many**

#### **One-to-Many**

* Example: `Department` → `Employees`

```java
@Entity
class Department {
   @OneToMany(mappedBy="department", cascade=CascadeType.ALL, fetch=FetchType.LAZY)
   private List<Employee> employees;
}

@Entity
class Employee {
   @ManyToOne
   @JoinColumn(name="dept_id")
   private Department department;
}
```

#### **Many-to-Many**

* Example: `Student` ↔ `Course`

```java
@Entity
class Student {
   @ManyToMany
   @JoinTable(
       name="student_course",
       joinColumns=@JoinColumn(name="student_id"),
       inverseJoinColumns=@JoinColumn(name="course_id")
   )
   private List<Course> courses;
}

@Entity
class Course {
   @ManyToMany(mappedBy="courses")
   private List<Student> students;
}
```

👉 **Interview Answer:**
*"We use `@OneToMany` with `mappedBy` for one-to-many relationships and `@ManyToMany` with a `@JoinTable` for many-to-many mappings."*


