# 📚 Clase 5: Arquitectura y Componentes de Kubernetes

## 🔹 Estructura de la Clase

### 🔸 1. Teoría

#### ✅ 1.1 Introducción a Kubernetes

**Concepto Clave:**
Kubernetes es una plataforma de orquestación de contenedores que automatiza la implementación, escalado y operación de aplicaciones.

**¿Por qué usar Kubernetes?**
- ✔ Automatiza la administración de contenedores.
- ✔ Escala aplicaciones de forma eficiente.
- ✔ Facilita la gestión del ciclo de vida de los contenedores.
- ✔ Proporciona alta disponibilidad y recuperación automática.

**Componentes Principales:**
- ✔ **Clúster**: Grupo de máquinas donde se ejecutan las aplicaciones.
- ✔ **Nodo**: Máquina dentro del clúster (puede ser física o virtual).
- ✔ **Pod**: La unidad más pequeña en Kubernetes, contiene uno o más contenedores.
- ✔ **Service**: Permite que los Pods se comuniquen entre sí o con el exterior.
- ✔ **Deployment**: Administra la actualización y replicación de Pods.

#### ✅ 1.2 Arquitectura de Kubernetes

**Concepto Clave:**
Kubernetes sigue un modelo **Master-Worker**, donde el **Control Plane** gestiona los nodos de trabajo.

**Control Plane (Nodo Maestro):**
- ✔ **API Server**: Punto central de comunicación con Kubernetes.
- ✔ **Scheduler**: Asigna Pods a los nodos disponibles.
- ✔ **Controller Manager**: Gestiona la creación y eliminación de objetos.
- ✔ **etcd**: Base de datos distribuida que almacena el estado del clúster.

**Nodos de Trabajo (Workers):**
- ✔ **Kubelet**: Agente que corre en cada nodo, reportando su estado.
- ✔ **Kube Proxy**: Maneja la comunicación de red entre los Pods y los Servicios.
- ✔ **Container Runtime**: Ejecuta los contenedores (Docker, containerd).

#### ✅ 1.3 Primeros Pasos con kubectl

**Concepto Clave:**
`kubectl` es la CLI principal para interactuar con Kubernetes.

**Comandos básicos:**
```sh
kubectl cluster-info  # Ver información del clúster
kubectl get nodes  # Ver nodos disponibles
kubectl get pods  # Ver pods en ejecución
kubectl get deployments  # Ver despliegues activos
kubectl get services  # Ver servicios expuestos
kubectl describe pod <nombre>  # Inspeccionar un pod
kubectl delete pod <nombre>  # Eliminar un pod
```

#### ✅ 1.4 Introducción a los Manifiestos YAML en Kubernetes

**Concepto Clave:**
Los **manifiestos YAML** en Kubernetes permiten definir recursos de manera declarativa.

**¿Por qué usar YAML en lugar de `kubectl run`?**
- ✔ Permiten versionar y reutilizar configuraciones.
- ✔ Son más portables y fáciles de administrar.
- ✔ Permiten definir múltiples recursos en un solo archivo.

**Ejemplo de un Manifiesto YAML para un Pod:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mi-pod
  labels:
    app: mi-aplicacion
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
```

**Ejemplo de un Manifiesto YAML para un Deployment:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mi-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: mi-app
  template:
    metadata:
      labels:
        app: mi-app
    spec:
      containers:
        - name: mi-container
          image: nginx
          ports:
            - containerPort: 80
```
✔ **Es una mejor práctica usar Deployments en lugar de Pods individuales.**

---

## 🔹 2. Práctica en KillerCoda

### **Lab 1: Exploración del Clúster Kubernetes**

**Objetivo:** Identificar los componentes clave de Kubernetes.

Abrir el entorno en [KillerCoda - Kubernetes Basics](https://killercoda.com/playgrounds/scenario/kubernetes-basics)

```sh
kubectl cluster-info  # Ver información del clúster
kubectl get nodes  # Ver nodos disponibles
kubectl describe node <nombre-nodo>  # Inspeccionar un nodo
```

### **Lab 2: Creación y Gestión de Pods**

**Objetivo:** Ejecutar y administrar un Pod en Kubernetes.

```sh
kubectl run mi-pod --image=nginx --restart=Never  # Crear un Pod
kubectl get pods  # Ver estado del Pod
kubectl describe pod mi-pod  # Obtener detalles del Pod
kubectl exec -it mi-pod -- /bin/sh  # Acceder al contenedor en el Pod
kubectl delete pod mi-pod  # Eliminar el Pod
```

### **Lab 3: Creación de un Pod con un Archivo YAML**

**Objetivo:** Crear un Pod de manera declarativa con un archivo YAML.

**Archivo `mi-pod.yaml`**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mi-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
```

```sh
kubectl apply -f mi-pod.yaml  # Aplicar el archivo YAML
kubectl get pods  # Verificar la creación del Pod
kubectl delete -f mi-pod.yaml  # Eliminar el Pod
```

### **Lab 4: Exploración de Logs y Debugging**

**Objetivo:** Usar logs y comandos de depuración en Kubernetes.

**Crear un Pod con una imagen incorrecta para generar un error:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mi-pod-error
spec:
  containers:
    - name: error-container
      image: imagen-inexistente
```

```sh
kubectl apply -f mi-pod-error.yaml  # Aplicar el archivo
kubectl get pods  # Ver estado del Pod
kubectl logs mi-pod-error  # Obtener logs del Pod
kubectl describe pod mi-pod-error  # Inspeccionar detalles del error
kubectl delete pod mi-pod-error  # Eliminar el Pod
```

---

## 🔹 3. Cierre y Tareas

### **Resumen de la clase:**
- ✔ Arquitectura de Kubernetes y sus componentes clave.
- ✔ Uso de `kubectl` para interactuar con el clúster.
- ✔ Creación y eliminación de Pods en Kubernetes.
- ✔ Depuración básica de errores en Pods.

### **Tareas para la próxima clase:**
- **Crear un Pod que ejecute un contenedor de Python**
  - Usar la imagen `python:3.9-slim`.
  - Especificar el comando `python -m http.server 8000`.
  - Exponer el puerto `8000` en el Pod.
- **Investigar cómo listar y filtrar Pods en Kubernetes**
  - ¿Cómo listar solo los Pods en estado `Running`?
  - ¿Cómo filtrar Pods por etiquetas (`labels`)?

🎯 **Resultado Esperado:**
- ✔ Entender la arquitectura de Kubernetes.
- ✔ Interactuar con el clúster usando `kubectl`.
- ✔ Crear, administrar y eliminar Pods.
- ✔ Usar logs y comandos de depuración para solucionar errores en Pods.