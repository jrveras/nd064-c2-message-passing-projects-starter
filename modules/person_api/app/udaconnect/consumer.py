#!/usr/bin/env python
import sys
import json
import requests
from confluent_kafka import Consumer

if __name__ == '__main__':

    configConsumer = {'bootstrap.servers': 'my-release-kafka.default.svc.cluster.local:9092', 'group.id': 'python_example_group_1', 'enable.auto.commit': False, 'auto.offset.reset': 'earliest'}
    topic = "person_queue_3"

    # Create Consumer instance
    consumer = Consumer(configConsumer)

    # Subscribe to topic
    consumer.subscribe([topic])
    # msg = consumer.poll(1.0)

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                print("Waiting...")
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                result = msg.value().decode("utf-8")
                np = json.loads(result)
                r = requests.post('http://localhost:30002/api/persons/new', data = np)
                
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.commit(asynchronous=False)
        consumer.close()