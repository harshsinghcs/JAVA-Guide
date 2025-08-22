# 🔹 **Meaning of Concurrency**

👉 **Concurrency means multiple tasks making progress at the same time.**

* In **Java (or Spring Boot projects)**, concurrency happens when **multiple threads, users, or requests** try to access or update shared resources **simultaneously**.
* It doesn’t always mean tasks are running at the exact same instant (that’s *parallelism*), but they are *in progress and overlapping in time*.

---

## 🖼 Example (Real Life)

* You’re at a **ticket counter**.
* 10 people try to buy the **last 2 tickets** at the same time.
* The system must handle concurrency to make sure **only 2 people succeed**, and the other 8 get “Sold Out.”

---

## 💻 Example (Java Code)

Without concurrency handling:

```java
int tickets = 1;

public void bookTicket() {
    if (tickets > 0) {
        tickets--; 
        System.out.println("Ticket booked!");
    } else {
        System.out.println("No tickets left.");
    }
}
```

If **2 threads run `bookTicket()` at the same time**, both may see `tickets > 0` and both book → **overselling bug**.

👉 This is a **concurrency problem** (race condition).

---

## ✅ With Concurrency Handling

```java
synchronized public void bookTicket() {
    if (tickets > 0) {
        tickets--;
        System.out.println("Ticket booked!");
    } else {
        System.out.println("No tickets left.");
    }
}
```

Now only **one thread at a time** can enter, so no overselling happens.

---

## 🔑 Summary

* **Concurrency = multiple tasks running in overlapping time periods.**
* **Problem:** Data corruption, race conditions, deadlocks.
* **Solution:** Locks, transactions, optimistic/pessimistic locking, distributed locks.

