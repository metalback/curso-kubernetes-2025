# 📚 Clase 8: Networking y Exposición de Servicios en Kubernetes
  
**Objetivo:** Aprender a exponer aplicaciones en Kubernetes mediante **Services** e **Ingress Controllers**, permitiendo la comunicación entre Pods y con el mundo exterior.

---

## 🔹 1. Teoría

> 🚀 Meta: Entender el modelo de red de Kubernetes y aprender a exponer aplicaciones con diferentes tipos de servicios.

### ✅ 1.1 Tipos de Networking en Kubernetes

**Concepto Clave:** Kubernetes crea una red plana donde todos los Pods pueden comunicarse entre sí, pero necesitamos mecanismos para exponer servicios de forma controlada.

**Tipos de comunicación:**
- **Pod-to-Pod**: interna, sin restricciones.
- **Pod-to-Service**: acceso a través de un nombre DNS estable.
- **Ingress**: punto de entrada HTTP/HTTPS para el mundo exterior.

---

### ✅ 1.2 Tipos de Services

| Tipo | Descripción |
|------|-------------|
| `ClusterIP` | Por defecto. Accesible solo dentro del clúster. |
| `NodePort` | Expuesto fuera del clúster en un puerto del nodo. |
| `LoadBalancer` | Usa un balanceador de carga externo (cloud). |
| `ExternalName` | Redirige a un nombre DNS externo. |

**Ejemplo de Service ClusterIP:**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mi-servicio
spec:
  selector:
    app: mi-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP
```

---

### ✅ 1.3 Introducción a Ingress Controllers

**Concepto Clave:** Un **Ingress** permite exponer uno o varios servicios HTTP bajo un mismo punto de entrada, usando reglas de enrutamiento.

**Ejemplo de recurso Ingress:**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mi-ingress
spec:
  rules:
    - host: mi-app.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: mi-servicio
                port:
                  number: 80
```

---

## 🔹 2. Práctica en KillerCoda

### ✅ Lab 1: Servicio ClusterIP

1. Crear Deployment de nginx con etiqueta `app: mi-app`.
2. Crear Service tipo ClusterIP apuntando al Deployment.
3. Ejecutar:
```sh
kubectl exec -it <otro-pod> -- curl mi-servicio
```

---

### ✅ Lab 2: Servicio NodePort

1. Modificar el Service para exponer como NodePort:
```yaml
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
```
2. Acceder al servicio:
```sh
curl http://<NODE-IP>:30080
```

---

### ✅ Lab 3: Configurar Ingress Controller

1. Habilitar Ingress Controller (en minikube o entorno compatible).
2. Crear Ingress con host `mi-app.local`.
3. Agregar a `/etc/hosts`:
```sh
echo "127.0.0.1 mi-app.local" | sudo tee -a /etc/hosts
```
4. Verificar acceso:
```sh
curl http://mi-app.local
```

---

### ✅ Lab 4: Diagnóstico de problemas de red

1. Revisar definición del Service e Ingress:
```sh
kubectl describe service mi-servicio
kubectl describe ingress mi-ingress
```
2. Consultar logs del controlador:
```sh
kubectl logs -n kube-system -l app.kubernetes.io/name=ingress-nginx
```

---

## 🔹 3. Cierre y Tareas

### ✉ Resumen:

- Servicios `ClusterIP`, `NodePort`, `LoadBalancer`.
- Uso de Ingress como puerta de entrada HTTP.
- Diagnóstico de problemas de red.

### 📅 Tareas:

1. Crear un Ingress para exponer dos servicios en rutas distintas (`/api`, `/web`).
2. Explorar cómo aplicar autenticación básica en Nginx Ingress con un Secret.

---

**🔜 Resultado esperado:** Participantes capaces de exponer aplicaciones Kubernetes usando distintos tipos de servicios y configurar reglas de entrada HTTP usando Ingress.

