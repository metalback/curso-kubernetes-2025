# 📚 Clase 6: Interacción con Kubernetes y Deployments
 
**Objetivo:** Aprender a administrar aplicaciones en Kubernetes utilizando **Deployments**, escalar Pods y gestionar el ciclo de vida de las aplicaciones con `kubectl`.

---

## 🔹 1. Teoría

> 🚀 Meta: Explicar cómo Kubernetes administra las aplicaciones a través de Deployments y cómo escalar servicios eficientemente.

### ✅ 1.1 ¿Qué es un Deployment?

**Concepto clave:** Un **Deployment** en Kubernetes se encarga de gestionar el ciclo de vida de los Pods, permitiendo escalabilidad, actualizaciones y rollbacks.

**Ventajas del Deployment sobre Pods individuales:**

- Permite **escalar** aplicaciones.
- Facilita **actualizaciones sin downtime**.
- Soporta **rollback** automático.
- Supervisa el estado de los Pods.

**Ejemplo básico de un Deployment:**

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
        - name: nginx-container
          image: nginx
          ports:
            - containerPort: 80
```

### ✅ 1.2 Creación y Gestión de Deployments

**Comandos esenciales con `kubectl`:**

```sh
kubectl apply -f deployment.yaml       # Crear Deployment
kubectl get deployments                 # Ver deployments
kubectl get pods -l app=mi-app         # Ver Pods del deployment
kubectl scale deployment mi-app --replicas=5  # Escalar
kubectl set image deployment/mi-app nginx=nginx:latest  # Actualizar imagen
kubectl delete deployment mi-app       # Eliminar
```

### ✅ 1.3 Rollbacks y Estrategias de Actualización

**Tipos de estrategia de despliegue:**

- **RollingUpdate** (por defecto): actualización gradual.
- **Recreate**: elimina todos los Pods antes de crear los nuevos.

**Comandos para rollback:**

```sh
kubectl rollout history deployment mi-app  # Ver historial
kubectl rollout undo deployment mi-app     # Hacer rollback
```

### ✅ 1.4 Escalado Automático con HPA (HorizontalPodAutoscaler)

**Concepto:** Kubernetes permite escalar de forma automática según el uso de CPU u otros métricos.

**Requisitos:** Tener el `metrics-server` instalado (por ejemplo, en Minikube se habilita con `minikube addons enable metrics-server`).

**Comando para crear un HPA:**
```sh
kubectl autoscale deployment mi-app --cpu-percent=50 --min=1 --max=5
```

**Ver estado del HPA:**
```sh
kubectl get hpa
```

---

## 🔹 2. Práctica en KillerCoda

### ✅ Lab 1: Creación de un Deployment

1. Crear archivo `deployment.yaml`.
2. Aplicar con `kubectl apply -f deployment.yaml`.
3. Verificar los Pods con `kubectl get pods`.
4. Eliminar con `kubectl delete deployment mi-app`.

### ✅ Lab 2: Escalado de un Deployment

1. Escalar a 5 réplicas:
```sh
kubectl scale deployment mi-app --replicas=5
```
2. Verificar:
```sh
kubectl get pods
```

### ✅ Lab 3: Actualización y Rollback

1. Actualizar imagen:
```sh
kubectl set image deployment/mi-app nginx=nginx:latest
```
2. Simular error:
```sh
kubectl set image deployment/mi-app nginx=imagen-inexistente
```
3. Ver error:
```sh
kubectl describe pod <nombre>
```
4. Hacer rollback:
```sh
kubectl rollout undo deployment mi-app
```

### ✅ Lab 4: Eliminación del Deployment

1. Verificar:
```sh
kubectl get deployments
```
2. Eliminar:
```sh
kubectl delete deployment mi-app
```

### ✅ Lab 5: Crear un HPA

1. Crear un Deployment con `resources.requests.cpu` definido:
```yaml
resources:
  requests:
    cpu: "100m"
```
2. Crear el autoscaler:
```sh
kubectl autoscale deployment mi-app --cpu-percent=50 --min=1 --max=5
```
3. Verificar:
```sh
kubectl get hpa
```

---

## 🔹 3. Cierre y Tareas

### ✉ Resumen:

- Uso de Deployments para gestionar el ciclo de vida de aplicaciones.
- Escalado, actualización y rollback con `kubectl`.
- Uso básico de HorizontalPodAutoscaler.

### 📅 Tareas:

1. Crear un Deployment para una app Flask en `python:3.9`.
2. Explorar el uso de `kubectl rollout pause` y `resume` para actualizaciones controladas.
3. Crear un HPA que escale una app de 1 a 3 Pods según CPU > 60%.

---

**🔜 Resultado esperado:** Participantes capaces de desplegar, escalar, actualizar y mantener aplicaciones usando Deployments de Kubernetes, incluyendo el escalado automático con HPA.

