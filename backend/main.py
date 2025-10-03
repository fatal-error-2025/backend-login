from fastapi import FastAPI

# Load environment and set dev defaults before importing routers that depend on them
import os
from dotenv import load_dotenv
load_dotenv()

if not os.getenv("SECRET_KEY"):
    # only for local development; use a secure value in production
    os.environ["SECRET_KEY"] = "dev-secret-key"

if not os.getenv("ALGORITHM"):
    os.environ["ALGORITHM"] = "HS256"

if not os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"):
    os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"] = "30"

from . import models, database
from .routes import auth
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Configuración de CORS: permitir orígenes comunes de desarrollo (Vite, CRA, etc.)
DEFAULT_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=DEFAULT_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "API funcionando 🚀"}
