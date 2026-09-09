# 07 — Pagination

Home feed uses SQLAlchemy pagination (5 posts per page) with Previous/Next links.

## Run

```bash
cd projects/flask-blog/07-Pagination
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
python app.py
```

Optional: seed enough posts to see multiple pages:

```bash
flask --app app seed-demo
python app.py
```

Demo login after seeding: `demo@campuswire.test` / `demopass1`.
