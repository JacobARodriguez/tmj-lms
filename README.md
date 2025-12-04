TMJ — Track My Journey (LMS Prototype)

TMJ (Track My Journey) is a lightweight learning management prototype focused on clear visual progress, module notes, and motivation tools such as streaks and reminders.

Current status:
Milestone 1: ✔ Complete
Milestone 2: ✔ ~70% Complete

🚀 How to Run Locally
```
git clone https://github.com/ThaoHuynh94/tmj-lms.git
cd tmj-lms

python -m venv .venv
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows

pip install -r requirements.txt

python run.py
```


Then open:

👉 http://127.0.0.1:5000/

🧱 Tech Stack

Flask

Flask-SQLAlchemy

Flask-Login

Flask-WTF / WTForms

SQLite

HTML / CSS / Jinja2

🗂️ Project Structure

```
app/
├── __init__.py
├── config.py
├── models.py
├── forms.py
│
├── auth/
│   ├── routes.py
│   └── templates/auth/login.html
│
├── main/
│   ├── routes.py
│   └── templates/main/
│       ├── index.html
│       ├── feature.html
│       └── course_detail.html
│
├── templates/base.html
└── static/
    ├── styles.css
    ├── img/
    └── video/
```

Top-level:
```
run.py
requirements.txt
README.md
```

🟩 Milestone 2 — ~70% Complete

The project requires 7 key features.
Here is the current status of each:

1) Student logs in/out — 🔄 In Progress

Login page UI + WTForms + CSRF

Flask-Login integrated

Remaining: real password check, login/logout, user_loader

2) Student views all course progress — 🔄 In Progress

Models support progress

UI ready

Remaining: backend route + real data

3) Student views one course’s details — ✅ UI Complete

/courses/<id> route

Progress bar

Module list

Completion badge

Safe fallback demo data

4) Student earns badges — ✅ UI Complete

Badge + completion banner

Placeholder logic until backend connects

5) Student writes module notes — ✅ Fully Implemented

ModuleNote model

ModuleNoteForm

Save + update logic

Notes textarea + “last saved note” preview

6) Student views streak progress — 🟨 UI Placeholder Ready

Streak UI display implemented

CSS styled

Shows real streak when backend supplies streak_days

7) System sends progress reminders — 🟨 UI Placeholder Ready

Reminder banner UI added

Automatically displays when backend provides reminder_message

🎨 UI Features (Thao)
🔐 Login Page (Mareli + Thao)

Flask-Login session scaffolding

WTForms validation

Neon-style UI

AI-generated hero video

📊 Dynamic Progress Updates (Jacob)

SQLAlchemy models

Module → course progress logic

/courses/<id> backend hooks (in progress)

🎨 Course Detail UI (Thao)

Course thumbnail

Progress bar

Completed & upcoming modules

Completion banner

Completion badge (AI-generated)

Module notes feature

Streak + reminder UI placeholders

🏠 UI Enhancements (Thao)

Homepage hero

Feature page hero

Updated navigation

Global CSS redesign

Consistent site layout

🧪 Unit Tests (M2 Requirement)

All tests passing:

```
3 passed in 0.39s
```

Routes tested: /, /feature, /auth/login

✔ Milestone 2 Deliverables Completed

App runs with no errors

70%+ functionality complete

Login UI functional (backend pending)

Course detail page complete

Module Notes fully implemented

Badge UI implemented

Streak + reminders UI ready

All pages extend base.html

Unit test suite passing

Repo tagged as m2

👥 Team Roles (Updated for M2)
Thao — UI / Front-End

Login page HTML/CSS + hero video

Homepage hero

Feature page hero

Course Detail UI

Module Notes feature

Streak/reminder UI placeholders

Global CSS + assets

README updates

Unit tests

Mareli — Authentication

WTForms LoginForm

Login/logout routes

Flask-Login integration

Session handling

user_loader + password verification

Jacob — Backend Progress & Models

SQLAlchemy models

Course progress calculation

/courses/<id> backend logic

Streak logic & reminders

Data integration for templates

📸 Screenshots
Home Page
<img width="715" height="441" src="https://github.com/user-attachments/assets/da78900a-f244-4727-ae96-4b1710e080b6" />
Feature Page
<img width="715" height="441" src="https://github.com/user-attachments/assets/f7ed03f3-2ee7-482e-95e1-3b9e4d5dc975" /> <img width="715" height="441" src="https://github.com/user-attachments/assets/dee639b3-47f4-4a34-9385-ec615a901b48" />
Login Page
<img width="715" height="441" src="https://github.com/user-attachments/assets/a828e97f-cfc8-47bb-9410-d3daa0d61f79" />
Course Detail Page

(More screenshots will be added once backend data is wired in)

🎯 Next Steps (M3)

Student dashboard (multiple courses)

Instructor dashboard

Achievement/badge system

Real-time progress updates

Improved module navigation UX
