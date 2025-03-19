# 📚 Clase 2: Creación de Dockerfiles y Construcción de Imágenes

## 🔹 Estructura de la Clase
### 🔸 1. Teoría

#### ✅ 1.1 ¿Qué es un Dockerfile?
**Concepto Clave:**
Un Dockerfile es un archivo de texto que contiene instrucciones para crear una imagen de Docker de manera reproducible.

**¿Por qué usar un Dockerfile?**
- Evita instalar dependencias manualmente en cada contenedor.
- Permite compartir entornos de desarrollo estandarizados.
- Automatiza la creación de imágenes de manera eficiente.

**Ejemplo simple de un Dockerfile para Node.js:**
```dockerfile
# Imagen base de Node.js
FROM node:18

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de la aplicación
COPY . .

# Instalar dependencias
RUN npm install

# Exponer el puerto 3000
EXPOSE 3000

# Comando para ejecutar la app
CMD ["node", "app.js"]
```

**Explicación rápida:**
- `FROM` → Define la imagen base.
- `WORKDIR` → Establece el directorio de trabajo.
- `COPY` → Copia los archivos de la aplicación al contenedor.
- `RUN` → Ejecuta comandos en la construcción de la imagen.
- `EXPOSE` → Define un puerto para el contenedor.
- `CMD` → Especifica el comando a ejecutar cuando se inicie el contenedor.

#### ✅ 1.2 Construcción de Imágenes y Buenas Prácticas
**Comando para construir una imagen personalizada:**
```sh
docker build -t mi-aplicacion .
```

**Ejecutar un contenedor basado en la imagen creada:**
```sh
docker run -d -p 3000:3000 mi-aplicacion
```

**Buenas prácticas para optimizar imágenes:**
- Usar imágenes base ligeras (`node:alpine`, `python:slim`).
- Utilizar `.dockerignore` para excluir archivos innecesarios.
- Minimizar el uso de `RUN` en múltiples capas.
- Usar **Multi-Stage Builds** para reducir el tamaño de la imagen.

**Ejemplo de `.dockerignore` para Node.js:**
```
node_modules
npm-debug.log
.DS_Store
.env
```

#### ✅ 1.3 Multi-Stage Builds
**¿Qué es un Multi-Stage Build?**
Permite generar imágenes optimizadas al usar varias etapas en la construcción.

**Ejemplo para Node.js (reduciendo el tamaño de la imagen final):**
```dockerfile
# Etapa 1: Construcción
FROM node:18 AS build
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

# Etapa 2: Imagen final
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app/dist /app
RUN npm install --only=production
EXPOSE 3000
CMD ["node", "app.js"]
```

✔ **Ventaja:** Reduce el tamaño de la imagen final eliminando dependencias innecesarias.

## 🔹 2. Práctica en KillerCoda

### 🛠️ Lab 1: Creación de un Dockerfile desde Cero (15 min)
**Objetivo:** Construir y ejecutar una imagen personalizada de Node.js.

**Dockerfile:**
```dockerfile
FROM node:18
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["node", "app.js"]
```

**package.json:**
```json
{
  "name": "hello-world-node",
  "version": "1.0.0",
  "description": "Un servidor simple en Node.js con Docker",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {}
}
```

**app.js:**
```js
const http = require("http");
const server = http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Hello, World!\n");
});
server.listen(3000, () => {
    console.log("Server running at http://localhost:3000/");
});
```

**Construcción y ejecución:**
```sh
docker build -t mi-app .
docker run -d -p 3000:3000 mi-app
```

### 🛠️ Lab 2: Uso de `.dockerignore` para Optimizar la Imagen
**Objetivo:** Reducir el tamaño de la imagen final excluyendo archivos innecesarios.

**Crear un archivo `.dockerignore`:**
```sh
echo "node_modules" > .dockerignore
```

**Construcción de la imagen optimizada:**
```sh
docker build -t mi-app-optimizada .
```

### 🛠️ Lab 3: Implementando Multi-Stage Builds
**Objetivo:** Construir una imagen eficiente usando varias etapas.

**Dockerfile Multi-Stage:**
```dockerfile
# Etapa de construcción
# Etapa de construcción
FROM node:18 AS build
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build || echo "No build step"

# Etapa final (producción)
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app/package.json .
COPY --from=build /app/ .
RUN npm install --only=production
COPY --from=build /app /app
EXPOSE 3000
CMD ["node", "index.js"]
```

**Construcción y ejecución:**
```sh
docker build -t mi-app-multistage .
docker run -d -p 3000:3000 mi-app-multistage
```

### 🛠️ Lab 4: Exploración y Optimización de Imágenes
**Objetivo:** Analizar imágenes y verificar buenas prácticas.

**Ver información detallada de una imagen:**
```sh
docker inspect mi-app
```

**Identificar capas creadas en la imagen:**
```sh
docker history mi-app
```

## 🔹 3. Cierre y Tareas
### 📌 Resumen de la clase:
- Creación de Dockerfiles personalizados.
- Construcción de imágenes con `docker build`.
- Uso de `.dockerignore` para optimizar imágenes.
- Implementación de **Multi-Stage Builds** para reducir el tamaño de imágenes.

### 📌 Tareas para la próxima clase:
1. **Crear un Dockerfile para una aplicación en Python**
   - Usar `python:3.9-slim` como imagen base.
   - Copiar el código de la aplicación y ejecutar `pip install -r requirements.txt`.
   - Exponer el puerto adecuado y definir `CMD ["python", "app.py"]`.
   - Construir y ejecutar la imagen.

2. **Explorar la diferencia entre `RUN` y `CMD` en Dockerfile**
   - Investigar cómo afectan la construcción de la imagen.
   - Probar cambiando `CMD` por `ENTRYPOINT` y observar el comportamiento.

🎯 **Resultado Esperado:**
- Entender cómo construir imágenes personalizadas en Docker.
- Aplicar buenas prácticas en la creación de Dockerfiles.
- Optimizar imágenes con `.dockerignore` y Multi-Stage Builds.