from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, init_db
from app import crud

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "¡FastAPI funcionando con Docker Compose!"}

@app.get("/2")
def read_root():
    return {"message": "¡FastAPI 2!"}

@app.get("/personas/{rut}")
def listar(rut: int, db: Session = Depends(get_db)):
    return crud.obtener_persona_por_rut(db, rut)

@app.get("/personas")
def listar(db: Session = Depends(get_db)):
    return crud.obtener_personas(db)
