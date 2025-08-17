# 📘 Angular Notes
[![Angular](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white)](#)

## 1. Introduction

* **Angular** is a **TypeScript-based** front-end framework developed by Google.
* Used to build **Single Page Applications (SPA)**.
* **Features**: Two-way data binding, Dependency Injection (DI), Directives, Routing, RxJS (reactive programming).

---

## 2. Angular Architecture

1. **Modules**

   * Root module: `AppModule`
   * Feature modules: e.g., `UserModule`, `AdminModule`
   * Lazy-loaded modules for optimization.

2. **Components**

   * Building blocks of UI.
   * Consist of **HTML template**, **CSS**, and **TypeScript class**.

3. **Templates**

   * Defines UI with **HTML + Angular directives**.
   * Example: `*ngIf`, `*ngFor`.

4. **Directives**

   * **Structural**: `*ngIf`, `*ngFor`, `*ngSwitch`.
   * **Attribute**: `ngClass`, `ngStyle`, custom directives.

5. **Services**

   * Used for **business logic and data sharing**.
   * Provided via **Dependency Injection (DI)**.

6. **Dependency Injection**

   * Design pattern to inject service into components.
   * Improves testability & reusability.

---

## 3. Data Binding

1. **Interpolation**: `{{ data }}`
2. **Property Binding**: `<img [src]="imageUrl">`
3. **Event Binding**: `<button (click)="handleClick()">Click</button>`
4. **Two-way Binding**: `<input [(ngModel)]="username">`

---

## 4. Angular Lifecycle Hooks

* `ngOnInit()` → Called after component initialization.
* `ngOnChanges()` → Runs when input properties change.
* `ngDoCheck()` → Developer custom change detection.
* `ngAfterViewInit()`, `ngAfterContentInit()` → Called after view/content is initialized.
* `ngOnDestroy()` → Cleanup (unsubscribe, remove listeners).

---

## 5. Routing

* Used for SPA navigation.
* **AppRoutingModule** defines routes:

  ```ts
  const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'users/:id', component: UserComponent },
    { path: '**', redirectTo: 'home' }
  ];
  ```
* **RouterLink**: `<a routerLink="/home">Home</a>`
* **RouterOutlet**: `<router-outlet></router-outlet>`

---

## 6. Forms

1. **Template-driven forms** (simple, less scalable).
2. **Reactive forms** (preferred, scalable).

   ```ts
   this.form = new FormGroup({
     name: new FormControl('', Validators.required),
     email: new FormControl('', [Validators.required, Validators.email])
   });
   ```

---

## 7. Observables & RxJS

* Angular uses **RxJS** for async programming.
* **Observable**: Stream of data (HTTP response, events).
* Common operators: `map`, `filter`, `mergeMap`, `switchMap`.
* Must **unsubscribe** to avoid memory leaks (or use `async` pipe).

---

## 8. HTTP Client

* Provided by `HttpClientModule`.
* Example:

  ```ts
  this.http.get<User[]>('/api/users')
    .subscribe(data => this.users = data);
  ```

---

## 9. State Management

* Local state with `BehaviorSubject` or `Service`.
* Global state with **NgRx (Redux pattern)**.

---

## 10. Angular Best Practices

✅ Use **Reactive forms** for complex forms.
✅ Always **unsubscribe** from observables.
✅ Use **Lazy loading** for feature modules.
✅ Follow **OnPush change detection** strategy for performance.
✅ Split large apps into **feature modules**.

---

## 11. Angular 16+ Features

* **Signals**: New reactive primitive to replace some RxJS use cases.
* **Standalone Components**: No need to declare in `NgModule`.
* **Improved Hydration** for SSR.
* **Required Inputs**: Inputs can be marked as required.

