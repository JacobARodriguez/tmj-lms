# seed.py - create demo data for TMJ

from datetime import date
from app import create_app, db
from app.models import User, Course, Module, ModuleNote, ModuleProgress

app = create_app()

with app.app_context():
    # wipe existing tables in the dev DB
    db.drop_all()
    db.create_all()

    # --- 1) Create a demo student user ---
    student = User(username="student1", email="student1@example.com")
    student.set_password("password123")

    db.session.add(student)
    db.session.flush()  # so student.id is available

    # --- 2) Create two courses for that student ---

    python_course = Course(
        user_id=student.id,
        title="Intro to Python",
        progress_percent=0,          # will be updated by logic
        completed_at=None,
    )

    habits_course = Course(
        user_id=student.id,
        title="Study Skills & Habits",
        progress_percent=0,          # will be updated by logic
        completed_at=None,
    )

    db.session.add_all([python_course, habits_course])
    db.session.flush()

    # --- 3) Modules for each course (for notes / future use) ---

    m1 = Module(course_id=python_course.id, title="Getting Started", order_index=1, is_completed=True)
    m2 = Module(course_id=python_course.id, title="Data Types & Variables", order_index=2, is_completed=True)
    m3 = Module(course_id=python_course.id, title="Control Flow", order_index=3, is_completed=True)

    m4 = Module(course_id=habits_course.id, title="Planning your week", order_index=1, is_completed=True)
    m5 = Module(course_id=habits_course.id, title="Deep work sessions", order_index=2, is_completed=False)

    db.session.add_all([m1, m2, m3, m4, m5])
    db.session.flush()

    # --- 4) ModuleProgress rows (this is what feature/course_detail use) ---

    demo_progress = [
        # Intro to Python – fully completed
        ModuleProgress(
            user_id=student.id,
            course_id=python_course.id,
            module_name="Getting Started",
            percent_complete=100,
        ),
        ModuleProgress(
            user_id=student.id,
            course_id=python_course.id,
            module_name="Data Types & Variables",
            percent_complete=100,
        ),
        ModuleProgress(
            user_id=student.id,
            course_id=python_course.id,
            module_name="Control Flow",
            percent_complete=100,
        ),

        # Study Skills & Habits – partially complete
        ModuleProgress(
            user_id=student.id,
            course_id=habits_course.id,
            module_name="Planning your week",
            percent_complete=100,
        ),
        ModuleProgress(
            user_id=student.id,
            course_id=habits_course.id,
            module_name="Deep work sessions",
            percent_complete=20,
        ),
    ]

    db.session.add_all(demo_progress)

    # --- 5) One example module note ---
    note = ModuleNote(
        user_id=student.id,
        module_id=m2.id,
        content="Remember to review list comprehensions before the quiz.",
    )
    db.session.add(note)

    db.session.commit()
    print("Seeded: 1 student, 2 courses, 5 modules, 5 module progress rows, 1 note")
