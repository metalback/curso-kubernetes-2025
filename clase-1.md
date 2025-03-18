# Comandos Básicos de Docker

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