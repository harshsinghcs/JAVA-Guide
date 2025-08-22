# 📘 Multithreading in Java

### 🔹 What is Multithreading?

* **Multithreading** is a process of executing multiple threads **simultaneously** to maximize CPU utilization.
* Each thread runs independently but shares the same memory space.

---

### 🔹 Thread vs Process

| **Process**                      | **Thread**                                           |
| -------------------------------- | ---------------------------------------------------- |
| Independent program in execution | Smallest unit of a process                           |
| Has its own memory               | Shares memory with other threads of the same process |
| Heavyweight                      | Lightweight                                          |
| Context switching is slower      | Context switching is faster                          |

---

### 🔹 Creating Threads in Java

There are two main ways:

1. **By extending `Thread` class**

   ```java
   class MyThread extends Thread {
       public void run() {
           System.out.println("Thread is running...");
       }
   }
   public class Main {
       public static void main(String[] args) {
           MyThread t1 = new MyThread();
           t1.start(); // start() creates a new thread and calls run()
       }
   }
   ```

2. **By implementing `Runnable` interface**

   ```java
   class MyRunnable implements Runnable {
       public void run() {
           System.out.println("Thread is running...");
       }
   }
   public class Main {
       public static void main(String[] args) {
           Thread t1 = new Thread(new MyRunnable());
           t1.start();
       }
   }
   ```

✅ **Runnable is preferred** because Java supports multiple inheritance through interfaces.

---

### 🔹 Thread Lifecycle (States)

1. **New** → Thread created but not started.
2. **Runnable** → Ready to run, waiting for CPU.
3. **Running** → Thread scheduler picks it for execution.
4. **Waiting/Blocked** → Temporarily inactive.
5. **Terminated** → Finished execution.

---

### 🔹 Important Thread Methods

| **Method**    | **Description**                                 |
| ------------- | ----------------------------------------------- |
| `start()`     | Starts a new thread (calls `run()` internally). |
| `run()`       | Code inside this executes in the new thread.    |
| `sleep(ms)`   | Makes the thread pause for given milliseconds.  |
| `join()`      | Waits for the thread to finish.                 |
| `yield()`     | Pauses current thread to give chance to others. |
| `interrupt()` | Interrupts a sleeping/waiting thread.           |
| `isAlive()`   | Checks if thread is still running.              |

---

### 🔹 Thread Priority

* Each thread has a **priority (1 to 10)**.
* Constants: `MIN_PRIORITY = 1`, `NORM_PRIORITY = 5` (default), `MAX_PRIORITY = 10`.
* Used by **Thread Scheduler** to decide execution (but not guaranteed).

---

### 🔹 Synchronization

Since multiple threads share data, inconsistency may occur.

* **`synchronized` keyword** ensures only one thread accesses the critical section at a time.

Example:

```java
class Counter {
    int count = 0;
    public synchronized void increment() {
        count++;
    }
}
```

---

### 🔹 Inter-Thread Communication

* Methods: `wait()`, `notify()`, `notifyAll()` (defined in Object class).
* Used to achieve coordination between threads.

---

### 🔹 Thread Pools (Executor Framework)

Instead of creating new threads each time → use **Thread Pool** for efficiency.

```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        for (int i = 0; i < 5; i++) {
            executor.execute(() -> {
                System.out.println("Thread running: " + Thread.currentThread().getName());
            });
        }
        executor.shutdown();
    }
}
```

---

### 🔹 Concurrency Utilities (java.util.concurrent)

* `ExecutorService` → Thread pool management.
* `Future` & `Callable` → Return results from threads.
* `CountDownLatch`, `CyclicBarrier` → Thread coordination.
* `ReentrantLock` → Advanced synchronization.
* `Atomic` classes → Lock-free thread-safe operations.

---

### 🔹 Advantages of Multithreading

* Better CPU utilization.
* Faster execution (concurrent tasks).
* Cost-effective (less memory than processes).

### 🔹 Disadvantages

* Complexity in debugging.
* Risk of deadlocks, race conditions.
* Context switching overhead.

