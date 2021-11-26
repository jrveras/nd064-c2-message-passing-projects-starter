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

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa
config = {'bootstrap.servers': 'my-release-kafka-0.my-release-kafka-headless.default.svc.cluster.local:9092'}
topic = "persons"


# TODO: This needs better exception handling

@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        producer = Producer(config)
        payload = request.get_json()
        print('WARNING: Message args 3: {}'.format(payload))
        producer.produce(topic, "TRICOLOR")
        producer.poll(10000)
        producer.flush()

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