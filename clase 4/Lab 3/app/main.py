from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE_URL = "postgresql+psycopg2://postgres:admin@db:5432/test_db"
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    return {"message": "¡FastAPI funcionando con Docker Compose!"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"db_status": result.scalar()}
