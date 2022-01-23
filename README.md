# UdaConnect

## Running the app
The project has been set up such that you should be able to have the project up and running with Kubernetes. \
**Run all the commands at the project root.**

### Prerequisites
We will be installing the tools that we'll need to use for getting our environment set up properly.
1. [Install Docker](https://docs.docker.com/get-docker/)
2. [Set up `kubectl`](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/cluster-access/kubectl/)
3. [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads) with at least version 6.0
4. [Install Vagrant](https://www.vagrantup.com/docs/installation) with at least version 2.0

### Initialize K3s
```bash
$ vagrant up
```

### Install Kafka
Add bitnami chart in the helm repo and install kafka (Message Queue)
```bash
$ helm repo add bitnami https://charts.bitnami.com/bitnami

$ helm install udaconnect-queue -f helm/values.yaml bitnami/kafka
```

### Initialize k8s manifest
```bash
$ kubectl apply -f deployment/.
```

### Configure Database
```bash
$ sh scripts/run_db_command.sh $(kubectl get pods --all-namespaces -o=jsonpath="{.items[0].metadata.name}" -l app=postgres-person)
$ sh scripts/run_db_command.sh $(kubectl get pods --all-namespaces -o=jsonpath="{.items[0].metadata.name}" -l app=postgres-location)
$ sh scripts/run_db_command.sh $(kubectl get pods --all-namespaces -o=jsonpath="{.items[0].metadata.name}" -l app=postgres-connection)
```


## Verifying it Works
These pages should also load on your web browser:
* `http://localhost:30001/` - OpenAPI Documentation
* `http://localhost:30001/api/` - Base path for Location API
* `http://localhost:30002/api/` - Base path for Person API
* `http://localhost:30003/api/` - Base path for Vacation API
* `http://localhost:30000/` - Frontend ReactJS Application


## Set up gRPC
### Start gRPC Server
```bash
$ kubectl exec -it $(kubectl get pods --all-namespaces -o=jsonpath="{.items[0].metadata.name}" -l service=udaconnect-connection-api) /bin/sh
$ python3 /app/grpc/app.py
```
### Execute gRPC Client
Open new terminal window. \
Args - 1: person_id 2: start_date 3: end_date 4: meters \
Example - getter.py 2 2020-01-01 2020-12-30 5
```bash
$ kubectl exec -it $(kubectl get pods --all-namespaces -o=jsonpath="{.items[0].metadata.name}" -l service=udaconnect-connection-api) /bin/sh
$ python3 /app/grpc/getter.py 2 2020-01-01 2020-12-30 5
```
