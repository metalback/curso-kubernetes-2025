```sh
kubectl run test --rm -it --image=busybox --restart=Never -- sh
wget -qO- backend  # Esto debería fallar
```
