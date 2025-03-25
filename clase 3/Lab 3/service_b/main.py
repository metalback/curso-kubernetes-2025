from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"service": "B", "message": "pong desde B"}
