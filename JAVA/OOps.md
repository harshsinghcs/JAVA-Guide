# 📘 OOPs Notes in Java

OOP (Object-Oriented Programming) in Java is a paradigm that organizes code into **classes and objects**.
Main principles: **Inheritance, Polymorphism, Abstraction, Encapsulation.**

---

## 🔹 1. Inheritance

Inheritance allows a class (**child**) to acquire properties & behavior of another class (**parent**).

### ✅ Types of Inheritance in Java:

| Type                         | Description                                                                                       | Example                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Single Inheritance**       | One child inherits from one parent                                                                | `class A → class B`                  |
| **Multilevel Inheritance**   | Chain of inheritance                                                                              | `A → B → C`                          |
| **Hierarchical Inheritance** | Multiple child classes inherit from one parent                                                    | `A → B, C`                           |
| **Multiple Inheritance**     | One class inherits from multiple parents (❌ not allowed with classes, ✅ possible with interfaces) | `interface A, interface B → class C` |
| **Hybrid Inheritance**       | Combination of multiple types (❌ not directly supported, ✅ via interfaces)                        | Mix of above                         |

👉 Example (Single Inheritance):

```java
class Animal {
    void eat() { System.out.println("Eating..."); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking..."); }
}
public class Test {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();  // from parent
        d.bark(); // from child
    }
}
```

---

## 🔹 2. Polymorphism

**Polymorphism = Many Forms.**
It allows methods/objects to behave differently based on context.

### Types:

1. **Compile-time (Method Overloading)** → Same method name, different parameter list.
2. **Runtime (Method Overriding)** → Child class provides its own implementation of a parent method.

👉 Example:

```java
// Compile-time
class Calculator {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
}

// Runtime
class Animal {
    void sound() { System.out.println("Animal makes sound"); }
}
class Dog extends Animal {
    void sound() { System.out.println("Dog barks"); }
}
```

---

## 🔹 3. Abstraction

Hiding implementation details and showing only functionality.

### Ways to achieve abstraction in Java:

* **Abstract Class** (0–100% abstraction)
* **Interface** (100% abstraction, Java 8+ allows default & static methods)

👉 Example:

```java
abstract class Animal {
    abstract void sound(); // abstract method
}
class Dog extends Animal {
    void sound() { System.out.println("Bark"); }
}
```

---

## 🔹 4. Encapsulation

Wrapping **data (variables)** and **methods** into a single unit (class).
Data is hidden using **private** and accessed via **getters/setters**.

👉 Example:

```java
class Student {
    private String name; // private data

    // getter
    public String getName() { return name; }

    // setter
    public void setName(String name) { this.name = name; }
}
```

---

## 🔹 5. Class & Object (Basic Building Block)

* **Class** → Blueprint/template.
* **Object** → Instance of class.

```java
class Car {
    String color = "Red";
    void drive() { System.out.println("Car is driving"); }
}

public class Main {
    public static void main(String[] args) {
        Car c = new Car(); // object
        c.drive();
    }
}
```

---

## ✅ Summary

* **Inheritance** → Code reuse (5 types).
* **Polymorphism** → Same method, different behavior.
* **Abstraction** → Hides implementation, shows features.
* **Encapsulation** → Data hiding + controlled access.
* **Class & Object** → Foundation of OOP.

