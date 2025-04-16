# 📚 Clase 9: Seguridad en Kubernetes
 
**Objetivo:** Aprender a aplicar seguridad en Kubernetes utilizando **RBAC**, **Service Accounts**, y **Network Policies** para controlar accesos, proteger credenciales y restringir comunicaciones dentro del clúster.

---

## 🔹 1. Teoría

> 🚀 Meta: Comprender los principales mecanismos de seguridad en Kubernetes para proteger recursos, comunicaciones y credenciales.

### ✅ 1.1 Fundamentos de Seguridad en Kubernetes

**Áreas clave:**
- **Autenticación y Autorización (RBAC)**
- **Control de acceso a redes (Network Policies)**
- **Protección de credenciales (Service Accounts y Secrets)**

---

### ✅ 1.2 RBAC: Control de Acceso Basado en Roles

**Componentes principales:**
- `Role`: permisos dentro de un namespace.
- `ClusterRole`: permisos a nivel de clúster.
- `RoleBinding`: asocia un usuario a un `Role`.
- `ClusterRoleBinding`: asocia un usuario a un `ClusterRole`.

**Ejemplo:**
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: lector-pods
  namespace: default
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list"]
```

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: lector-binding
  namespace: default
subjects:
  - kind: User
    name: juan
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: lector-pods
  apiGroup: rbac.authorization.k8s.io
```

---

### ✅ 1.3 Network Policies

**Concepto:** Permiten restringir el tráfico entre Pods.

**Ejemplo: solo permite ingreso a pods con label `app=backend` desde `app=frontend`:**
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: permitir-frontend
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
```

---

### ✅ 1.4 Service Accounts y Uso Seguro de Credenciales

**ServiceAccount:** Entidad que las aplicaciones usan para autenticarse en la API de Kubernetes.

**Ejemplo:**
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: mi-cuenta
```

**Asignación a un Pod:**
```yaml
spec:
  serviceAccountName: mi-cuenta
```

---

## 🔹 2. Práctica en KillerCoda

### ✅ Lab 1: RBAC con Role y RoleBinding

1. Crear Role y RoleBinding para listar Pods.
2. Verificar permisos con:
```sh
kubectl auth can-i list pods --as=juan
kubectl auth can-i delete pods --as=juan  # debería fallar
```

---

### ✅ Lab 2: Network Policies

1. Crear dos Pods `frontend` y `backend`.
2. Aplicar una NetworkPolicy que bloquee todo:
```yaml
policyTypes: ["Ingress"]
podSelector: {}
ingress: []
```
3. Probar comunicación entre Pods (debería fallar).
4. Crear excepciones para `frontend` usando labels.

---

### ✅ Lab 3: Uso de Service Accounts

1. Crear `mi-cuenta` como ServiceAccount.
2. Asignarla a un Pod.
3. Acceder al token montado en `/var/run/secrets/kubernetes.io/serviceaccount/token`.

---

### ✅ Lab 4: Diagnóstico de permisos y acceso

1. Revisar permisos de un usuario:
```sh
kubectl auth can-i get deployments --as=juan
```
2. Listar roles asociados:
```sh
kubectl get rolebindings --all-namespaces
```

---

## 🔹 3. Cierre y Tareas

### ✉ Resumen:

- Uso de RBAC para controlar accesos.
- Protección de tráfico con Network Policies.
- Seguridad de autenticación con Service Accounts.

### 📅 Tareas:

1. Crear un `ClusterRole` de solo lectura global.
2. Crear una `NetworkPolicy` que solo permita Egress a `8.8.8.8`.

---

**🔜 Resultado esperado:** Participantes capaces de aplicar controles de seguridad en Kubernetes con buenas prácticas de acceso, comunicación y autenticación.

