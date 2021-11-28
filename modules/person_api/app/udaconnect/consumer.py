#!/usr/bin/env python
import sys
import json
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Consumer, OFFSET_BEGINNING
from app.udaconnect.services import PersonService
from app.udaconnect.models import Person


if __name__ == '__main__':
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('--reset', action='store_true')
    args = parser.parse_args()

    config = {'bootstrap.servers': 'my-release-kafka.default.svc.cluster.local:9092', 'group.id': 'python_example_group_1', 'auto.offset.reset': 'earliest'}

    # Create Consumer instance
    consumer = Consumer(config)

    # Set up a callback to handle the '--reset' flag.
    def reset_offset(consumer, partitions):
        if args.reset:
            for p in partitions:
                p.offset = OFFSET_BEGINNING
            consumer.assign(partitions)

    # Subscribe to topic
    topic = "persons"
    consumer.subscribe([topic], on_assign=reset_offset)

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                print("Waiting...")
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                # Extract the (optional) key and value, and print.

                result = msg.value().decode("utf-8")
                # response = json.loads(result)
                new_person: Person = PersonService.create(result)

                # print("Consumed event from topic {topic}: {person}".format(
                #     topic=msg.topic(), person=response["company_name"]))
                print("Consumed event from topic {topic}: {person}".format(
                    topic=msg.topic(), person=msg.value().decode("utf-8")))
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()