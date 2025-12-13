# 📚 TMJ — Track My Journey (Final MVP – Milestone 3)

**TMJ (Track My Journey)** is a lightweight LMS companion that gives students clear visibility into their learning progress. TMJ enhances traditional LMS platforms by providing:

* **Visual course progress bars**
* **Module-level progress tracking**
* **Completion badges**
* **Personal notes per module**
* **Streak tracking**
* **Reminder prompts** to encourage consistent study habits

This repository contains the Milestone 3 (**Final Release**) of the TMJ project.

---

## 🟢 Project Status

| Milestone | Status | Notes |
| :--- | :--- | :--- |
| **M1 — Prototype** | ✔ Complete | |
| **M2 — Functional Prototype** | ✔ 100% Complete | All 7 required features implemented. |
| **M3 — Final MVP** | ✔ Complete | Authentication, dashboard, UI polish, test suite, and final documentation. |

---

## 🚀 How to Run Locally

To get the project up and running on your local machine:

1.  ### Clone the Repository
    ```bash
    git clone [https://github.com/ThaoHuynh94/tmj-lms.git](https://github.com/ThaoHuynh94/tmj-lms.git)
    cd tmj-lms
    ```

2.  ### Create & Activate Virtual Environment
    ```bash
    python -m venv .venv
    # Mac/Linux
    source .venv/bin/activate
    # Windows
    .venv\Scripts\activate
    ```

3.  ### Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

4.  ### Seed the Demo Database
    ```bash
    python seed.py
    ```

5.  ### Run the Application
    ```bash
    python run.py
    ```

**Open the application at:**

👉 http://127.0.0.1:5000/


6. ### Demo Login
* **Username:**  student1
* **Password:**  password123

---

## 🧱 Tech Stack

| **Component**         | **Technology**             |
| --------------------- | -------------------------- |
| 🖥 **Backend**        | Flask                      |
| 🗄 **Database**       | SQLite + SQLAlchemy ORM    |
| 🔐 **Authentication** | Flask-Login                |
| 📝 **Forms**          | Flask-WTF + WTForms        |
| 🧩 **Templates**      | Jinja2                     |
| 🎨 **Styling**        | Custom CSS                 |
| 🧪 **Testing**        | pytest + Flask test client |


---

## 🗂️ Project Structure

The structure follows a clean Flask blueprint pattern:
---

## 🗂️ Project Structure

```
app/
├── __init__.py          # App factory + DB + Login setup
├── config.py            # App configuration
├── models.py            # User, Course, Module, ModuleProgress, ModuleNote
├── forms.py             # Forms: LoginForm, ModuleNoteForm
│
├── auth/
│   ├── routes.py        # Login + logout logic
│   └── templates/auth/login.html
│
├── main/
│   ├── routes.py        # /, /feature (dashboard), /courses/<id>
│   └── templates/main/
│       ├── index.html
│       ├── feature.html
│       └── course_detail.html
│
├── templates/base.html  # Shared layout, navbar, flash messages
│
└── static/
    ├── styles.css
    ├── img/
    └── video/

```

---
## 🟩 Milestone 3 Features — MVP Complete

### ✔ Authentication
* Secure login + logout.
* **Dashboard requires login** (Implemented for M3).
* Personalized streak + reminder based on activity.

### ✔ Dashboard (`/feature`)
* Shows **only the logged-in student's courses**.
* Real-time progress calculation from `ModuleProgress`.
* Streak + inactivity reminder display.

### ✔ Course Detail Page
* Per-module progress.
* Notes (save + update).
* Completion badge + banner.
* Streak + reminder display.

### ✔ UI/UX Enhancements
* Full custom design system implemented.
* Consistent navbar + flash messages.
* Dashboard and detail pages redesigned for clarity.
* Status pill styling corrected (`completed` / `in-progress`).

### ✔ Testing (16 Tests)
* Unit tests for forms & models.
* Integration tests for login, logout, dashboard, notes, and protected routes.
* 404 custom page tested.
* **87% coverage.**
---
## Test Results (M3)
All tests pass:
```
16 passed, 0 failed
```
### Coverage Report
Generated using:

