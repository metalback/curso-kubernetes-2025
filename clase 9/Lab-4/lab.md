🎯 Objetivo:
Verificar los permisos que tiene un usuario y listar los roles asignados.

🧪 Pasos:
1. Ver si el usuario puede obtener Deployments:
```sh
kubectl auth can-i get deployments --as=juan
```
2. Ver todos los RoleBindings y ClusterRoleBindings:
```sh
kubectl get rolebindings --all-namespaces
kubectl get clusterrolebindings
```
3. Ver los permisos exactos asignados a un Role:
```sh
kubectl describe role lector-pods -n default
```
