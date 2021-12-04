POD=$(kubectl get pod -l app=broker -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward $POD 9092:9092
kafka-topics --create --topic persons --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
kafka-topics --list --bootstrap-server localhost:9092

helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/kafka
helm delete my-release
helm install my-release -f values.yaml bitnami/kafka

kubectl run my-release-kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.1-debian-10-r31 --namespace default --command -- sleep infinity
kubectl exec --tty -i my-release-kafka-client --namespace default -- bash