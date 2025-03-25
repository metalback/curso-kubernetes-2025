from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola FastAPI en Docker con live reload!"}

@app.get("/test")
def read_root():
    return {"message": "Hola FastAPI este es un test!"}
