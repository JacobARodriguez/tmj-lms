# TMJ — Track My Journey

## 📘 Overview

TMJ (Track My Journey) is a simple Learning Management System (LMS) prototype focused on progress visibility.

This Milestone 1 version is a non-functional Flask scaffold that demonstrates the app’s architecture and design setup.

It includes basic routes, templates, and a static progress bar to visualize the concept.

---

## 🚀 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/ThaoHuynh94/tmj-lms.git](https://github.com/ThaoHuynh94/tmj-lms.git)
    cd tmj-lms
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv .venv
    
    # (Mac/Linux)
    source .venv/bin/activate
    
    # (Windows)
    .venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the app**
    ```bash
    python run.py
    ```
    Then open your browser and go to:
    👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧱 Tech Stack

* **Flask** — web framework
* **Flask-SQLAlchemy** — ORM with SQLite (non-functional stub for M1)
* **Flask-Login** — user management (wired but non-functional)
* **Flask-WTF** — form handling
* **HTML / CSS / Jinja2** — templates and styling

---

## 🗂️ Project Structure

```
app/
├── __init__.py          # app factory: create_app()
├── config.py            # SQLite URI + SECRET_KEY placeholder
├── models.py            # User + Course model stubs
├── forms.py             # WTForms LoginForm
├── auth/
│   ├── __init__.py
│   ├── routes.py        # /auth/login (GET render, POST validate + flash)
│   └── templates/auth/login.html
├── main/
│   ├── __init__.py
│   ├── routes.py        # / (index), /feature
│   └── templates/main/
│       ├── index.html
│       └── feature.html
├── templates/base.html  # base layout with nav + flash messages
└── static/styles.css    # basic CSS styling

run.py                   # entry point calling create_app()
requirements.txt         # dependencies
README.md                # setup/run, structure rationale, screenshot, team roles
.gitignore               # ignored files
```

---
## 🔐 Login Page Flow


```
(base.html)
   ↑
   │ extends
(login.html) ←──── render_template() ←──── (auth/routes.py) ←──── (forms.py)
   │
   │ inherits from base.html (nav, flash messages)
   │
   └── needs SECRET_KEY from config.py (for FlaskForm CSRF)

```

### Explanation:

- base.html provides shared layout (nav + flash messages).

- login.html extends base.html and renders the LoginForm.

- auth/routes.py handles /auth/login (GET shows form, POST validates and flashes).

- forms.py defines the LoginForm fields and validation.

- config.py supplies SECRET_KEY for CSRF protection used by Flask-WTF.

---

## 💡 Features (Milestone 1)

* Flask app runs with no errors
* Routes `/`, `/feature`, `/auth/login` render correctly
* WTForms login form validates and flashes “Login not implemented.”
* Static progress bar demo (60 %)
* Base template with navigation and flash message area
* SQLite + SQLAlchemy configured but not used yet

---

## 🎯 Next Steps

* **M2:** Connect database and calculate real progress dynamically
* **M3:** Add dashboards for students and instructors

---

## 📸 Screenshot

Here’s the M1 prototype running locally:


#### Home Page
<img width="437" height="304" alt="Screenshot 2025-11-12 at 12 28 01 AM" src="https://github.com/user-attachments/assets/a1852419-75cd-4d84-a134-bfd638cee1f8" />

#### Feature Page
<img width="437" height="304" alt="Screenshot 2025-11-12 at 12 28 30 AM" src="https://github.com/user-attachments/assets/098b1b33-98f1-4ee9-8505-097abaaffef9" />

#### Login Page
<img width="437" height="304" alt="Screenshot 2025-11-12 at 12 28 46 AM" src="https://github.com/user-attachments/assets/e5ab27cd-e301-4c7d-a3a4-3598d8f3890e" />


#### Login Not implemented
<img width="437" height="304" alt="image" src="https://github.com/user-attachments/assets/63066ee3-6091-44a3-ad87-099e4bf320cb" />

---

# 🖼️ UI Sketches (All Milestones)

Below are the wireframes for TMJ, illustrating the planned UI layout for all project milestones.

---

## **Milestone 1 — Basic Static UI Layout**

### **Home Page Sketch**
![Home Page Sketch](docs/home-page.png)

### **Feature Demo Sketch**
![Feature Demo Sketch](docs/feature-demo.png)

### **Login Page Sketch**
![Login Sketch](docs/login.png)

---

## **Milestone 2 — Dynamic Course Progress Pages**

### **Course In Progress Sketch**
_Shows real-time completion values using database data._
![Course In Progress](docs/course-in-progress.png)

### **Course Completed Sketch**
_Displays when a student finishes all lessons and objectives._
![Course Completed](docs/course-completed.png)

---

## **Milestone 3 — Student Dashboard**

### **Student Dashboard Sketch**
_Overall progress summary, current course details, and upcoming tasks._
![Student Dashboard](docs/user-page.png)

---

## 👥 Team TMJ's Roles (M1)
- **Thao (T)** – Project Lead / Architect: repo setup, `create_app()`, blueprints, README.  
- **Mareli (M)** – Frontend: HTML templates, CSS, progress bar layout.  
- **Jacob (J)** – Backend: WTForms LoginForm, models, form validation logic.

---

## ✅ Milestone 1 Deliverables:

* One-page concept summary (PDF)
* Working Flask scaffold (HTML stubs only)
* Tagged repo release `m1`


