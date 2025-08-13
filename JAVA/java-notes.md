
# ☕ Java Notes
[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://github.com/your-username/your-java-notes-repo)

## 1. Basics of Java

* **Java**: High-level, object-oriented, platform-independent programming language.
* **Key Features**:
  * **Platform Independent** – Write Once, Run Anywhere (via JVM).
  * **Object-Oriented** – Everything is represented as objects.
  * **Robust** – Strong memory management, exception handling.
  * **Secure** – No explicit pointer, bytecode verification.
  * **Multithreaded** – Support for concurrent execution.
  * **Portable** – Compiled bytecode runs on any platform with JVM.

---

## 2. Java Architecture

* **Source Code (.java)** → **Compiler (javac)** → **Bytecode (.class)** → **JVM** → **Machine Code**
* **JVM Components**:
  * **Class Loader** – Loads class files.
  * **Memory Areas** – Method area, Heap, Stack, PC register.
  * **Execution Engine** – Interpreter, JIT compiler.
  * **Garbage Collector** – Frees unused objects.

---

## 3. Data Types

* **Primitive**:
  * `byte` (1 byte), `short` (2), `int` (4), `long` (8)
  * `float` (4), `double` (8)
  * `char` (2), `boolean` (1 bit)
* **Non-Primitive**:
  * Strings, Arrays, Classes, Interfaces.

---

## 4. OOP Concepts

| Concept           | Description                                       | Example                            |
| ----------------- | ------------------------------------------------- | ---------------------------------- |
| **Encapsulation** | Wrapping data and methods in one unit (class).    | `private` fields + getters/setters |
| **Inheritance**   | One class acquires properties/methods of another. | `extends` keyword                  |
| **Polymorphism**  | Same method name, different behavior.             | Overloading / Overriding           |
| **Abstraction**   | Hiding implementation details.                    | Abstract classes / Interfaces      |

---

## 5. Important Keywords

* **final** – Variable (constant), method (cannot override), class (cannot extend).
* **static** – Belongs to class, not object.
* **this** – Refers to current object.
* **super** – Refers to parent class.
* **synchronized** – Thread-safe block/method.
* **volatile** – Tells JVM value may change unexpectedly (thread communication).
* **transient** – Excluded from serialization.

---

## 6. Java Collections Framework

* **List** – Ordered, duplicates allowed → `ArrayList`, `LinkedList`.
* **Set** – No duplicates → `HashSet`, `LinkedHashSet`, `TreeSet`.
* **Map** – Key-value pairs → `HashMap`, `LinkedHashMap`, `TreeMap`.
* **Queue** – FIFO → `PriorityQueue`, `ArrayDeque`.

---

## 7. Exception Handling

* **Checked** – Compile-time (IOException, SQLException).
* **Unchecked** – Runtime (NullPointerException, ArithmeticException).
* **Keywords**: `try`, `catch`, `finally`, `throw`, `throws`.

Example:

```java
try {
    int a = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero");
} finally {
    System.out.println("Always runs");
}
```

---

## 8. Java 8 Features

* **Lambda Expressions** – `(param) -> expression`
* **Functional Interfaces** – Single abstract method (`@FunctionalInterface`)
* **Streams API** – Functional-style operations on collections.
* **Optional** – Avoid `null` checks.
* **Default & Static Methods in Interfaces**.

---

## 9. Multithreading

* **Thread creation**:
  * Extending `Thread` class.
  * Implementing `Runnable` interface.
* **Thread lifecycle**:
  * New → Runnable → Running → Waiting/Sleeping → Terminated.
* **Synchronization** to avoid race conditions.

---

## 10. Memory Management

* **Heap** – Stores objects.
* **Stack** – Stores method calls and local variables.
* **Garbage Collection** – Automatic removal of unused objects.

