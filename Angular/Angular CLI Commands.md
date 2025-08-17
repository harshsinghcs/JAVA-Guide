# ⚡ Angular CLI Commands
[![Angular](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white)](#)

## 1. Project Setup

* **Create a new Angular project**

  ```bash
  ng new project-name
  ```

  > Adds Angular structure with routing & styling options.

* **Run the development server**

  ```bash
  ng serve
  ```

  > Default at `http://localhost:4200`.

* **Run with specific port**

  ```bash
  ng serve --port 4500
  ```

---

## 2. Generate Commands (Scaffolding)

* **Generate component**

  ```bash
  ng generate component component-name
  ng g c component-name     # shortcut
  ```

* **Generate service**

  ```bash
  ng g s service-name
  ```

* **Generate module**

  ```bash
  ng g m module-name
  ```

* **Generate directive**

  ```bash
  ng g d directive-name
  ```

* **Generate pipe**

  ```bash
  ng g p pipe-name
  ```

* **Generate guard** (for routing auth, etc.)

  ```bash
  ng g guard guard-name
  ```

---

## 3. Build & Deployment

* **Build for production**

  ```bash
  ng build --prod
  ```

* **Build with output path**

  ```bash
  ng build --output-path=dist/my-app
  ```

* **Serve build locally** (needs http-server package)

  ```bash
  npx http-server dist/my-app
  ```

---

## 4. Testing

* **Run unit tests**

  ```bash
  ng test
  ```

* **Run end-to-end tests (E2E)**

  ```bash
  ng e2e
  ```

---

## 5. Linting & Formatting

* **Lint the code**

  ```bash
  ng lint
  ```

---

## 6. Useful Options

* **Check Angular version**

  ```bash
  ng version
  ```

* **Update Angular**

  ```bash
  ng update @angular/cli @angular/core
  ```

* **List available commands**

  ```bash
  ng help
  ```

---

✅ **Shortcut summary table:**

| Task               | Command (Short)    |
| ------------------ | ------------------ |
| Create project     | `ng new app-name`  |
| Start server       | `ng serve -o`      |
| Generate component | `ng g c comp-name` |
| Generate service   | `ng g s service`   |
| Generate module    | `ng g m module`    |
| Generate pipe      | `ng g p pipe`      |
| Build production   | `ng build --prod`  |
| Run tests          | `ng test`          |
| Version info       | `ng v`             |

---


