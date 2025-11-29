# TMJ — Track My Journey  
_A lightweight LMS companion focused on clear progress tracking_

---

## 📘 Overview

TMJ (Track My Journey) is a minimalist LMS prototype designed to help students clearly understand how far they’ve progressed in a course. Many LMS platforms hide progress indicators or bury them in menus, which reduces motivation. TMJ highlights course completion with intuitive progress bars, module breakdowns, and clear completion indicators.

This **Milestone 2** release extends the M1 scaffold into a functional prototype featuring:

- Working login/logout with **Flask-Login**
- Database-backed course and module progress
- A full **Course Detail** page with completion UI
- Updated UI using **AI-generated branding**
- A passing **pytest** test suite

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/ThaoHuynh94/tmj-lms.git
cd tmj-lms
```

## 2. Create & activate a virtual environment
* python -m venv .venv
* source .venv/bin/activate     # Mac/Linux
* .venv\Scripts\activate        # Windows

## 3. Install dependencies
pip install -r requirements.txt

## 4. Run the app
```
python run.py
```

Visit in browser:
👉 http://127.0.0.1:5000/

## 5. Run tests
```
pytest
```


## 🧱 Tech Stack

- Flask (backend + routing)

- Flask-SQLAlchemy (SQLite database)

- Flask-Login (authentication)

- WTForms (form validation)

-  Jinja2 + HTML/CSS (templates & styling)

- pytest (unit testing)

- AI-generated images/video (branding)
 
## 🗂️ Project Structure (M2)

```
app/
├── __init__.py
├── config.py
├── models.py
├── forms.py

├── auth/
│   ├── routes.py
│   └── templates/auth/
│       └── login.html

├── main/
│   ├── routes.py
│   └── templates/main/
│       ├── index.html
│       ├── feature.html
│       └── course_detail.html   ← NEW (M2)

├── templates/
│   └── base.html

└── static/
    ├── styles.css
    ├── img/                    ← NEW (M2)
    │   ├── tmj-logo.png
    │   ├── Home-page.png
    │   ├── feature-hero.png
    │   ├── course-python.png
    │   ├── Completion Badge.png
    ├── video/                  ← NEW (M2)
    │   └── login-hero.mp4

tests/
    └── test_routes.py   ← NEW (M2)

```
## ✨ M2 Features
### 🔐 Login Page (Mareli + Thao)

- Flask-Login session management

- WTForms validation

- Neon-style UI

- AI-generated hero video

###  📊 Dynamic Progress Updates (Jacob)

- SQLAlchemy User/Course/Module models

- Module tracking → course progress calculation

- /courses/<id> shows real progress

### 🎨 Course Detail UI (Thao)

- Course thumbnail

- Progress bar

- Completed & upcoming modules

- Completion banner

- Completion badge (AI image)

###  🏠 UI Enhancements (Thao)

- Homepage hero section

- Feature page hero image

- Updated navigation & layout

- Consistent global CSS design

### 🧪 Unit Tests (M2 Requirement)

Route tests: /, /feature, /auth/login

All tests passing:

```
3 passed in 0.39s

```
###  ✔ Milestone 2 Deliverables Completed

- App runs with no errors

- 70%+ MVP functionality met

- Login/logout functional

- Database-backed progress updates

- All pages extend shared base.html

- New UI for login, feature, and course detail pages

- Passing unit test suite

- Repo tagged as m2


### 👥 Team Roles (Updated for M2)
Thao — UI / Front-End

* Login page HTML/CSS with hero video

* Homepage & Feature page hero sections

* Course Detail UI (progress bar, modules, completion badge)

* Integrated AI-generated images + logo

* Updated base.html layout

* Ensured UI matches sketches

Mareli — Authentication

* WTForms LoginForm

* Login/logout routes

* Flask-Login integration

* Session handling

Jacob — Backend Progress & Models

* SQLAlchemy models (User, Course, Module)

* Course progress calculation

* /courses/<id> backend logic

* Test structure

## 📸 Screenshots 

### Home Page
<img width="715" height="441" alt="Screenshot 2025-11-26 at 4 30 56 PM" src="https://github.com/user-attachments/assets/da78900a-f244-4727-ae96-4b1710e080b6" />

### Feature Page

<img width="715" height="441" alt="Screenshot 2025-11-26 at 4 31 06 PM" src="https://github.com/user-attachments/assets/f7ed03f3-2ee7-482e-95e1-3b9e4d5dc975" />
<img width="715" height="441" alt="Screenshot 2025-11-26 at 4 31 12 PM" src="https://github.com/user-attachments/assets/dee639b3-47f4-4a34-9385-ec615a901b48" />


### Login Page
<img width="715" height="441" alt="Screenshot 2025-11-26 at 4 31 25 PM" src="https://github.com/user-attachments/assets/a828e97f-cfc8-47bb-9410-d3daa0d61f79" />

- (Mareli will add more)

### Course Detail Page

- (Jacob will add more)


## 🎯 Next Steps (M3)

- Student dashboard (multiple courses)

- Instructor dashboard

- Badge/achievement system

- Real-time progress updates

- Improved module flow UX



