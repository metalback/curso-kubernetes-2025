# 📚 Clase 1: Introducción a Docker y Contenedores

## 🔹 Estructura de la Clase

### 🔸 1. Teoría

#### ✅ 1.1 Introducción a Docker y Contenedores
**Concepto Clave:** Docker permite empaquetar aplicaciones y sus dependencias en contenedores portables y ligeros.

**Problema que resuelve Docker:**
- "Funciona en mi máquina, pero no en la tuya."
- Inconsistencias entre entornos de desarrollo, prueba y producción.
- Instalaciones pesadas con múltiples dependencias.

**¿Qué es un contenedor?**
- Es una unidad de software empaquetada con código y dependencias.
- Se ejecuta de forma aislada del sistema operativo anfitrión.
- Se puede desplegar en cualquier lugar sin cambios (local, servidores, nube).

**Comparación rápida: Contenedores vs Máquinas Virtuales (VMs)**
| Característica | Contenedores | Máquinas Virtuales |
|--------------|-------------|-----------------|
| Tiempo de inicio | Segundos | Minutos |
| Tamaño | Megabytes | Gigabytes |
| Uso del sistema | Comparte kernel | Requiere un SO completo |
| Portabilidad | Alta | Media |

#### ✅ 1.2 Componentes de Docker

**Docker Engine:**
- Se compone del Daemon (gestiona contenedores) y la CLI (herramienta de línea de comandos).
- Se ejecuta en segundo plano en Linux/macOS/Windows.

**Docker CLI:**
- Herramienta para interactuar con contenedores (`docker run`, `docker ps`, etc.).

**Docker Hub:**
- Registro público donde se almacenan imágenes listas para usar.
- Ejemplo: `docker pull nginx` obtiene la imagen de Nginx desde Docker Hub.

**Imagen vs Contenedor:**
- **Imagen:** Plantilla inmutable con el código de la aplicación.
- **Contenedor:** Instancia en ejecución de una imagen.

Ejemplo:
- Una imagen de Node.js es como un archivo `.iso` de Ubuntu.
- Un contenedor basado en esa imagen es como un sistema Ubuntu en ejecución.

#### ✅ 1.3 Comandos básicos de Docker

**Gestión de Contenedores:**
```sh
docker run nginx          # Ejecutar un contenedor con la imagen de Nginx
docker ps                 # Ver contenedores en ejecución
docker stop <ID/NOMBRE>   # Detener un contenedor
docker rm <ID/NOMBRE>     # Eliminar un contenedor
```

**Gestión de Imágenes:**
```sh
docker images             # Ver imágenes locales
docker pull redis         # Descargar una imagen de Redis
docker rmi <IMAGEN>       # Eliminar una imagen
```

**Ejecución Interactiva:**
```sh
docker run -it ubuntu bash   # Acceder a un contenedor de Ubuntu en modo interactivo
```

## 🔹 2. Práctica en KillerCoda

### 🛠️ Lab 1: Primer Contenedor con Docker
**Objetivo:** Ejecutar un contenedor simple y verificar su estado.

**Ejecutar un contenedor de Nginx:**
```sh
docker run -d --name mi-nginx -p 8080:80 nginx
```

**Verificar su estado:**
```sh
docker ps
```

**Acceder desde un navegador:**
```
http://localhost:8080
```

**Detener y eliminar el contenedor:**
```sh
docker stop mi-nginx
docker rm mi-nginx
```

### 🛠️ Lab 2: Explorando Contenedores en Ejecución
**Objetivo:** Ejecutar un contenedor interactivo y entender su aislamiento.

**Iniciar un contenedor de Ubuntu en modo interactivo:**
```sh
docker run -it ubuntu bash
```

**Probar comandos dentro del contenedor:**
```sh
ls /
echo "Hola desde un contenedor" > /home/mensaje.txt
cat /home/mensaje.txt
exit
```

**Inspeccionar el contenedor después de salir:**
```sh
docker ps -a
```

### 🛠️ Lab 3: Descargando y Gestionando Imágenes
**Objetivo:** Manejar imágenes de Docker en el sistema.

**Listar imágenes locales:**
```sh
docker images
```

**Descargar manualmente una imagen de Redis:**
```sh
docker pull redis
```

**Inspeccionar la información de la imagen:**
```sh
docker inspect redis
```

### 🛠️ Lab 4: Creando y Ejecutando Contenedores en Segundo Plano
**Objetivo:** Ejecutar servicios en segundo plano.

**Ejecutar un contenedor de PostgreSQL:**
```sh
docker run -d --name mi-postgres -e POSTGRES_PASSWORD=admin -p 5432:5432 postgres
```

**Verificar su ejecución:**
```sh
docker ps
```

**Detener y eliminar el contenedor:**
```sh
docker stop mi-postgres
docker rm mi-postgres
```

## 🔹 3. Cierre y Tareas

