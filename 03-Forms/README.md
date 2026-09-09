# 03 — Forms

Flask-WTF `PostForm` with title and content fields, validators, and flash messages. Drafts are stored in a Python list (no database yet).

## Run

```bash
cd projects/flask-blog/03-Forms
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
python app.py
```

Open http://127.0.0.1:5000/new, submit a short title/body, and confirm the flash + home list update.
