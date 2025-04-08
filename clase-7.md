# 📚 Clase 7: Configuración de Aplicaciones y Persistencia en Kubernetes
 
**Objetivo:** Aprender a administrar configuraciones mediante **ConfigMaps y Secrets**, y gestionar almacenamiento persistente con **Persistent Volumes (PV)** y **Persistent Volume Claims (PVC)**.

---

## 🔹 1. Teoría

> 🚀 Meta: Explicar cómo Kubernetes gestiona la configuración y persistencia de datos de forma desacoplada de la aplicación.

### ✅ 1.1 Uso de ConfigMaps y Secrets

**ConfigMap:** Objeto que permite inyectar configuración no sensible (como variables de entorno o archivos).

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mi-configmap
data:
  APP_ENV: "produccion"
  LOG_LEVEL: "debug"
```

**Secret:** Similar al ConfigMap, pero para información sensible (como contraseñas o tokens), almacenada en Base64.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mi-secret
type: Opaque
data:
  PASSWORD: c2VjcmV0MTIz  # "secret123"
```

**Uso en Pods:**
```yaml
spec:
  containers:
    - name: mi-app
      image: nginx
      env:
        - name: APP_ENV
          valueFrom:
            configMapKeyRef:
              name: mi-configmap
              key: APP_ENV
        - name: PASSWORD
          valueFrom:
            secretKeyRef:
              name: mi-secret
              key: PASSWORD
```

---

### ✅ 1.2 Persistencia de Datos con PV y PVC

**PersistentVolume (PV):** Recurso del clúster que representa un volumen de almacenamiento.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mi-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
```

**PersistentVolumeClaim (PVC):** Solicitud de almacenamiento para un Pod.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mi-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

**Uso del PVC en un Pod:**
```yaml
spec:
  containers:
    - name: mi-app
      image: nginx
      volumeMounts:
        - mountPath: "/data"
          name: mi-volumen
  volumes:
    - name: mi-volumen
      persistentVolumeClaim:
        claimName: mi-pvc
```

---

### ✅ 1.3 Volúmenes efímeros (emptyDir)

**Uso típico:** Compartir datos entre contenedores en un mismo Pod.

```yaml
spec:
  containers:
    - name: mi-app
      image: nginx
      volumeMounts:
        - mountPath: "/tmp"
          name: temporal
  volumes:
    - name: temporal
      emptyDir: {}
```

---

## 🔹 2. Práctica en KillerCoda

### ✅ Lab 1: Crear y usar un ConfigMap

```sh
kubectl create configmap mi-configmap --from-literal=APP_ENV=produccion --from-literal=LOG_LEVEL=debug
```
Crear Pod con valores de entorno desde el ConfigMap y verificar:
```sh
kubectl exec -it mi-pod -- env | grep APP_ENV
```

---

### ✅ Lab 2: Crear y usar un Secret

```sh
echo -n "secret123" | base64
```
Crear `mi-secret.yaml` y aplicarlo:
```sh
kubectl apply -f mi-secret.yaml
```
Verificar con:
```sh
kubectl exec -it mi-pod -- env | grep PASSWORD
```

---

### ✅ Lab 3: Crear y montar un PV y PVC

Aplicar `pv.yaml` y `pvc.yaml`, luego montar en un Pod:
```sh
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
```
Verificar persistencia:
```sh
kubectl exec -it mi-pod -- touch /data/test.txt
kubectl delete pod mi-pod
kubectl apply -f mi-pod.yaml
kubectl exec -it mi-pod -- ls /data
```

---

### ✅ Lab 4: emptyDir entre contenedores

Crear un Pod con dos contenedores que compartan un emptyDir y pasen datos entre ellos.

---

## 🔹 3. Cierre y Tareas

### ✉ Resumen:

- Uso de ConfigMaps y Secrets.
- Montaje de volúmenes persistentes con PV y PVC.
- Compartición de datos con emptyDir.

### 📅 Tareas:

1. Crear un PVC y usarlo con una app Python que escriba logs en `/logs`.
2. Investigar diferencia entre `hostPath` y `emptyDir`.

---

**🔜 Resultado esperado:** Participantes capaces de gestionar configuraciones y persistencia de datos en Kubernetes usando las herramientas nativas del clúster.

