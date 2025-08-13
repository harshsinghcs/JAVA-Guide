# **Postman Notes**

![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## **1. What is Postman?**

Postman is a **popular API testing tool** that helps developers send HTTP requests to APIs, inspect responses, and automate API tests without writing extra code.

---

## **2. Why Use Postman?**

* Test REST APIs easily without writing code
* Check API responses (status codes, data, errors)
* Automate repetitive API testing
* Organize API requests in **collections**
* Share API documentation with team members

---

## **3. Basic Features**

| Feature                   | Description                                         |
| ------------------------- | --------------------------------------------------- |
| **New Request**           | Send API requests (GET, POST, PUT, DELETE, etc.)    |
| **Collections**           | Group related requests together                     |
| **Environment Variables** | Store reusable values like `baseURL` or `authToken` |
| **Pre-request Scripts**   | JavaScript code to run before sending a request     |
| **Tests**                 | JavaScript code to validate API responses           |
| **History**               | View past requests and responses                    |

---

## **4. HTTP Methods in Postman**

| Method     | Purpose                       | Example                  |
| ---------- | ----------------------------- | ------------------------ |
| **GET**    | Retrieve data from the server | Get all users            |
| **POST**   | Send new data to the server   | Create a user            |
| **PUT**    | Update existing data          | Update a user profile    |
| **PATCH**  | Partially update data         | Update only user’s email |
| **DELETE** | Remove data                   | Delete a user            |

---

## **5. How to Send a Request in Postman**

1. **Open Postman**
2. Click **New → HTTP Request**
3. Select **HTTP method** (GET, POST, etc.)
4. Enter **API endpoint URL**
5. (Optional) Add **Headers** (e.g., `Content-Type: application/json`)
6. (Optional) Add **Body** for POST/PUT requests (choose `raw` → JSON)
7. Click **Send**
8. See **response status, time, and body** in the response panel

---

## **6. Setting Environment Variables**

* Go to **Environments** in Postman
* Add variables like:

  * `baseURL = https://api.example.com`
  * `authToken = your_token_here`
* Use them in requests: `{{baseURL}}/users`

---

## **7. Writing Tests in Postman**

Postman allows you to write small scripts to check responses:

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

---

## **8. Tips for Using Postman Efficiently**

* Save requests in **Collections** for reuse
* Use **Environments** for different setups (dev, staging, production)
* Share Collections with your team
* Use **Monitors** to schedule API tests
* Use **Pre-request Scripts** for authentication

---

## **9. Common Status Codes**

| Code    | Meaning                                       |
| ------- | --------------------------------------------- |
| **200** | OK - Successful request                       |
| **201** | Created - Resource successfully created       |
| **400** | Bad Request - Invalid input                   |
| **401** | Unauthorized - Missing/invalid authentication |
| **403** | Forbidden - No permission                     |
| **404** | Not Found - Resource doesn’t exist            |
| **500** | Internal Server Error                         |

---

## **10. Example: Testing a Registration API in Postman**

* **Method:** `POST`
* **URL:** `{{baseURL}}/register`
* **Headers:**

  * `Content-Type: application/json`
  * `Authorization: Bearer {{authToken}}`
* **Body (raw → JSON):**

```json
{
  "name": "Harsh Singh",
  "email": "harsh@example.com",
  "password": "pass123"
}
```

* **Send Request** → Check response status & body
