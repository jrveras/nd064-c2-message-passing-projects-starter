import json
import logging

from app.udaconnect.models import Location, Person
from app.udaconnect.schemas import (
    LocationSchema,
    PersonSchema,
)
from app.udaconnect.services import LocationService, PersonService
from flask import request, json, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from confluent_kafka import Producer

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa
config = {'bootstrap.servers': 'udaconnect-queue-kafka-0.udaconnect-queue-kafka-headless.default.svc.cluster.local:9092'}
topic = "locations"

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# TODO: This needs better exception handling

@api.route("/locations")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        try:
            payload = request.get_json()
            new_location: Location = LocationService.create(payload)
        except Exception as e:
            response = Response(response=json.dumps({ "ERROR": format(e) }), status=500, mimetype="application/json")
            response.headers["Content-Type"] = "application/json; charset=utf-8"

            return response
        finally:
            producer = Producer(config)
            location = json.dumps(payload)

            producer.produce(topic, location)
            producer.flush()
        
        return new_location

    # @responds(schema=LocationSchema, many=True)
    # def get(self) -> List[Location]:
    #     locations: List[Location] = LocationService.retrieve_all()
    #     return locations

@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location

@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        payload = request.get_json()
        new_person: Person = PersonService.create(payload)
        return new_person