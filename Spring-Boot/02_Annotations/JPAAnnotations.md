# JPA Annotations

JPA (Java Persistence API) provides annotations to map Java classes to database tables.  
Here are the most important ones:

---

## 🔹 @Entity
- Marks a class as a JPA entity (mapped to a database table).
```java
@Entity
public class User { ... }
````

---

## 🔹 @Table

* Specifies the table name in the database.

```java
@Entity
@Table(name = "users")
public class User { ... }
```

---

## 🔹 @Id

* Defines the primary key of the entity.

```java
@Id
private Long id;
```

---

## 🔹 @GeneratedValue

* Defines how the primary key is generated.

```java
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
```

---

## 🔹 @Column

* Maps a field to a column with custom properties.

```java
@Column(name = "email", nullable = false, unique = true)
private String email;
```

---

## 🔹 @Transient

* Marks a field that should **not** be persisted in DB.

```java
@Transient
private int age;
```

---

## 🔹 @Lob

* Used for large objects (BLOB, CLOB).

```java
@Lob
private String description;
```

---

## 🔹 Relationships

### @OneToOne

```java
@OneToOne
@JoinColumn(name = "profile_id")
private Profile profile;
```

### @OneToMany

```java
@OneToMany(mappedBy = "user", cascade = CascadeType.ALL)
private List<Order> orders;
```

### @ManyToOne

```java
@ManyToOne
@JoinColumn(name = "user_id")
private User user;
```

### @ManyToMany

```java
@ManyToMany
@JoinTable(
  name = "student_course",
  joinColumns = @JoinColumn(name = "student_id"),
  inverseJoinColumns = @JoinColumn(name = "course_id")
)
private List<Course> courses;
```

---

## 🔹 @Embedded & @Embeddable

* Used for value objects inside an entity.

```java
@Embeddable
public class Address {
   private String city;
   private String state;
}

@Entity
public class User {
   @Embedded
   private Address address;
}
```

---

## 🔹 @Enumerated

* Maps an enum to a database column.

```java
@Enumerated(EnumType.STRING)
private Role role;
```

