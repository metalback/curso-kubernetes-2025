```bash
kubectl exec -it pod-con-cuenta -- sh
ls /var/run/secrets/kubernetes.io/serviceaccount/
cat /var/run/secrets/kubernetes.io/serviceaccount/token
```