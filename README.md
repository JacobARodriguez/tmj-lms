# 📚 TMJ — Track My Journey (LMS Prototype)

**TMJ (Track My Journey)** is a lightweight LMS companion focused on **clear visual course progress**, **module notes**, **completion badges**, **streak tracking**, and **reminder prompts** to keep students motivated.

---

## 🟢 Current Status

* **Milestone 1:** ✔ Complete
* **Milestone 2:** ✔ 100% Complete — All 7 required features implemented!

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

---

## 🧱 Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend Framework** | Flask | Lightweight Python web framework. |
| **Database** | SQLite + Flask-SQLAlchemy | ORM for handling models and data. |
| **Authentication** | Flask-Login | Secure session management. |
| **Forms** | Flask-WTF / WTForms | Form generation and validation. |
| **Templating** | Jinja2 | Used for dynamic HTML generation. |
| **Frontend** | HTML + CSS | Custom design system for the UI. |

---

## 🗂️ Project Structure

The structure follows a clean Flask blueprint pattern:
---

## 🗂️ Project Structure

The application structure follows a standard Flask blueprint pattern:
```
app/
├── __init__.py          # App factory + DB + Login setup
├── config.py            # Secret key + DB URI
├── models.py            # User, Course, Module, ModuleNote, ModuleProgress
├── forms.py             # LoginForm, ModuleNoteForm
│
├── auth/
│   ├── routes.py        # Login + logout
│   └── templates/auth/login.html
│
├── main/
│   ├── routes.py        # /, /feature, /courses/<id>
│   └── templates/main/
│       ├── index.html
│       ├── feature.html
│       └── course_detail.html
│
├── templates/base.html  # Layout, navbar, flash messages
│
└── static/
    ├── styles.css
    ├── img/             # course thumbnails + branding
    └── video/


```

---

## 🟩 Milestone 2 — All 7 Required Features (✔ COMPLETE)

| # | Feature | Status | Description |
| :--- | :--- | :--- | :--- |
| **1** | Student logs in/out | **✔ Complete** | Secure login/logout with hashed passwords, session handling, `user_loader`. |
| **2** | Student views all course progress | **✔ Complete** | Multi-course dashboard on Feature page showing progress, streak, reminders. |
| **3** | Student views one course’s details | **✔ Complete** | Course detail page with progress, modules, badge, notes, streak, reminder. |
| **4** | Student earns badges | **✔ Complete** | Auto-display of completion banner + badge when progress hits 100%. |
| **5** | Student writes module notes | **✔ Complete** | Notes saved per-user per-module with editable textarea + preview. |
| **6** | Student views streak progress | **✔ Complete** | Streak calculated on login + displayed across pages. |
| **7** | System sends progress reminders | **✔ Complete** | Reminder banner shows when user inactive $\geq 3$ days (dynamic backend logic). |

---

## 👥 Team Roles (M2)

| Role | Team Member | Key Responsibilities |
| :--- | :--- | :--- |
| **UI / Front-End** | Thao | All major UI/UX, Global CSS, Multi-course dashboard, Course Detail UI, Module Notes, Streak/Reminder UI, Unit tests, `seed.py` demo database. |
| **Documentation** | Thao | Wrote the full **Milestone 2 2-page PDF deliverable**, including Updated Concept Overview, 7 Use Cases, Implementation Summary, and Testing Plan. Also authored and maintained the README. |
| **Authentication** | Mareli | WTForms LoginForm, Login/Logout routes, Password hashing, Flask-Login integration, Session handling. |
| **Backend Progress & Models** | Jacob | SQLAlchemy models, ModuleProgress logic, Course progress calculation, Streak logic, Reminder logic, Dynamic backend routes. |


---

## 🎨 Deliverables & Enhancements

### **User Interface (Thao)**
* **Course Detail UI:** Dynamic thumbnails (5 images), progress bar/status, module progress list, completion badge + banner, module notes section, streak + reminder UI.
* **Layout:** Homepage/Feature hero, updated global navbar, multi-course progress dashboard layout.
* **Styling:** Global CSS redesign and responsive improvements.

### **Data Seeding & Setup (Thao)**
* Built **`seed.py`** to initialize real demo data (1 student, 5 courses, progress records, notes, streak/reminder data).
* Ensured the entire application runs cleanly and displays dynamic data upon execution.

### **Dynamic Progress, Streaks & Reminders (Jacob)**
* Implemented **`ModuleProgress`** model for granular tracking.
* Logic for **course progress calculation** (percentage).
* **Streak logic** updated on user login.
* **Reminder logic** (checks for inactivity $\geq 3$ days).
* Multi-course backend integration for `/feature` and `/courses/<id>`.

### **Authentication (Mareli + Thao)**
* Complete Flask-Login integration.
* Secure password hashing and verification.
* WTForms `LoginForm` implementation.
* Neon-style login UI with hero video.

### **🧪 Testing**
All tests pass:
```bash
================================ test session starts ========================================================
platform darwin -- Python 3.11.5, pytest-9.0.0, pluggy-1.6.0
rootdir: /Users/iris/tmj-lms
plugins: anyio-3.5.0, cov-7.0.0
collected 12 items                                                                                                                                                                                         

tests/test_forms.py ...                                                                                                                                                                              [ 25%]
tests/test_models.py ...                                                                                                                                                                             [ 50%]
tests/test_routes.py ......                                                                                                                                                                          [100%]

=================================warnings summary ==============================================================
tests/test_routes.py::test_course_detail_after_login_with_progress
tests/test_routes.py::test_course_detail_after_login_with_progress
  /Users/iris/tmj-lms/app/__init__.py:30: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    return User.query.get(int(user_id))

tests/test_routes.py::test_course_detail_after_login_with_progress
  /Users/iris/anaconda3/lib/python3.11/site-packages/flask_sqlalchemy/query.py:30: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    rv = self.get(ident)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================= 12 passed in 0.95s =================================================
```

**Routes tested:**  
- `/` – Home page  
- `/feature` – Multi-course dashboard  
- `/auth/login` – Login (GET + POST)  
- `/auth/logout` – Logout flow  
- `/courses/<id>` – Redirect when not logged in + render when authenticated  

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

## 🎯 Next Steps (M3)

* Student dashboard (multiple courses).
* Instructor dashboard.
* Achievement/badge system.
* Real-time progress updates.
* Improved module navigation UX.
