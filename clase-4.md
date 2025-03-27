# 📚 Clase 4: Introducción a Docker Compose

## 🔹 Estructura de la Clase

### 🔸 1. Teoría

#### ✅ 1.1 ¿Qué es Docker Compose?

**Concepto Clave:**
Docker Compose permite definir y ejecutar aplicaciones **multi-contenedor** mediante un solo archivo YAML.

**¿Por qué usar Docker Compose?**
* ✔ Facilita la gestión de aplicaciones con múltiples servicios (ejemplo: backend + base de datos).
* ✔ Permite ejecutar entornos completos con un solo comando (`docker-compose up`).
* ✔ Define volúmenes y redes de manera estructurada.

**Ejemplo de una aplicación sin Docker Compose:**
```sh
docker network create mi-red
docker run -d --name db --network mi-red -e POSTGRES_PASSWORD=admin postgres
docker run -d --name app --network mi-red mi-backend
```
**Problema:** Es complicado de manejar y escalar.

**Ejemplo de la misma aplicación con Docker Compose:**
```yaml
version: "3.8"
services:
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: admin
    networks:
      - mi-red
  
  app:
    image: mi-backend
    depends_on:
      - db
    networks:
      - mi-red

networks:
  mi-red:
```
**Ventaja:** Se ejecuta con un solo comando:
```sh
docker-compose up -d
```

#### ✅ 1.2 Sintaxis de Docker Compose

**Estructura básica de `docker-compose.yml`**
```yaml
version: "3.8"
services:
  <nombre-del-servicio>:
    image: <imagen>
    build: <directorio-con-dockerfile>
    ports:
      - "puerto-local:puerto-contenedor"
    environment:
      VARIABLE: "valor"
    volumes:
      - "volumen-host:volumen-contenedor"
    networks:
      - <nombre-red>
```
**Principales componentes:**
* ✔ **services** → Define los contenedores a ejecutar.
* ✔ **image** → Especifica una imagen existente o un `build` propio.
* ✔ **ports** → Define los puertos expuestos.
* ✔ **environment** → Establece variables de entorno.
* ✔ **volumes** → Permite persistencia de datos.
* ✔ **networks** → Define redes personalizadas.

#### ✅ 1.3 Principales Comandos de Docker Compose

**Comandos esenciales:**
```sh
docker-compose up -d       # Levantar los servicios en modo "detached"
docker-compose down        # Detener y eliminar los servicios
docker-compose ps          # Ver contenedores en ejecución
docker-compose logs -f     # Ver logs en tiempo real
docker-compose restart     # Reiniciar los servicios
```
**Ejemplo:** Iniciar un servicio con logs en vivo:
```sh
docker-compose up --build
```

---

## 🔹 2. Práctica en KillerCoda

### **Lab 1: Creación de un Docker Compose básico**

**Objetivo:** Definir y ejecutar una aplicación con un backend en FastAPI conectado a una base de datos PostgreSQL.

Abrir el entorno en [KillerCoda - Docker Compose](https://killercoda.com/playgrounds/scenario/docker-compose)

**Crear un archivo `docker-compose.yml` con el siguiente contenido:**
```css
├── app
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yml
└── Dockerfile
```

**Dockerfile**
```Dockerfile
FROM python:3.10

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**requirements.txt**
```txt
fastapi
uvicorn[standard]
asyncpg
sqlalchemy
```

**main.py**
```python
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡FastAPI funcionando con Docker Compose!"}
```

**Crear un archivo `docker-compose.yml` con el siguiente contenido:**
```yaml
version: "3.8"

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: test_db
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  postgres-data:
```

**Levantar los servicios:**
```sh
docker-compose up -d
```

**Verificar que los contenedores están en ejecución:**
```sh
docker-compose ps
```

**Detener los servicios:**
```sh
docker-compose down
```

### **Lab 2: Volúmenes persistentes y conexión real a PostgreSQL**

**Objetivo:** Asegurar que PostgreSQL almacene los datos de forma persistente y que FastAPI pueda conectarse realmente a la base de datos.

**Extensión de main.py para conectar a PostgreSQL:**
```python
from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE_URL = "postgresql+psycopg2://postgres:admin@db:5432/test_db"
engine = create_engine(DATABASE_URL)

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"db_status": result.scalar()}

