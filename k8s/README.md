Manual management of cluster (accidentally created devops pod):
`root@mineserver:/home/skyline/kuber# kubectl get pods`
```
NAME                          READY   STATUS             RESTARTS   AGE
devops-57dbbbd5dc-v625x       0/1     ImagePullBackOff   0          6m39s
devops-lab-74d47c8987-pdn2s   1/1     Running            0          6m3s
```

`root@mineserver:/home/skyline/kuber# kubectl get svc`
```
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
devops-lab   LoadBalancer   10.101.45.125   <pending>     8080:30932/TCP   4m8s
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          11m
```
Management via config files:
`root@mineserver:/home/skyline/kuber# kubectl get pods,svc`
```
NAME                                    READY   STATUS    RESTARTS   AGE
pod/django-deployment-7c759647f-2f28b   1/1     Running   0          4m47s
pod/django-deployment-7c759647f-wrz4t   1/1     Running   0          4m47s
pod/django-deployment-7c759647f-zfnl8   1/1     Running   0          4m47s

NAME                     TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/django-service   LoadBalancer   10.98.241.62   <pending>     8000:30000/TCP   25s
service/kubernetes       ClusterIP      10.96.0.1      <none>        443/TCP          32m
```