# Free Computer Courses — Flask Blog

Original step-by-step Flask blog for [Free Computer Courses](https://freecomputercourses.com). Each numbered folder is a **complete, runnable snapshot** of the app at that stage of the tutorial.

## Snapshots

| Folder | What you learn |
|--------|----------------|
| `01-Getting-Started/` | Minimal Flask app and one route |
| `02-Templates/` | Jinja2 layouts, `render_template`, Bootstrap CDN |
| `03-Forms/` | Flask-WTF forms, validation, flash messages |
| `04-Database/` | SQLite + SQLAlchemy `User` and `Post` models |
| `05-Auth/` | Register, login, logout with Flask-Login |
| `06-Posts/` | Create, edit, and delete your own posts |
| `07-Pagination/` | Paginated home feed |
| `08-Deploy/` | Env-based config and deploy notes |

## How to run any snapshot

From the **snapshot folder** you want to try:

```bash
cd projects/flask-blog/01-Getting-Started   # or 02-Templates, etc.
python3 -m venv .venv
source .venv/bin/activate                   # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

Later snapshots use the same pattern — always install from the shared parent `requirements.txt`:

```bash
pip install -r ../requirements.txt
```

Each folder also has its own `README.md` with exact commands for that stage.

## Curriculum

Site lessons that walk through these snapshots live under the Flask Blog project on Free Computer Courses (see `scripts/projects/flask_blog.py`).
