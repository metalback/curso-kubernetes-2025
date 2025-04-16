```bash
kubectl auth can-i list pods --as=juan
kubectl auth can-i delete pods --as=juan  # Debería responder: no
```