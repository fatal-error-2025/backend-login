from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, tasks
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS para frontend en localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(auth.router)
app.include_router(tasks.router)
