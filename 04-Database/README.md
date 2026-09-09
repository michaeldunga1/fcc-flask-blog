# 04 — Database

SQLite + Flask-SQLAlchemy with `User` and `Post` models. Tables are created on startup and sample data is seeded when the database is empty.

## Run

```bash
cd projects/flask-blog/04-Database
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
python app.py
```

Open http://127.0.0.1:5000/ to see posts loaded from `instance/campus_wire.db` (or `campus_wire.db` depending on Flask/SQLAlchemy version).

## Optional shell exploration

```bash
python
>>> from app import app, db, User, Post
>>> app.app_context().push()
>>> User.query.all()
>>> Post.query.all()
```

To reset, delete the SQLite file and run `python app.py` again.
