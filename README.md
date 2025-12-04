# 📚 TMJ — Track My Journey (LMS Prototype)

**TMJ (Track My Journey)** is a lightweight learning management prototype focused on **clear visual progress**, **module notes**, and **motivation tools** such as streaks and reminders.

---

## 🟢 Current Status

* **Milestone 1:** ✔ Complete
* **Milestone 2:** ✔ ~70% Complete

---

## 🚀 How to Run Locally

To get the project up and running on your local machine:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/ThaoHuynh94/tmj-lms.git](https://github.com/ThaoHuynh94/tmj-lms.git)
    cd tmj-lms
    ```

2.  **Set up Virtual Environment**
    ```bash
    python -m venv .venv
    # Activate for Mac/Linux
    source .venv/bin/activate
    # Activate for Windows
    .venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    python run.py
    ```

**Then open:**

👉 http://127.0.0.1:5000/

---

## 🧱 Tech Stack

The prototype is built using the following technologies:

* **Framework:** Flask
* **Database:** Flask-SQLAlchemy (ORM) / SQLite
* **Authentication:** Flask-Login
* **Forms:** Flask-WTF / WTForms
* **Frontend:** HTML / CSS / Jinja2

---

## 🗂️ Project Structure

The application structure follows a standard Flask blueprint pattern:
```
app/
├── __init__.py         # app factory, DB + Login manager setup
├── config.py           # configuration (SECRET_KEY, DB URI)
├── models.py           # User, Course, Module, ModuleNote
├── forms.py            # LoginForm, ModuleNoteForm
│
├── auth/
│   ├── routes.py       # /auth/login
│   └── templates/auth/
│       └── login.html  # login page
│
├── main/
│   ├── routes.py       # /, /feature, /courses/<id>
│   └── templates/main/
│       ├── index.html
│       ├── feature.html
│       └── course_detail.html
│
├── templates/
│   └── base.html       # shared layout, navbar, flash messages
│
└── static/
    ├── styles.css
    ├── img/
    └── video/

```

---

## 🟩 Milestone 2 — Status Summary

Milestone 2 requires **6+ key features**. Here is the current implementation status:

| # | Feature | Status | Notes |
| :--- | :--- | :--- | :--- |
| **1** | Student logs in/out | **🔄 In Progress** | UI + Forms ready. Remaining: real password check, login/logout logic, `user_loader`. |
| **2** | Student views all course progress | **🔄 In Progress** | Models and UI ready. Remaining: backend route + real data integration. |
| **3** | Student views one course’s details | **✅ UI Complete** | `/courses/<id>` route, progress bar, module list, completion badge, safe fallback data. |
| **4** | Student earns badges | **✅ UI Complete** | Badge + completion banner UI implemented. Logic is a placeholder. |
| **5** | Student writes module notes | **✅ Fully Implemented** | `ModuleNote` model, `ModuleNoteForm`, save/update logic, notes textarea + preview. |
| **6** | Student views streak progress | **🟨 UI Placeholder Ready** | Streak display UI styled. Waiting for backend to supply `streak_days`. |
| **7** | System sends progress reminders | **🟨 UI Placeholder Ready** | Reminder banner UI added. Displays when backend provides `reminder_message`. |

---

## 👥 Team Roles (M2)

| Role | Team Member | Responsibilities |
| :--- | :--- | :--- |
| **UI / Front-End** | Thao | Login/Homepage/Feature page hero, Course Detail UI, Module Notes, Streak/Reminder UI, Global CSS, Unit tests, README. |
| **Authentication** | Mareli | WTForms, Login/logout routes, Flask-Login integration, Session handling, `user_loader` + password verification. |
| **Backend Progress & Models** | Jacob | SQLAlchemy models, Course progress calculation, `/courses/<id>` backend logic, Streak logic & reminders, Data integration. |

---

## 🎨 Deliverables & Enhancements

### **User Interface (Thao)**
* Course Detail UI (Thumbnail, Progress bar, Modules, Completion banner/badge, Module notes, Streak/reminder placeholders).
* Homepage hero, Feature page hero, updated navigation.
* Global CSS redesign and consistent site layout.

### **Authentication (Mareli + Thao)**
* Flask-Login session scaffolding.
* WTForms validation.
* Neon-style UI and AI-generated hero video for the login page.

### **Dynamic Progress Updates (Jacob)**
* SQLAlchemy models for progress.
* Module $\to$ course progress calculation logic.
* Backend hooks for `/courses/<id>` (in progress).

### **🧪 Unit Tests (M2 Requirement)**
All tests are passing:
3 passed in 0.39s

Routes tested: `/`, `/feature`, `/auth/login`.

---

## ✔ Milestone 2 Deliverables Completed

* App runs with no errors.
* 70%+ functionality complete.
* Login UI functional (backend pending).
* Course detail page complete.
* Module Notes fully implemented.
* Badge UI implemented.
* Streak + reminders UI ready.
* All pages extend `base.html`.
* Unit test suite passing.
* Repo tagged as `m2`.

---

## 📸 Screenshots

| Page | Screenshots |
| :--- | :--- |
| **Home Page** | <img width="715" height="441" src="https://github.com/user-attachments/assets/da78900a-f244-4727-ae96-4b1710e080b6" /> |
| **Feature Page** | <img width="715" height="441" alt="image" src="https://github.com/user-attachments/assets/7fe4c944-718d-4093-b40a-4dc81d4a5768" /> <img width="715" height="441" src="https://github.com/user-attachments/assets/dee639b3-47f4-4a34-9385-ec615a901b48" /> |
| **Login Page** | <img width="715" height="441" src="https://github.com/user-attachments/assets/a828e97f-cfc8-47bb-9410-d3daa0d61f79" /> |
| **Course Detail Page** | *(More screenshots will be added once backend data is wired in)* |

---

## 🎯 Next Steps (M3)

* Student dashboard (multiple courses).
* Instructor dashboard.
* Achievement/badge system.
* Real-time progress updates.
* Improved module navigation UX.
