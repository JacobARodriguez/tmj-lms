# seed.py - create demo data for TMJ (Milestone 2)

from datetime import date, timedelta

from app import create_app, db
from app.models import User, Course, Module, ModuleNote, ModuleProgress

# Create the Flask app and push an app context
app = create_app()

with app.app_context():
    # Start fresh each time: drop and recreate all tables
    db.drop_all()
    db.create_all()

    # -------------------------------------------------
    # 1) Demo student user
    # -------------------------------------------------
    student = User(username="student1", email="student1@example.com")
    student.set_password("password123")

    # Demo streak/reminder data:
    # - streak_days: how many days in a row they studied
    # - last_active_date: a few days ago so the reminder banner can show
    student.streak_days = 3
    student.last_active_date = date.today() - timedelta(days=4)

    db.session.add(student)
    db.session.flush()  # so student.id is available

    # -------------------------------------------------
    # 2) Two demo courses
    # -------------------------------------------------
    python_course = Course(
        user_id=student.id,
        title="Intro to Python",
        progress_percent=0,      # will be updated by logic
        completed_at=None,
    )

    habits_course = Course(
        user_id=student.id,
        title="Study Skills & Habits",
        progress_percent=0,      # will be updated by logic
        completed_at=None,
    )

    db.session.add_all([python_course, habits_course])
    db.session.flush()  # so course ids are available

    # -------------------------------------------------
    # 3) Modules for each course
    #    (used for notes; progress uses ModuleProgress below)
    # -------------------------------------------------
    m1 = Module(
        course_id=python_course.id,
        title="Getting Started",
        order_index=1,
        is_completed=True,
    )
    m2 = Module(
        course_id=python_course.id,
        title="Data Types & Variables",
        order_index=2,
        is_completed=True,
    )
    m3 = Module(
        course_id=python_course.id,
        title="Control Flow",
        order_index=3,
        is_completed=True,
    )

    m4 = Module(
        course_id=habits_course.id,
        title="Planning your week",
        order_index=1,
        is_completed=True,
    )
    m5 = Module(
        course_id=habits_course.id,
        title="Deep work sessions",
        order_index=2,
        is_completed=False,
    )

    db.session.add_all([m1, m2, m3, m4, m5])
    db.session.flush()

    # -------------------------------------------------
    # 4) ModuleProgress rows
    #    (what /feature and /courses/<id> actually use)
    # -------------------------------------------------
    demo_progress = [
        # Intro to Python – fully complete
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

    # -------------------------------------------------
    # 5) One example module note
    #    (for the FIRST module so course_detail finds it)
    # -------------------------------------------------
    note = ModuleNote(
        user_id=student.id,
        module_id=m1.id,  # first module of Intro to Python
        content="Remember to review list comprehensions before the quiz.",
    )
    db.session.add(note)

    # -------------------------------------------------
    # 6) Commit everything
    # -------------------------------------------------
    db.session.commit()

    print(
        "Seeded: 1 student, 2 courses, 5 modules, "
        "5 module progress rows, 1 note (with streak + reminder demo data)"
    )
