# 🛠 Handling Concurrency in Real-Life Java Projects

## 1. **Booking System (e.g., Movie/Bus Ticket Booking)**

**Problem:** Two users try to book the last available seat at the same time.
**Solution Approaches:**

* **Optimistic Locking (preferred):**

  ```java
  @Entity
  public class Seat {
      @Id
      private Long id;
      private boolean booked;

      @Version
      private int version;
  }
  ```

  * If two users book the same seat, one update succeeds, the other fails (`OptimisticLockException` → retry logic).
* **Pessimistic Locking (when conflicts are frequent):**

  ```java
  @Lock(LockModeType.PESSIMISTIC_WRITE)
  Seat findSeatById(Long id);
  ```

  * Locks the seat row until transaction finishes.

👉 Used in **IRCTC, BookMyShow, Bus Ticket apps**.

---

## 2. **E-Commerce (Amazon/Flipkart Style)**

**Problems:**

* Multiple users add the same product to cart.
* Inventory stock may reduce to **negative** if concurrency isn’t handled.

**Solutions:**

* **Atomic Inventory Updates** (DB handles concurrency):

  ```sql
  UPDATE product 
  SET stock = stock - 1 
  WHERE id = ? AND stock > 0;
  ```

  * Only one request succeeds, others fail gracefully.
* **Versioning with Optimistic Locking** in JPA for product stock.
* **Distributed Locking (Redis/Zookeeper)** if multiple service instances are deployed.
  Example with Redisson:

  ```java
  RLock lock = redissonClient.getLock("product:123");
  lock.lock();
  try {
      // reduce stock safely
  } finally {
      lock.unlock();
  }
  ```

👉 Used in **Amazon flash sales, Flipkart Big Billion Days**.

---

## 3. **Shopping Cart / Order Processing**

**Problem:**

* Multiple microservices (Cart, Payment, Inventory) update the same order.
* Need consistency across services.

**Solutions:**

* **Transactional Outbox / Saga Pattern** (event-driven):

  * Cart → Order Created Event → Inventory Service reserves stock → Payment Service deducts money.
  * If payment fails → send compensating event → Inventory restores stock.
* **Idempotency Key**: Prevents duplicate orders when a user clicks "Pay" twice.

Example:

```java
@PostMapping("/order")
public ResponseEntity<?> placeOrder(@RequestHeader("Idempotency-Key") String key) {
    if(orderService.alreadyProcessed(key)){
        return ResponseEntity.ok("Order already placed!");
    }
    return ResponseEntity.ok(orderService.createOrder(key));
}
```

👉 Used in **Swiggy, Zomato, Amazon checkout systems**.

---

## 4. **Banking / Payment Systems**

**Problem:** Same account balance updated by multiple transactions.
**Solutions:**

* Use **Serializable isolation** to ensure no phantom reads.
* **Distributed Locking (Redis/DB row-level lock)** for account balance.
* **Eventual Consistency** with Kafka for balance updates across microservices.

---

## 🔑 Best Practices Across Projects

1. **Use Optimistic Locking** for performance in high-read systems.
2. **Use Pessimistic Locking** only when conflict probability is high (like ticket booking).
3. **Apply Database Constraints** (unique indexes, check constraints) → last line of defense.
4. **Keep transactions small** to avoid deadlocks.
5. **Use Message Queues (Kafka, RabbitMQ)** for async tasks → avoid direct race conditions.
6. **Distributed Locking (Redis/Zookeeper)** in microservices → ensures cluster-wide safety.
7. **Always add retry + backoff logic** in case of optimistic lock failures.

---

✅ **Quick Mapping**

| Project Type         | Concurrency Problem         | Solution                                  |
| -------------------- | --------------------------- | ----------------------------------------- |
| Ticket Booking       | Last seat booked by 2 users | Optimistic Locking / Pessimistic Lock     |
| E-Commerce Inventory | Stock going negative        | Atomic DB update / Redis Lock             |
| Shopping Cart        | Duplicate order/payment     | Idempotency Key + Saga Pattern            |
| Banking              | Double debit/credit         | Serializable Isolation / Distributed Lock |

---
