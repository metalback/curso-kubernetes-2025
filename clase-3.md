# 📚 Clase 3: Desarrollo Local con Docker y Debugging

## 🔹 Estructura de la Clase

### 🔸 1. Teoría

#### ✅ 1.1 ¿Por qué usar Docker para Desarrollo Local?

**Concepto Clave:**
El desarrollo con Docker permite replicar entornos de producción sin afectar la máquina local.

**Problemas comunes sin Docker:**
- "Funciona en mi máquina pero no en la tuya."
- Diferencias en dependencias entre equipos.
- Configuración manual de bases de datos y servidores.

**Ventajas de usar Docker en desarrollo:**
✔ Evita instalaciones manuales, ya que todo está en contenedores.
✔ Permite hot-reloading para cambios en tiempo real.
✔ Usa volúmenes para persistir datos entre sesiones.

#### ✅ 1.2 Uso de Volúmenes para Desarrollo en Vivo

**Concepto Clave:**
Los volúmenes permiten compartir archivos entre el contenedor y el sistema local.

**Ejemplo sin volúmenes (no refleja cambios en vivo)**
```sh
docker run -d -p 3000:3000 mi-app
```

**Ejemplo con volúmenes (hot-reloading habilitado)**
```sh
docker run -d -p 3000:3000 -v $(pwd):/app mi-app
```

✔**Ventaja:**Cualquier cambio en el código local se refleja en el contenedor sin reiniciarlo.

**Definiendo volúmenes en `docker-compose.yml`**
```yaml
services:
  app:
    image: node:18
    working_dir: /app
    volumes:
      - .:/app
    command: ["npm", "run", "dev"]
```

#### ✅ 1.3 Debugging y Troubleshooting en Docker

**Concepto Clave:**
Los errores en contenedores deben resolverse sin acceso a un "escritorio gráfico", usando logs y comandos en la terminal.

**Comandos útiles para debugging:**

✔ Ver logs en vivo de un contenedor:
```sh
docker logs -f <nombre_contenedor>
```

✔ Acceder a un contenedor en ejecución:
```sh
docker exec -it <nombre_contenedor> bash
```

✔ Inspeccionar detalles de un contenedor:
```sh
docker inspect <nombre_contenedor>
```

✔ Ver procesos dentro de un contenedor:
```sh
docker top <nombre_contenedor>
```

**Ejemplo de un error común:**

❌**Error:**"El contenedor se detiene inesperadamente."

✔**Diagnóstico:**
```sh
docker ps -a    # Ver si el contenedor está detenido
docker logs <nombre_contenedor>  # Ver mensajes de error
docker inspect <nombre_contenedor> | grep "OOM"  # Revisar si se quedó sin memoria
```

✔**Solución:**Ajustar `memory_limit` o revisar el código de la app.

---

## 🔹 2. Práctica en KillerCoda

###**Lab 1: Desarrollo con Hot-Reloading

**Objetivo:**Configurar un entorno de desarrollo donde los cambios en el código se reflejen sin reiniciar el contenedor.

