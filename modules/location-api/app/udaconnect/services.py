import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.udaconnect.models import Location, Person
from app.udaconnect.schemas import LocationSchema, PersonSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        logger.warning('WARNING: Resultado 1: {}'.format(location))
        logger.warning('WARNING: Resultado 2: {}'.format(coord_text))

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        logger.warning('WARNING: Resultado 3: {}'.format(location))
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        db.session.add(new_location)
        db.session.commit()

        return new_location
    
    # @staticmethod
    # def retrieve_all() -> List[Location]:
    #     locations: List[Location] = db.session.query(Location).all()

    #     # logger.warning('WARNING: Resultado 1: {}'.format(locations))

    #     data = []
    #     for location in locations:
    #         data.append(
    #                 {
    #                     "id": location.id,
    #                     "person_id": location.person_id,
    #                     "longitude": "-106.5721846",
    #                     "latitude": "35.058564",
    #                     "creation_time": '2020-07-07 10:37:06.000000'
    #                 }
    #             )
        
    #     # for location in locations:
    #     #     location = Location(
    #     #             id=location.id,
    #     #             person_id=location.person_id,
    #     #             creation_time=location.creation_time,
    #     #             longitude="" ,
    #     #             latitude=""
    #     #         )

    #     #     data.append(
    #     #         Location(location)
    #     #     )

    #     # # return db.session.query(Location).all()
    #     # logger.warning('WARNING: Resultado 2: {}'.format(data))
    #     for location in data:
    #         # location.wkt_shape = location.coordinate.ST_AsText()
    #         validation_results: Dict = LocationSchema().validate(location)
    #         if validation_results:
    #             logger.warning(f"Unexpected data format in payload JJ New: {validation_results}")
    #             raise Exception(f"Invalid payload: {validation_results}")
    #     return data


class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        db.session.add(new_person)
        db.session.commit()

        return new_person

