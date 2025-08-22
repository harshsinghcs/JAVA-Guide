# 📘 Exception Handling in Java – Notes

---

## 1. **What is Exception Handling?**

* **Definition**: Exception handling in Java is a mechanism to handle runtime errors, so the normal flow of the application can be maintained.
* **Exception** = an abnormal condition that interrupts program execution.
* **Goal**: Provide a way to detect, handle, and recover from runtime problems.

---

## 2. **Hierarchy of Exceptions**

All exceptions in Java are objects of type `Throwable`.

```
Object
 └── Throwable
      ├── Error
      │    ├── OutOfMemoryError
      │    ├── StackOverflowError
      │    └── VirtualMachineError
      │
      └── Exception
           ├── RuntimeException (Unchecked)
           │    ├── NullPointerException
           │    ├── ArrayIndexOutOfBoundsException
           │    ├── ArithmeticException
           │    └── ClassCastException
           │
           └── Checked Exceptions
                ├── IOException
                ├── SQLException
                └── FileNotFoundException
```

✅ **Error** → serious issues, cannot be recovered (JVM related).
✅ **Exception** → conditions in code that can be handled.

* **Checked Exception** → checked at compile time (must be handled).
* **Unchecked Exception** → checked at runtime (programmer mistakes).

---

## 3. **Keywords in Exception Handling**

1. **try** → block of code that may throw exception.
2. **catch** → block that handles the exception.
3. **finally** → block that executes always (cleanup code).
4. **throw** → used to explicitly throw an exception.
5. **throws** → declares exceptions a method may throw.

---

## 4. **Basic Syntax**

```java
try {
    // code that may throw exception
} catch (ExceptionType e) {
    // handling code
} finally {
    // cleanup code (always executed)
}
```

---

## 5. **Example**

```java
public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            int a = 10 / 0;  // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero!");
        } finally {
            System.out.println("Finally block executed.");
        }
    }
}
```

**Output:**

```
Cannot divide by zero!
Finally block executed.
```

---

## 6. **Types of Exceptions**

| **Type**                       | **Checked / Unchecked** | **Example**                          |
| ------------------------------ | ----------------------- | ------------------------------------ |
| IOException                    | Checked                 | File not found, input/output errors  |
| SQLException                   | Checked                 | Database issues                      |
| ClassNotFoundException         | Checked                 | Class not found at runtime           |
| NullPointerException           | Unchecked               | Accessing object with null reference |
| ArithmeticException            | Unchecked               | Divide by zero                       |
| ArrayIndexOutOfBoundsException | Unchecked               | Invalid index in array               |

---

## 7. **Multiple Catch Blocks**

```java
try {
    String s = null;
    System.out.println(s.length());
} catch (ArithmeticException e) {
    System.out.println("Arithmetic Exception");
} catch (NullPointerException e) {
    System.out.println("Null Pointer Exception");
} catch (Exception e) {
    System.out.println("General Exception");
}
```

⚠️ Always put **child exceptions first**, then parent.

---

## 8. **Nested try-catch**

```java
try {
    try {
        int arr[] = new int[5];
        arr[5] = 100; // ArrayIndexOutOfBoundsException
    } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println("Inner catch: " + e);
    }
} catch (Exception e) {
    System.out.println("Outer catch: " + e);
}
```

---

## 9. **throw vs throws**

| **throw**                                  | **throws**                                        |
| ------------------------------------------ | ------------------------------------------------- |
| Used to explicitly throw exception.        | Used in method declaration to specify exceptions. |
| Followed by instance of exception.         | Followed by class names of exceptions.            |
| Example: `throw new IOException("Error");` | Example: `void readFile() throws IOException`     |

---

## 10. **Custom Exception**

You can define your own exception by extending `Exception` or `RuntimeException`.

```java
class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}

public class Test {
    static void validateAge(int age) throws InvalidAgeException {
        if (age < 18)
            throw new InvalidAgeException("Age must be 18 or above.");
    }

    public static void main(String[] args) {
        try {
            validateAge(16);
        } catch (InvalidAgeException e) {
            System.out.println("Caught Exception: " + e.getMessage());
        }
    }
}
```

---

## 11. **finally vs finalize**

* **finally** → block always executed (cleanup, closing resources).
* **finalize()** → method called by GC before destroying object (not reliable, deprecated).

---

## 12. **try-with-resources (Java 7+)**

Used for **automatic resource management** (closes resources automatically).

```java
import java.io.*;

public class TryWithResourceDemo {
    public static void main(String[] args) {
        try (FileReader fr = new FileReader("file.txt")) {
            int i;
            while ((i = fr.read()) != -1) {
                System.out.print((char) i);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

---

## 13. **Best Practices**

* Catch specific exceptions (not generic `Exception` always).
* Use **finally** or **try-with-resources** for closing connections/files.
* Don’t swallow exceptions (e.g., empty catch block).
* Create custom exceptions only when needed.
* Never use exceptions for normal program flow.