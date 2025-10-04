# Plan My Weather - Backend Login 🔑

This is the **backend-login service** for **Plan My Weather**, built with **FastAPI** and **PostgreSQL (Neon)**.  
It handles user authentication (login and registration) and management of personal weather-related tasks.

---

## Features

- 📧 User registration and login  
- 🌦️ CRUD operations for personal weather plans/tasks  
- 🐘 PostgreSQL database hosted on **Neon**  
- 🔄 CORS enabled for frontend communication  
- 🐍 Written in Python 3.11+  

---

## Getting Started

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
