POD=$(kubectl get pod -l app=broker -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward $POD 9092:9092
kafka-topics --create --topic persons --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
kafka-topics --list --bootstrap-server localhost:9092

helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/kafka
helm delete my-release
helm install udaconnect-queue -f values.yaml bitnami/kafka

kubectl run my-release-kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.1-debian-10-r31 --namespace default --command -- sleep infinity
kubectl exec --tty -i my-release-kafka-client --namespace default -- bash



** Please be patient while the chart is being deployed **

Kafka can be accessed by consumers via port 9092 on the following DNS name from within your cluster:

    udaconnect-queue-kafka.default.svc.cluster.local

Each Kafka broker can be accessed by producers via port 9092 on the following DNS name(s) from within your cluster:

    udaconnect-queue-kafka-0.udaconnect-queue-kafka-headless.default.svc.cluster.local:9092

To create a pod that you can use as a Kafka client run the following commands:

    kubectl run udaconnect-queue-kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.1-debian-10-r31 --namespace default --command -- sleep infinity
    kubectl exec --tty -i udaconnect-queue-kafka-client --namespace default -- bash

    PRODUCER:
        kafka-console-producer.sh \
            
            --broker-list udaconnect-queue-kafka-0.udaconnect-queue-kafka-headless.default.svc.cluster.local:9092 \
            --topic test

    CONSUMER:
        kafka-console-consumer.sh \
            
            --bootstrap-server udaconnect-queue-kafka.default.svc.cluster.local:9092 \
            --topic test \
            --from-beginning