# 📨 Apache Kafka Notes  
![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)

A **comprehensive & beginner-friendly guide** to **Apache Kafka** — focused on **Java + Spring Boot microservices**.  
Covers concepts, architecture, commands, and best practices for real-world backend projects.

---

## 📌 **Overview**

- **Apache Kafka** is a **distributed event streaming platform** for building **real-time data pipelines** and **streaming applications**.
- Originally developed at **LinkedIn**, now maintained by the **Apache Software Foundation**.
- Known for **high throughput**, **low latency**, **fault tolerance**, and **scalability**.

---

## 1️⃣ **Core Concepts**

| Concept             | Description                                                                                                         | Example                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Producer**        | Sends messages (events) to Kafka topics.                                                                            | Order Service publishing "Order Placed" events.    |
| **Consumer**        | Reads messages from Kafka topics.                                                                                   | Inventory Service consuming "Order Placed" events. |
| **Broker**          | Kafka server that stores and serves messages.                                                                       | A Kafka cluster can have multiple brokers.         |
| **Topic**           | Named category/feed where records are stored.                                                                       | `order-events`                                     |
| **Partition**       | Splits a topic for parallelism & scalability.                                                                       | `order-events` with 3 partitions.                  |
| **Offset**          | Position of a record in a partition.                                                                                | Offset 0, 1, 2...                                  |
| **Consumer Group**  | A set of consumers sharing the work of consuming messages from a topic.                                             | Multiple consumers processing events in parallel.  |
| **ZooKeeper** (Old) | Used for metadata management (deprecated in Kafka 3.0+).                                                            | Not required in latest Kafka versions.             |

---

## 2️⃣ **Kafka Architecture**

**Producers → Topics (Partitions) → Brokers → Consumers**

- **Replication** ensures fault tolerance (**Replication Factor ≥ 2** recommended).
- Consumers **commit offsets** to avoid reprocessing.
- Supports both **Pub/Sub** and **Message Queue** patterns.

---

## 3️⃣ **Key Features**

✅ High throughput — millions of messages/sec  
✅ Horizontally scalable — add brokers & partitions easily  
✅ Durable — messages stored & replicated on disk  
✅ Low latency — near real-time event streaming  
✅ Flexible — works for both **microservices** & **big data pipelines**  

---

## 4️⃣ **Kafka Workflow**

1. **Producer** sends a message to a topic.  
2. **Broker** stores it in a specific partition.  
3. **Consumers** (in groups) read and process messages.  
4. Offsets are committed to track progress.

---

## 5️⃣ **Kafka with Java + Spring Boot**

**Dependency:**
```xml
<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka</artifactId>
</dependency>
````

**Producer Config:**

```yaml
spring:
  kafka:
    bootstrap-servers: localhost:9092
    producer:
      key-serializer: org.apache.kafka.common.serialization.StringSerializer
      value-serializer: org.apache.kafka.common.serialization.StringSerializer
```

**Consumer Config:**

```yaml
spring:
  kafka:
    bootstrap-servers: localhost:9092
    consumer:
      group-id: my-group
      key-deserializer: org.apache.kafka.common.serialization.StringDeserializer
      value-deserializer: org.apache.kafka.common.serialization.StringDeserializer
```

**Producer Example:**

```java
@Autowired
private KafkaTemplate<String, String> kafkaTemplate;

public void sendMessage(String msg) {
    kafkaTemplate.send("order-events", msg);
}
```

**Consumer Example:**

```java
@KafkaListener(topics = "order-events", groupId = "my-group")
public void consume(String message) {
    System.out.println("Received: " + message);
}
```

---

## 6️⃣ **Common Use Cases**

* Microservices event-driven communication
* Log aggregation & monitoring
* Real-time analytics (e.g., stock prices)
* Data integration (ETL pipelines)
* IoT data streams (sensor readings, fraud detection)

---

## 7️⃣ **Best Practices**

✔ Pick optimal partition count based on throughput
✔ Use **key-based partitioning** to preserve order for related messages
✔ Monitor **consumer lag** to ensure real-time performance
✔ Set **retention policies** (time or size based) wisely
✔ Use schema validation (JSON, Avro, Protobuf) for data consistency

---

## 8️⃣ **Kafka CLI Commands**

```bash
# Start Zookeeper (for old versions)
zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka broker
kafka-server-start.sh config/server.properties

# Create topic
kafka-topics.sh --create --topic order-events --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

# List topics
kafka-topics.sh --list --bootstrap-server localhost:9092

# Produce messages
kafka-console-producer.sh --topic order-events --bootstrap-server localhost:9092

# Consume messages
kafka-console-consumer.sh --topic order-events --bootstrap-server localhost:9092 --from-beginning
```

---

## Kafka vs Kafka Broker

| Aspect         | Kafka                                                                               | Kafka Broker                                                       |
| -------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Definition** | Entire event streaming platform (producers, consumers, topics, brokers, APIs, etc.) | A single Kafka server storing & serving messages.                  |
| **Scope**      | Complete ecosystem for producing, storing, and consuming events.                    | Component of Kafka responsible for storing data & serving clients. |
| **Analogy**    | **Railway network** (all stations, trains, signals).                                | **Single railway station** handling part of the network.           |
| **Cluster**    | Kafka is usually deployed as a **cluster of brokers**.                              | One **node** inside that cluster.                                  |

---

##  Kafka Architecture (Visual Overview)

Here’s a simplified architecture diagram illustrating how components like producers, brokers, and consumers interact in a Kafka-based microservices setup:

<p align="center">
  <img src="/images/kafka-event-driven-architecture-spring-boot.png" alt="Kafka Architecture Diagram" width="500" />
</p>

**Key Flow:**
1. Producers send events to Kafka topics (partitioned for scalability).  
2. Brokers store and replicate these events across a cluster.  
3. Consumers (grouped with offsets) read and process messages reliably.  
4. Replication and offset tracking ensure fault tolerance and persistence.
