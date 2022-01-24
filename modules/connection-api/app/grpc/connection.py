import time
import os
from datetime import datetime, timedelta
from typing import Dict
import connection_pb2
import connection_pb2_grpc

from sqlalchemy import create_engine
from sqlalchemy.sql import text

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

engine = create_engine(
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True
)

class ConnectionServicer(connection_pb2_grpc.ConnectionServiceServicer):

    def GetList(self, request, context):

        with engine.connect() as con:

            # Prepare arguments for queries
            person_id = request.person_id
            startDate = request.start_date
            endDate = request.end_date
            meters = request.meters
            start_date = datetime.strptime(startDate, '%Y-%m-%d').date()
            end_date = datetime.strptime(endDate, '%Y-%m-%d').date()

            queryPerson = text(
                """
                SELECT company_name, last_name, first_name, id
                FROM   person
                """
            )

            person_map: Dict[str, connection_pb2.Person] = {person.id: person for person in con.execute(queryPerson)}

            queryLocation = text(
                """
                SELECT person_id, id, ST_X(coordinate) AS latitude, ST_Y(coordinate) AS longitude, creation_time
                FROM   location
                WHERE  person_id = :person_id
                AND    TO_DATE(:start_date, 'YYYY-MM-DD') <= creation_time
                AND    TO_DATE(:end_date, 'YYYY-MM-DD') > creation_time;
                """
            )
            paramLocation = { "person_id": person_id, "start_date": startDate, "end_date": endDate}

            data = []
            locations = con.execute(queryLocation, paramLocation)
            for rowLine in locations:
                data.append(
                    {
                        "person_id": person_id,
                        "longitude": rowLine.longitude,
                        "latitude": rowLine.latitude,
                        "meters": meters,
                        "start_date": start_date.strftime("%Y-%m-%d"),
                        "end_date": (end_date + timedelta(days=1)).strftime("%Y-%m-%d"),
                    }
                )

            query = text(
                """
                SELECT  person_id, id, ST_X(coordinate) AS latitude, ST_Y(coordinate) AS longitude, creation_time
                FROM    location
                WHERE   ST_DWithin(coordinate::geography,ST_SetSRID(ST_MakePoint(:latitude,:longitude),4326)::geography, :meters)
                AND     person_id != :person_id
                AND     TO_DATE(:start_date, 'YYYY-MM-DD') <= creation_time
                AND     TO_DATE(:end_date, 'YYYY-MM-DD') > creation_time;
                """
            )
            result = connection_pb2.ConnectionMessageList()
            for line in tuple(data):
                for (
                    exposed_person_id,
                    location_id,
                    exposed_lat,
                    exposed_long,
                    exposed_time,
                ) in con.execute(query, **line):
                    location = connection_pb2.Location(
                        person_id = exposed_person_id,
                        longitude = str(exposed_long),
                        latitude = str(exposed_lat),
                        creation_time = exposed_time.strftime("%m/%d/%Y, %H:%M:%S"),
                        id = location_id
                    )

                    person=connection_pb2.Person(
                        company_name = person_map[exposed_person_id].company_name,
                        last_name = person_map[exposed_person_id].last_name,
                        first_name = person_map[exposed_person_id].first_name,
                        id = person_map[exposed_person_id].id
                    )

                    connection = connection_pb2.ConnectionMessage(
                        location=location,
                        person=person
                    )

                    result.connections.extend([connection])

        return result
