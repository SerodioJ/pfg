# KubeEdge configuration

## Cloud

In order to setup KubeEdge's cloud side, the first step is to create a Kubernetes cluster.



And then run the following command to create Cloudcore related resources.
```
kubectl create -f cloud/01-namespace.yaml -f cloud/02-serviceaccount.yaml -f cloud/03-clusterrole.yaml -f cloud/04-clusterrolebinding.yaml -f cloud/05-service.yaml

```

Fill the ADVERTISE_ADDRESS in `cloud/06-configmap.yaml` with the external IP obtained with
```
kubectl get services --namespace=kubeedge
```

Finish resource creation with
```
kubectl create -f cloud/06-configmap.yaml -f cloud/07-deployment.yaml
```

## Edge Device

### Install keadm

As root run
```
docker run --rm kubeedge/installation-package:v1.12.0 cat /usr/local/bin/keadm > /usr/local/bin/keadm && chmod +x /usr/local/bin/keadm
```

### Config Device

Append `cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1` to `/boot/firmware/cmdline.txt` and add the following docker configuration:
```
sudo mkdir -p /etc/systemd/system/docker.service.d/
cat << EOF | sudo tee /etc/systemd/system/docker.service.d/clear_mount_propagtion_flags.conf
[Service]
MountFlags=
EOF
```

After that, reboot the device.

### Connect to cluster

On a machine with kubectl, connect to the cluster control plane and get the `token` to connect with cloudcore with
```
kubectl get secret tokensecret  --namespace=kubeedge -o jsonpath='{.data.tokendata}' | base64 -d
```

Then on the edge device join the cluster by running
```
sudo keadm join --cloudcore-ipport=<ADVERTISE_IP>:10000 --kubeedge-version=1.12.0 --token=<TOKEN>
```

## Cluster Labeling

To facilitate pod placement a good approach is to use custom labels on the nodes, apart from the preset ones.
Good labels are `placement=cloud` or `placement=edge` to differentiate cloud and edge nodes, and also `type=rasp4`, `type=rasp3` and `type=x86` can be used to distinguish edge nodes based on hardware.

`kubectl` can be used to add labels to resources
```
kubectl label nodes <NODE_NAME> <NEW_LABEL, ex: placement=cloud>
```
