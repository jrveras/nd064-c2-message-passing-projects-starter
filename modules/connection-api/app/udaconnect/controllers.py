import json
import logging
import logging.config
import sys

from datetime import datetime

from app.udaconnect.models import Person, Location
from app.udaconnect.schemas import (
    PersonSchema,
    ConnectionSchema,
    LocationSchema,
)
from app.udaconnect.services import PersonService, ConnectionService, LocationService
from flask import request, json, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

class _ExcludeErrorsFilter(logging.Filter):
    def filter(self, record):
        """Only lets through log messages with log level below ERROR (numeric value: 40)."""
        return record.levelno < 40

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
logger = logging.getLogger(__name__)

@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)

        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        return results

@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        payload = request.get_json()
        new_person: Person = PersonService.create(payload)
        return new_person

@api.route("/locations")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        request.get_json()
        location: Location = LocationService.create(request.get_json())
        return location

