from sqlalchemy import (
    Column, BigInteger, String, Boolean, Integer, DateTime, Date
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persona(Base):
    __tablename__ = "persona_natural"
    __table_args__ = {"schema": "bdi"}

    rut = Column(BigInteger, primary_key=True, index=True)
    digito_verificador = Column(String(1), nullable=False)
    nombre = Column(String(8000), nullable=False)
    apellido_paterno = Column(String(8000), nullable=False)
    apellido_materno = Column(String(8000), nullable=False)
    chileno = Column(Boolean)
    fecha_nacimiento = Column(DateTime)
    sexo = Column(String(1))
    id_pueblo_originario = Column(Integer)
    email = Column(String(8000))
    id_pais = Column(Integer)
    id_regimen_conyugal = Column(Integer)
    id_estado_civil = Column(Integer)
    id_nivel_educacional = Column(Integer)
    id_usuario = Column(Integer)
    inicio_actividad = Column(Boolean)
    rut_conyuge = Column(BigInteger)
    id_regimen_conyugal_caracteristica = Column(Integer)
    fecha_defuncion = Column(Date)
    id_pueblo_originario_pertenencia = Column(Integer)
    fecha_actualizacion_registro_civil = Column(DateTime)
    fecha_actualizacion_mideso = Column(DateTime)
    calificacion_socioeconomica = Column(Integer)
    serie = Column(Integer)
    fecha_matrimonio = Column(Date)
    imagen_path = Column(String(100))