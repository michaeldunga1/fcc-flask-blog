# 08 — Deploy

Production-minded Campus Wire: `SECRET_KEY` and optional `DATABASE_URL` from the environment, debug off by default, host/port from env for platforms that inject `PORT`.

## Run locally

```bash
cd 08-Deploy
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
export SECRET_KEY="local-dev-secret"   # Windows PowerShell: $env:SECRET_KEY="local-dev-secret"
export FLASK_DEBUG=1                   # optional; omit in production
python app.py
```

## Deploy (high level)

### Shared checklist

1. Generate a long random `SECRET_KEY` and set it as an environment variable (never commit it).
2. Prefer a managed Postgres URL in `DATABASE_URL` for real hosting; SQLite is fine for demos.
3. Install dependencies from `../requirements.txt` (add `gunicorn` on Linux hosts).
4. Run table creation once (`db.create_all()` already runs on import here; use migrations for larger apps).
5. Serve with a WSGI server, for example: `gunicorn -b 0.0.0.0:$PORT app:app`.

### Render

- Create a Web Service from this repo folder (or monorepo root with the correct root directory).
- Build: `pip install -r requirements.txt` (point at this project's requirements).
- Start: `gunicorn app:app`.
- Set `SECRET_KEY` (and `DATABASE_URL` if using Render Postgres).

### Railway

- New project → deploy from GitHub.
- Set `SECRET_KEY`; attach a Postgres plugin and map its URL to `DATABASE_URL` if needed.
- Start command: `gunicorn app:app`.

### VPS (Ubuntu-style)

- Create a non-root user, clone the repo, create a venv, install requirements + gunicorn.
- Put `SECRET_KEY` in a systemd unit `Environment=` line or an env file with restricted permissions.
- Reverse-proxy with nginx/caddy to the gunicorn bind address.
- Enable HTTPS (Let's Encrypt) before accepting real users.

This snapshot is intentionally small — treat it as a teaching scaffold, not a hardened production checklist.
