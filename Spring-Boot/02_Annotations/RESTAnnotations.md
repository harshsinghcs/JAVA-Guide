# REST Annotations (Spring Boot)

Spring Boot provides several annotations to build REST APIs easily.  
Here are the most commonly used ones:

---

## 🔹 @RestController
- Combines `@Controller` + `@ResponseBody`.
- Marks a class as a REST API controller.
- All methods return JSON/XML directly.

```java
@RestController
public class UserController {
    @GetMapping("/users")
    public List<User> getAllUsers() {
        return userService.getUsers();
    }
}
````

---

## 🔹 @RequestMapping

* Maps HTTP requests to handler methods/classes.
* Can define path + HTTP method.

```java
@RequestMapping(value = "/users", method = RequestMethod.GET)
public List<User> getUsers() { ... }
```

---

## 🔹 @GetMapping / @PostMapping / @PutMapping / @DeleteMapping

* Shortcut annotations for HTTP methods.

```java
@GetMapping("/users/{id}")
public User getUser(@PathVariable int id) { ... }

@PostMapping("/users")
public User addUser(@RequestBody User user) { ... }
```

---

## 🔹 @PathVariable

* Binds URL path parameter to a method parameter.

```java
@GetMapping("/users/{id}")
public User getUser(@PathVariable("id") int userId) { ... }
```

---

## 🔹 @RequestParam

* Extracts query parameters from the request URL.

```java
@GetMapping("/search")
public List<User> searchUsers(@RequestParam String name) { ... }
```

---

## 🔹 @RequestBody

* Maps the request body (JSON/XML) to a Java object.

```java
@PostMapping("/users")
public User createUser(@RequestBody User user) { ... }
```

---

## 🔹 @ResponseStatus

* Sets the HTTP response status code.

```java
@ResponseStatus(HttpStatus.CREATED)
@PostMapping("/users")
public User createUser(@RequestBody User user) { ... }
```

---

## 🔹 @CrossOrigin

* Enables CORS (Cross-Origin Resource Sharing) for APIs.

```java
@CrossOrigin(origins = "http://localhost:3000")
@GetMapping("/users")
public List<User> getUsers() { ... }
```