```

**Modificar `docker-compose.yml` para agregar volúmenes:**
```yaml
version: "3.8"

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: test_db
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  postgres-data:
```

**Ejecutar:**
```sh
docker-compose up -d
```

**Verificar que los datos persisten tras reiniciar el contenedor.**

### **Lab 3: Creación de una Red Personalizada**

**Objetivo:** Conectar servicios a través de una red Docker personalizada.

**Agregar una red personalizada a `docker-compose.yml`:**
```yaml
networks:
  red-app:
  
services:
  db:
    ...
    networks:
      - red-app

  backend:
    ...
    networks:
      - red-app

networks:
  red-app:
```

**Ejecutar:**
```sh
docker-compose up -d
```

**Comprobar que los servicios están en la misma red:**
```sh
docker network inspect mi-red
```

### **Lab 4: CRUD con FastAPI + SQLAlchemy conectado a SQL Server externo**

**Objetivo:** Veamos algo mas menos real.

**Estructura del proyecto:**
```css
.
├── app
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── crud.py
├── .env
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

```

**.env:**
```txt
DB_HOST=mi-sqlserver-host
DB_PORT=1433
DB_NAME=mi_basedatos
DB_USER=usuario
DB_PASS=clave
```

**requirements.txt:**
```txt
fastapi
uvicorn[standard]
sqlalchemy
pymssql
```

**models.py:**
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)
```

**database.py:**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Reemplaza los datos con los de tu instancia SQL Server
DB_HOST = "sqlserver_host"
DB_PORT = "1433"
DB_NAME = "mi_basedatos"
DB_USER = "usuario"
DB_PASS = "clave"

DATABASE_URL = f"mssql+pymssql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
```

**main.py:**
```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, init_db
from app import crud

app = FastAPI()

# Inicializa la base de datos al arrancar
@app.on_event("startup")
def startup():
    init_db()

# Dependencia de sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clientes")
def crear(nombre: str, email: str, db: Session = Depends(get_db)):
    return crud.crear_cliente(db, nombre, email)

@app.get("/clientes")
def listar(db: Session = Depends(get_db)):
    return crud.obtener_clientes(db)
```

**Dockerfile:**
```Dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

**docker-compose.yml:**
```yaml
version: "3.8"

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Para ejecutar
Asegúrate de que el SQL Server externo esté accesible desde tu máquina.

Modifica database.py con los datos reales.

Ejecuta:

1. sh
2. Copiar
3. Editar
```sh
docker-compose up --build
```
Accede a la API en Swagger: http://localhost:8000/docs

**Confirmar que el backend se vuelve a conectar automáticamente.**

### **Extra: Depuración de Servicios con Logs**

**Objetivo:** Explorar logs de un servicio en ejecución.

**Ver los logs del backend:**
```sh
docker-compose logs -f backend
```

**Detener y reiniciar el servicio de la base de datos:**
```sh
docker-compose restart db
```

**Confirmar que el backend se vuelve a conectar automáticamente.**

---

## 🔹 3. Cierre y Tareas

### **Resumen de la clase:**
* ✔ Uso de Docker Compose para definir aplicaciones multi-contenedor.
* ✔ Manejo de volúmenes persistentes en bases de datos.
* ✔ Configuración de redes personalizadas para comunicación entre servicios.
* ✔ Uso de `docker-compose logs` y `depends_on` para depuración y orden de inicio.

### **Tareas para la próxima clase:**
- **Crear un `docker-compose.yml` para una aplicación Flask + Redis**
  - Usar una imagen de Python (`python:3.9`).
  - Instalar dependencias (`pip install flask redis`).
  - Conectar el backend con Redis en una red personalizada.
- **Explorar el uso de `healthcheck` en Docker Compose**
  - Investigar cómo `healthcheck` ayuda a verificar si un servicio está activo.
  - Probar agregar un `healthcheck` a PostgreSQL para asegurarse de que esté listo antes de iniciar el backend.

🎯 **Resultado Esperado:**
* ✔ Gestionar aplicaciones multi-contenedor con Docker Compose.
* ✔ Aplicar volúmenes persistentes y redes personalizadas.
* ✔ Usar logs para depurar servicios en tiempo real.
* ✔ Ejecutar aplicaciones con múltiples servicios de manera ordenada y eficiente.