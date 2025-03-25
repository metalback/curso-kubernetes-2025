from fastapi import FastAPI
import httpx
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

@app.get("/")
def root():
    return {"service": "A", "status": "ok"}

@app.get("/check-b")
def check_b():
    try:
        host = os.getenv("SERVICE_B_HOST", "service_b")
        port = os.getenv("SERVICE_B_PORT", "8001")
        response = httpx.get(f"http://{host}:{port}/ping", timeout=5)
        return {"from": "A", "to": "B", "status": response.status_code, "response": response.json()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/check-db")
def check_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "db"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            user=os.getenv("POSTGRES_USER", "user"),
            password=os.getenv("POSTGRES_PASSWORD", "pass"),
            dbname=os.getenv("POSTGRES_DB", "appdb"),
            cursor_factory=RealDictCursor
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        conn.close()
        return {"status": "ok", "db_version": version}
    except Exception as e:
        return {"error": str(e)}
