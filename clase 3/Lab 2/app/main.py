from fastapi import FastAPI, Request, HTTPException
import os
import time

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI debug app"}

@app.get("/env")
def get_env():
    return {"env": dict(os.environ)}

@app.get("/error")
def trigger_error():
    raise ValueError("Este es un error intencional para depuración.")

@app.get("/timeout")
def timeout():
    time.sleep(15)
    return {"message": "Este endpoint se demoró intencionalmente"}

@app.get("/crash")
def crash():
    os._exit(1)  # Termina el proceso (simula crash de la app)

@app.get("/headers")
async def show_headers(request: Request):
    return {"headers": dict(request.headers)}

# Simula consumo excesivo de memoria
memory_list = []

@app.get("/memory-leak")
def memory_leak():
    global memory_list
    for _ in range(10_000_000):
        memory_list.append("leak" * 1000)  # Cada ítem es ~4KB
    return {"message": "Memoria consumida intencionalmente 🚨"}
