# app/main.py
from fastapi import FastAPI
from .api import router  # importa do api.py

app = FastAPI()
app.include_router(router)
