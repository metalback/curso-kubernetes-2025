1. Crear los Pods:
```sh
kubectl run backend --image=nginx --labels="app=backend" --expose --port=80
kubectl run frontend --image=busybox --labels="app=frontend" -it --restart=Never -- sh
```
2. Probar conectividad desde frontend a backend:
```sh
wget -qO- backend
```