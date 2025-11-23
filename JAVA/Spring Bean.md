# Spring Beans in Spring Boot

## 📌 What is a Spring Bean?

A **Spring Bean** is simply a **Java object that is created, managed, and controlled by the Spring IoC (Inversion of Control) container**.

Spring is responsible for:
- Creating the object
- Injecting dependencies
- Managing its lifecycle
- Reusing the object where needed

---

## 🧠 Why are Spring Beans Used?

| Reason | Explanation |
|-------|-------------|
| **Automatic Object Creation** | Spring creates objects for you, no need for `new` |
| **Dependency Injection (DI)** | Beans can be automatically injected into each other |
| **Lifecycle Management** | Spring handles init/destroy |
| **Reusability** | A single bean can be reused across the app |
| **Loose Coupling** | Increases flexibility and maintainability |

---

## ✔️ How to Create a Spring Bean?

### **1. Using Stereotype Annotations**
Spring automatically creates beans when you use:

- `@Component`
- `@Service`
- `@Repository`
- `@Controller`
- `@RestController`

Example:
```java
@Service
public class MyService {
}




### **2. Using `@Bean` Annotation (Manual Creation)**

```java
@Configuration
public class AppConfig {

    @Bean
    public UserService userService() {
        return new UserService();
    }
}
```

---

## 🧩 Real Example

### **Bean Class**

```java
@Service
public class MessageService {
    public String getMessage() {
        return "Hello from Bean!";
    }
}
```

### **Using Bean in Controller**

```java
@RestController
public class MyController {

    @Autowired
    private MessageService messageService;

    @GetMapping("/msg")
    public String msg() {
        return messageService.getMessage();
    }
}
```

---

## 🔥 Interview-Ready Answer

**“A Spring Bean is an object that the Spring IoC container manages — it creates, configures, and injects dependencies into these objects automatically.”**

---

## 📘 Bean Lifecycle (Short Summary)

1. Bean is **created**
2. Dependencies are **injected**
3. **Init** method is called
4. Bean is **used by application**
5. **Destroy** method is called on shutdown

---
