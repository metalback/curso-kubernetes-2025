# 📚 Clase 10: Optimización y Buenas Prácticas en Kubernetes
 
**Objetivo:** Aprender a optimizar el uso de recursos en Kubernetes mediante **Resource Requests & Limits**, mejorar la eficiencia con **Liveness y Readiness Probes**, y aplicar **buenas prácticas** para entornos productivos.

---

## 🔹 1. Teoría

> 🚀 Meta: Explicar cómo Kubernetes gestiona los recursos y cómo optimizar la ejecución de contenedores.

### ✅ 1.1 Administración de Recursos

**Concepto clave:**
Los **requests** y **limits** permiten controlar el uso de CPU y memoria.

```yaml
resources:
  requests:
    memory: "128Mi"
    cpu: "250m"
  limits:
    memory: "256Mi"
    cpu: "500m"
```

- **Requests:** mínimo garantizado.
- **Limits:** máximo permitido.

---

### ✅ 1.2 Liveness y Readiness Probes

**Probes:** Monitorean la salud de las aplicaciones.

```yaml
livenessProbe:
  httpGet:
    path: /
    port: 80
  initialDelaySeconds: 5
  periodSeconds: 10
readinessProbe:
  httpGet:
    path: /
    port: 80
  initialDelaySeconds: 3
  periodSeconds: 5
```

- **Liveness:** reinicia si falla.
- **Readiness:** quita del balanceo si no está listo.

---

### ✅ 1.3 Buenas Prácticas

- Usar ConfigMaps y Secrets.
- Definir Requests & Limits.
- Implementar Probes.
- Evitar ejecutar como root:
```yaml
securityContext:
  runAsNonRoot: true
```
- Organizar con Namespaces.
- Usar Autoscaling.

---

## 🔹 2. Práctica en KillerCoda

### ✅ Lab 1: Resource Requests & Limits

1. Crear Pod con recursos definidos.
2. Aplicar y verificar:
```sh
kubectl get pod mi-pod -o yaml | grep -A5 resources
```

---

### ✅ Lab 2: Probes

1. Crear Pod con `livenessProbe` y `readinessProbe`.
2. Simular error para probar reinicio:
```sh
kubectl exec -it mi-pod -- rm -rf /usr/share/nginx/html
```

---

### ✅ Lab 3: Uso de Namespaces

1. Crear Namespace:
```sh
kubectl create namespace desarrollo
```
2. Desplegar un Deployment dentro del namespace.

---

### ✅ Lab 4: Autoscaling con HPA

1. Habilitar `metrics-server` (Minikube):
```sh
minikube addons enable metrics-server
```
2. Crear Deployment escalable.
3. Aplicar HPA:
```sh
kubectl autoscale deployment mi-app --cpu-percent=50 --min=1 --max=5
```

---

## 🔹 3. Cierre y Tareas

### ✉ Resumen:

- Optimización con Requests & Limits.
- Monitorización con Probes.
- Organización con Namespaces.
- Escalado automático con HPA.

### 📅 Tareas:

1. Crear una Readiness Probe que espere 10 segundos.
2. Investigar cómo limitar acceso a un Namespace con RBAC.

---

**📌 Resultado esperado:** Participantes capaces de optimizar, monitorear y escalar aplicaciones en Kubernetes aplicando buenas prácticas.