**Abrir el entorno en KillerCoda - Docker Debugging**
[https://killercoda.com/playgrounds/scenario/docker-debugging](https://killercoda.com/playgrounds/scenario/docker-debugging)

**Estructura del proyecto:**
```javascript
Lab 1/
│
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

```

**Crear `app/main.py`:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola FastAPI en Docker con live reload!"}
```

**requirements.txt:**
```sh
fastapi
uvicorn[standard]
```

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY ./app ./app

# Comando por defecto (puede ser sobrescrito por docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

**docker-compose.yml:**
```sh
version: "3.8"

services:
  web:
    build: .
    volumes:
      - ./app:/app/app
    ports:
      - "8000:8000"
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Ejecutar el entorno:**
```sh
docker-compose up --build
```

Modificar `main.py` y ver cambios en vivo sin reiniciar el contenedor.

---

###**Lab 2: Debugging de Contenedores

**Objetivo:**Usar comandos de depuración para inspeccionar y solucionar errores en contenedores.

**Estructura del proyecto:**
```javascript
Lab 2/
│
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── docker-compose.yml
```

**Crear `app/main.py`:**
```python
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
```

**requirements.txt:**
```sh
fastapi
uvicorn[standard]
```

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY ./app ./app

# Comando por defecto (puede ser sobrescrito por docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

**.dockerignore:**
```sh
__pycache__/
*.pyc
*.pyo
*.pyd
.env
```

**docker-compose.yml:**
```yaml
version: "3.9"

services:
  debug-app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./app:/app/app
    environment:
      DEBUG_MODE: "true"
```

**Ejecutar el entorno:**
```sh
docker-compose up --build
```

Modificar `main.py` y ver cambios en vivo sin reiniciar el contenedor.



**Levantar una aplicación fallida:**
```sh
docker run -d --name mi-app node:18 node server.js
```

**Ver logs del contenedor:**
```sh
docker logs -f mi-app
```

**Acceder a la terminal del contenedor:**
```sh
docker exec -it mi-app bash
```

**Inspeccionar procesos en ejecución:**
```sh
docker top mi-app
```

**Verificar variables de entorno:**
```sh
docker inspect mi-app | grep "Env"
```

---

###**Lab 3: Análisis de Problemas con Redes de Docker

**Objetivo:**Diagnosticar problemas de conexión entre servicios en una red Docker.

**Nueva estructura del proyecto**
```css
docker-network-debug/
│
├── service_a/
│   └── main.py
├── service_b/
│   └── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── docker-compose.yml
└── .env
```

**Agrega una base de datos PostgreSQL**
```yaml
version: "3.9"

services:
  service_a:
    build:
      context: ./service_a
      dockerfile: ../Dockerfile
    ports:
      - "8000:8000"
    environment:
      SERVICE_B_HOST: service_b
      SERVICE_B_PORT: 8001
      POSTGRES_HOST: db
      POSTGRES_PORT: 5432
      POSTGRES_DB: appdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    depends_on:
      - service_b
      - db
    networks:
      - app_net

  service_b:
    build:
      context: ./service_b
      dockerfile: ../Dockerfile
    ports:
      - "8001:8001"
    networks:
      - app_net

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - app_net

volumes:
  pgdata:

networks:
  app_net:
    driver: bridge
```

**Variables `.env` (opcional)**
```yaml
Puedes mover las credenciales a .env y usar env_file: .env.
```

**`service_a/main.py` con conexión PostgreSQL**
```python
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
```

**Verifica conexión a PostgreSQL**
```sh
curl http://localhost:8000/check-db
```

**Desde dentro del contenedor A:**
```bash
docker exec -it <service_a_id> /bin/sh

# Verifica red
ping db
nslookup db

# Prueba conexión PostgreSQL
apk add postgresql-client
psql -h db -U user -d appdb
```


**Crear `docker-compose.yml` con una base de datos PostgreSQL y una aplicación Node.js:**
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
    image: node:18
    networks:
      - mi-red
    depends_on:
      - db
    command: ["node", "-e", "console.log('Intentando conectar a la BD...')"]
 
networks:
  mi-red:
```

**Ejecutar:**
```sh
docker-compose up -d
```

**Verificar que los servicios están conectados:**
```sh
docker network inspect mi-red
```

**Diagnosticar problemas de conexión con `ping`:**
```sh
docker exec -it <id_app> ping db
```

**Solucionar agregando `healthcheck` a la BD:**
```yaml
healthcheck:
  test: ["CMD", "pg_isready", "-U", "postgres"]
  interval: 10s
  retries: 5
```

---

## 🔹 3. Cierre y Tareas

### **Resumen de la clase:**
✔ Uso de volúmenes para compartir archivos entre el contenedor y el sistema local.
✔ Aplicación de hot-reloading en entornos de desarrollo.
✔ Depuración de contenedores con `docker logs`, `docker exec` y `docker inspect`.
✔ Diagnóstico de problemas en redes de Docker.

### **Tareas para la próxima clase:**
- Crear un `docker-compose.yml` con MySQL y una aplicación Python.
- Explorar `healthcheck` en Docker Compose.

🎯**Resultado Esperado:**

* ✔ Uso eficiente de volúmenes en entornos de desarrollo.
* ✔ Depuración efectiva de contenedores.
* ✔ Diagnóstico y solución de problemas de red en Docker.
* ✔ Aplicación de buenas prácticas en Docker para desarrollo local.
