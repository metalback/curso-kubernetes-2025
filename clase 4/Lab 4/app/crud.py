from sqlalchemy.orm import Session
from app.models import Persona
from typing import List, Optional

def crear_cliente(db: Session, nombre: str, email: str):
    cliente = Persona(nombre=nombre, email=email)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def obtener_personas(db: Session, offset: int = 0, limit: int = 10) -> List[Persona]:
    return (
        db.query(Persona)
        .order_by(Persona.rut)
        .offset(offset)
        .limit(limit)
        .all()
    )

def obtener_persona_por_rut(db: Session, rut: int) -> Optional[Persona]:
    return db.query(Persona).filter(Persona.rut == rut).first()

def crear_persona(db: Session, persona: Persona) -> Persona:
    db.add(persona)
    db.commit()
    db.refresh(persona)
    return persona

def actualizar_persona(db: Session, rut: int, nuevos_datos: dict) -> Optional[Persona]:
    persona = db.query(Persona).filter(Persona.rut == rut).first()
    if persona:
        for clave, valor in nuevos_datos.items():
            setattr(persona, clave, valor)
        db.commit()
        db.refresh(persona)
    return persona

def eliminar_persona(db: Session, rut: int) -> bool:
    persona = db.query(Persona).filter(Persona.rut == rut).first()
    if persona:
        db.delete(persona)
        db.commit()
        return True
    return False