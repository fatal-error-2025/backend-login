# Backend login service

Setup (local development):

1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and adjust values if needed.

3. Run the app:

```bash
uvicorn backend.main:app --reload --port 8000
```

Notes:
- The app uses SQLite by default if you set `DATABASE_URL=sqlite:///./test.db` in `.env`.
- For production, set a strong `SECRET_KEY`, configure the database and tighten CORS.