```sh
kubectl run frontend --image=busybox -it --rm --labels="app=frontend" --restart=Never -- sh
wget -qO- backend  # Ahora debería funcionar
```
