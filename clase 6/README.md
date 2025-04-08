## Lab 1: Creación de un Deployment
kubectl create deployment --image nginx --replicas 3 --port 80 --dry-run nginx -o yaml > deploy.yaml

## Lab 2:  Escalado de un Deployment
kubectl scale deployment nginx --replicas 10
kubectl scale deployment nginx --replicas 2

## Lab 3: Actualización y Rollback de un Deployment 


## Lab 4: Eliminar un Deployment y Ver su Comportamiento
kubectl delete pod nginx # se vuelve a recrear
kubectl delete deployment nginx # se elimina por completo