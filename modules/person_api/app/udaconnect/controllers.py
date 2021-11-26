from datetime import datetime

from app.udaconnect.models import Person
from app.udaconnect.schemas import (
    PersonSchema,
)
from app.udaconnect.services import PersonService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
from confluent_kafka import Producer
import json
import logging
import logging.config
import sys

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa
config = {'bootstrap.servers': 'my-release-kafka-0.my-release-kafka-headless.default.svc.cluster.local:9092'}
topic = "persons"


# TODO: This needs better exception handling
configLog = {
        'version': 1,
        'filters': {
            'exclude_errors': {
                '()': _ExcludeErrorsFilter
            }
        },
        'formatters': {
            # Modify log message format here or replace with your custom formatter class
            'customFormatter': {
                'format': '%(asctime)s:%(levelname)s:%(name)s:[%(filename)s.%(funcName)s:%(lineno)d]:%(levelno)s:%(message)s'
            }
        },
        'handlers': {
            'console_stderr': {
                # Sends log messages with log level ERROR or higher to stderr
                'class': 'logging.StreamHandler',
                'level': 'ERROR',
                'formatter': 'customFormatter',
                'stream': sys.stderr
            },
            'console_stdout': {
                # Sends log messages with log level lower than ERROR to stdout
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'customFormatter',
                'filters': ['exclude_errors'],
                'stream': sys.stdout
            },
            'file_stderr': {
                # Sends all log messages to a file
                'class': 'logging.FileHandler',
                'level': 'ERROR',
                'formatter': 'customFormatter',
                'filename': 'stderr.log',
                'encoding': 'utf8'
            },
            'file_stdout': {
                # Sends all log messages to a file
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'customFormatter',
                'filters': ['exclude_errors'],
                'filename': 'stdout.log',
                'encoding': 'utf8'
            }
        },
        'root': {
            # In general, this should be kept at 'NOTSET'.
            # Otherwise it would interfere with the log levels set for each handler.
            'level': 'NOTSET',
            'handlers': ['console_stderr', 'console_stdout', 'file_stderr', 'file_stdout']
        },
    }

logging.config.dictConfig(configLog)
logger = logging.getLogger("udaconnect-person-api")

@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        producer = Producer(config)
        payload = request.get_json()

        producer.produce(topic, "TRICOLOR")
        producer.poll(10000)
        producer.flush()

        logger.debug('WARNING: Message args 3: {}'.format(payload))
        logger.debug('WARNING: TRICOLOR')

        new_person: Person = PersonService.create(payload)
        return new_person

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        persons: List[Person] = PersonService.retrieve_all()
        return persons


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person