#!/usr/bin/env python

import sys
import json
import logging
import requests
from argparse import ArgumentParser
from confluent_kafka import Consumer, OFFSET_BEGINNING

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--reset', action='store_true')
    args = parser.parse_args()

    config = {'bootstrap.servers': 'udaconnect-queue-kafka.default.svc.cluster.local:9092', 'group.id': 'python_example_group_1', 'auto.offset.reset': 'earliest'}

    # Create Consumer instance
    consumer = Consumer(config)

    # Set up a callback to handle the '--reset' flag.
    def reset_offset(consumer, partitions):
        if args.reset:
            for p in partitions:
                p.offset = OFFSET_BEGINNING
            consumer.assign(partitions)

    topic = "persons"
    consumer.subscribe([topic], on_assign=reset_offset)

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                logger.debug('DEBUG: Waiting...')
            elif msg.error():
                logger.debug('ERROR: %s'.format(msg.error()))
            else:
                result = msg.value().decode("utf-8")
                newPerson = json.loads(result)
                logger.debug("Consumed event from topic {topic}: {person}".format(
                    topic=msg.topic(), person=msg.value().decode("utf-8")))
                # response = requests.get('http://udaconnect-location-api.default.svc.cluster.local:5000/api/locations/47')
                response = requests.post('http://udaconnect-location-api.default.svc.cluster.local:5000/api/persons', data = newPerson)
                logger.debug(response.text)
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()