### 📌 Resumen de la clase:
- Diferencias entre contenedores y máquinas virtuales.
- Uso de Docker CLI para ejecutar y administrar contenedores.
- Descarga y gestión de imágenes desde Docker Hub.
- Ejecución de contenedores en modo interactivo y en segundo plano.

### 📌 Tareas para la próxima clase:

1. **Ejecutar un contenedor con MySQL**
   - Descargar la imagen de MySQL (`docker pull mysql`).
   - Ejecutar un contenedor en modo interactivo con `-e MYSQL_ROOT_PASSWORD=admin`.
   - Verificar que el contenedor está corriendo (`docker ps`).
   - Detener y eliminar el contenedor.

2. **Explorar imágenes en Docker Hub**
   - Buscar imágenes de lenguajes de programación (ejemplo: `python`, `node`).
   - Descargar una imagen y ejecutar un contenedor en modo interactivo.
   - Probar ejecutar un simple script de Python dentro del contenedor.

🎯 **Resultado Esperado:**
- Los participantes entienden qué es Docker y para qué se usa.
- Ejecutan y gestionan contenedores básicos con Docker.
- Descargan y exploran imágenes de Docker Hub.
- Manejan comandos básicos de inspección y eliminación de contenedores.


# Extensión: Comandos Básicos de Docker

## 📌 1. Gestión de Imágenes

### Descargar una imagen
```sh
docker pull nombre_imagen
```
Ejemplo:
```sh
docker pull nginx
```

### Listar imágenes descargadas
```sh
docker images
docker image ls
```

### Eliminar una imagen
```sh
docker rmi nombre_imagen
```
Ejemplo:
```sh
docker rmi nginx
```

## 🚀 2. Gestión de Contenedores

### Crear y ejecutar un contenedor
```sh
docker run nombre_imagen
```
Ejemplo:
```sh
docker run nginx
```

### Ejecutar un contenedor en segundo plano (-d)
```sh
docker run -d nombre_imagen
```
Ejemplo:
```sh
docker run -d nginx
```

### Asignar un nombre a un contenedor
```sh
docker run --name mi_contenedor nombre_imagen
```
Ejemplo:
```sh
docker run --name servidor_web nginx
```

### Ejecutar un contenedor con un puerto mapeado
```sh
docker run -p puerto_host:puerto_contenedor nombre_imagen
```
Ejemplo:
```sh
docker run -p 8080:80 nginx
```

### Listar contenedores en ejecución
```sh
docker ps
```

### Listar todos los contenedores (incluyendo detenidos)
```sh
docker ps -a
```

### Detener un contenedor
```sh
docker stop id_contenedor
```
Ejemplo:
```sh
docker stop 123abc
```

### Iniciar un contenedor detenido
```sh
docker start id_contenedor
```

### Eliminar un contenedor
```sh
docker rm id_contenedor
```

## 🏗️ 3. Gestión de Volúmenes

### Crear un volumen
```sh
docker volume create nombre_volumen
```

### Listar volúmenes
```sh
docker volume ls
```

### Eliminar un volumen
```sh
docker volume rm nombre_volumen
```

### Usar un volumen en un contenedor
```sh
docker run -v nombre_volumen:/ruta/en/contenedor nombre_imagen
```
Ejemplo:
```sh
docker run -v mi_datos:/app/datos nginx
```

## 🔧 4. Variables de Entorno

### Pasar variables de entorno al contenedor
```sh
docker run -e NOMBRE=valor nombre_imagen
```
Ejemplo:
```sh
docker run -e MYSQL_ROOT_PASSWORD=secreto mysql
```

### Usar un archivo `.env`
```sh
docker run --env-file .env nombre_imagen
```

## 🏗️ 5. Gestión de Redes

### Listar redes
```sh
docker network ls
```

### Crear una red personalizada
```sh
docker network create mi_red
```

### Conectar un contenedor a una red
```sh
docker network connect mi_red id_contenedor
```

### Desconectar un contenedor de una red
```sh
docker network disconnect mi_red id_contenedor
```

## 🛠️ 6. Inspección y Logs

### Ver logs de un contenedor
```sh
docker logs id_contenedor
```

### Ver detalles de un contenedor
```sh
docker inspect id_contenedor
```

### Ver detalles de una imagen
```sh
docker inspect nombre_imagen
```

## 🔄 7. Ejecutar Comandos en un Contenedor

### Acceder a un contenedor en ejecución
```sh
docker exec -it id_contenedor bash
```
Ejemplo:
```sh
docker exec -it servidor_web bash
```

### Ejecutar un comando dentro de un contenedor
```sh
docker exec id_contenedor comando
```
Ejemplo:
```sh
docker exec servidor_web ls -la
```

## 🗑️ 8. Limpieza de Docker

### Eliminar contenedores detenidos
```sh
docker container prune
```

### Eliminar imágenes sin usar
```sh
docker image prune
```

### Eliminar todos los volúmenes sin usar
```sh
docker volume prune
```

### Eliminar todo lo que no esté en uso
```sh
docker system prune -a
```