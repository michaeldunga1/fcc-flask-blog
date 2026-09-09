# 05 — Auth

Flask-Login with register, login, logout, `@login_required` for publishing, and Werkzeug password hashing.

## Run

```bash
cd 05-Auth
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
python app.py
```

1. Open http://127.0.0.1:5000/register and create an account.
2. Log in, then visit `/new` to publish a post.
3. Log out and confirm `/new` redirects to login.
