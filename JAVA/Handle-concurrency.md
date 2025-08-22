# 📝 Concurrency Handling in Java Spring Boot

Concurrency issues occur when **multiple threads or requests** try to access/modify the same resource (database record, cache, file, etc.) at the same time.
If not handled properly, this leads to **race conditions, dirty reads, lost updates, or deadlocks**.

---

## 1. **At Java Language Level**

* ✅ **Synchronized blocks/methods** – Prevents multiple threads from executing a code block at the same time.
* ✅ **Locks (ReentrantLock, ReadWriteLock)** – More fine-grained locking than `synchronized`.
* ✅ **Concurrent Collections** – `ConcurrentHashMap`, `CopyOnWriteArrayList` help in thread-safe data structures.
* ✅ **Atomic classes** – `AtomicInteger`, `AtomicReference` provide lock-free thread safety.

---

## 2. **Spring Boot Level**

### a) **Optimistic Locking** (Preferred in high-read systems)

* Uses **versioning** in database rows.
* Example: Add a `@Version` field in JPA entity.

```java
@Entity
public class Account {
    @Id
    private Long id;

    private double balance;

    @Version
    private int version;
}
```

* If two users try to update the same record, only one succeeds, others get an `OptimisticLockException`.

---

### b) **Pessimistic Locking** (Preferred in high-write systems)

* Locks the database row while one transaction is updating it.

```java
@Lock(LockModeType.PESSIMISTIC_WRITE)
@Query("SELECT a FROM Account a WHERE a.id = :id")
Account findAccountForUpdate(@Param("id") Long id);
```

* Prevents conflicts but reduces concurrency → might cause blocking.

---

### c) **@Transactional and Isolation Levels**

Spring’s `@Transactional` allows configuring database **isolation levels**:

* `READ_COMMITTED` → Prevents dirty reads. (Default in most DBs)
* `REPEATABLE_READ` → Prevents non-repeatable reads.
* `SERIALIZABLE` → Strictest, prevents phantom reads but reduces performance.

Example:

```java
@Transactional(isolation = Isolation.SERIALIZABLE)
public void transferMoney(Long fromId, Long toId, Double amount) {
    // safe money transfer
}
```

---

### d) **Synchronized in Services**

For in-memory shared resources:

```java
@Service
public class CounterService {
    private AtomicInteger counter = new AtomicInteger(0);

    public int increment() {
        return counter.incrementAndGet();
    }
}
```

* Use **synchronized** carefully in Spring beans → since beans are **singleton by default**, multiple requests share them.

---

### e) **Asynchronous Processing**

* `@Async` in Spring allows non-blocking execution.

```java
@Async
public void sendNotification(String message) {
    // runs in a separate thread
}
```

* Use `ThreadPoolTaskExecutor` to manage concurrency.

---

### f) **Distributed Locking (Microservices Case)**

When multiple instances of the service are running:

* Use **Redis-based locks** (e.g., Redisson).
* Use **Zookeeper locks** or **DB-based locks**.

Example with Redisson:

```java
RLock lock = redissonClient.getLock("accountLock");
try {
    lock.lock();
    // critical section
} finally {
    lock.unlock();
}
```

---

## 3. **Best Practices**

* Always prefer **optimistic locking** unless strong consistency is required.
* Keep **transactions short** to avoid deadlocks.
* Use **bulk updates carefully** (may skip versioning checks).
* Monitor thread pools to avoid bottlenecks.
* For distributed systems, rely on **message queues (Kafka, RabbitMQ)** instead of direct shared-state concurrency.

---

✅ **Summary Table**

| Approach                           | Use Case             | Pros                   | Cons                  |
| ---------------------------------- | -------------------- | ---------------------- | --------------------- |
| Synchronized / Locks               | In-memory state      | Simple                 | Not for distributed   |
| Optimistic Locking                 | High-read systems    | Scalable               | Retry needed          |
| Pessimistic Locking                | High-write conflicts | Prevents lost updates  | Slower                |
| @Transactional Isolation           | Data integrity       | DB handles concurrency | May reduce throughput |
| Distributed Lock (Redis/ZooKeeper) | Microservices        | Ensures global lock    | Extra infra           |
| Async Processing                   | Background tasks     | Non-blocking           | Debugging harder      |