```
pytest --cov=app --cov-report=term-missing
```

```
=============================== tests coverage ================================
_______________ coverage: platform darwin, python 3.11.5-final-0 _______________

Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
app/__init__.py           21      0   100%
app/auth/__init__.py       0      0   100%
app/auth/routes.py        46      8    83%   38, 94-102
app/config.py              6      0   100%
app/forms.py              11      0   100%
app/main/__init__.py       0      0   100%
app/main/routes.py        78     11    86%   36-37, 42-43, 50, 69, 73, 105-116, 170
app/models.py             62      6    90%   45, 72, 75, 97, 114, 140
app/run.py                 4      4     0%   1-5
----------------------------------------------------
TOTAL                    228     29    87%
======================== 16 passed, 3 warnings in 1.42s ========================


```
### Coverage Summary (for reports)
* **Total Coverage:** ~87%

* **Routes:** ~85–100% covered

* **Models:** ~90% covered

* **Forms:** 100%

* **Integration tests:** login, logout, dashboard, detail view, notes, 404

---

## 📸 Screenshots

Below are key pages of the TMJ — Track My Journey prototype, including the fully implemented multi-course progress dashboard and course detail interface.

---

### 🏠 Home Page
<img width="715" height="441" alt="Screenshot 2025-12-07 at 1 28 09 PM" src="https://github.com/user-attachments/assets/37509967-2a4f-4229-8faa-d5c08377f531" />

---

### 🔐 Login Page
<img width="715" height="441" alt="image" src="https://github.com/user-attachments/assets/9118e422-2157-43d6-8fd6-5aca82eac82b" />

---

## 📊 Feature Page — Multi-Course Progress Dashboard

| Course | Screenshot |
|--------|------------|
| **Intro to Python — Full Course Completion** | <img width="500" height="1000" alt="Screenshot 2025-12-07 at 12 38 15 PM" src="https://github.com/user-attachments/assets/284045b1-a170-4563-b156-4f46cab02032" />|
| **Study Skills & Habits — Partial Progress** | <img width="500" height="1000" alt="Screenshot 2025-12-07 at 1 05 38 PM" src="https://github.com/user-attachments/assets/8a72b80f-fec5-4a51-885f-90a3b8cf2790" />|
| **Time Management Essentials — Early Progress** | <img width="500" height="1000" alt="Screenshot 2025-12-07 at 1 06 01 PM" src="https://github.com/user-attachments/assets/104c977c-3d1a-4afd-a646-712e2e0bd788" />|
| **Effective Note-Taking — Mixed Completion** | <img width="500" height="1000" alt="Screenshot 2025-12-07 at 1 06 13 PM" src="https://github.com/user-attachments/assets/93fade41-0973-4f6a-b7da-e2044d2c8c78" />|
| **Mindfulness for Students — Low Progress** | <img width="500" height="1000" alt="Screenshot 2025-12-07 at 1 06 24 PM" src="https://github.com/user-attachments/assets/975c84ee-b84c-4288-87d4-39dc20666217" />|

---

## 🧠 Course Detail Page — Per-Module Progress, Notes, Badge, Streak & Reminder
<img width="1200" height="1000" alt="Screenshot 2025-12-07 at 1 33 59 PM" src="https://github.com/user-attachments/assets/b2184e01-34ef-43c4-bb8d-9350da3c1a22" />
<img width="1200" height="1000" alt="Screenshot 2025-12-07 at 1 51 36 PM" src="https://github.com/user-attachments/assets/901e54a8-b4e4-447c-9620-6596bbb889a3" />
<img width="1200" height="1000" alt="Screenshot 2025-12-07 at 1 51 44 PM" src="https://github.com/user-attachments/assets/dc7829e9-a892-4ee0-ac4d-7debc11325bf" />

---

## 🎯 Next Steps (Stretch Goals)

These features were planned but not required for M3:

Instructor dashboard

Expanded badge/achievement system

Real-time progress updates

Improved module navigation

Calendar-based streak visualization

---
## 🏁 Final Release Tag

Milestone 3 is tagged as:

```
git tag m3
git push --tags
```
