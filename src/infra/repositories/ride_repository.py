from abc import ABCMeta

from src.domain.ride import Ride
from src.infra.database.database_connection import DatabaseConnection


class RideRepository(metaclass=ABCMeta):
    def get_ride_by_id(ride_id: str) -> Ride:
        raise NotImplementedError

    def save_ride(ride: Ride) -> None:
        raise NotImplementedError


class RideRepositoryDatabase(RideRepository):
    def __init__(self, connection: DatabaseConnection) -> None:
        self.connection = connection

    def get_ride_by_id(self, ride_id: str) -> Ride:
        ride_data = self.connection.get_one('SELECT * FROM ccca.ride WHERE ride_id = %s', [ride_id])
        if not ride_data:
            raise Exception('ride not found')
        return Ride(
            ride_id=ride_data.ride_id,
            passenger_id=ride_data.passenger_id,
            from_lat=ride_data.from_lat,
            from_long=ride_data.from_long,
            to_lat=ride_data.to_lat,
            to_long=ride_data.to_long,
            status=ride_data.status,
            date=ride_data.date,
        )

    def save_ride(self, ride: Ride) -> None:
        self.connection.create(
            """
            INSERT INTO ccca.ride
            (ride_id, passenger_id, from_lat, from_long, to_lat, to_long, status, date)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                ride.get_ride_id(),
                ride.get_passenger_id(),
                ride.get_from().get_lat(),
                ride.get_from().get_long(),
                ride.get_to().get_lat(),
                ride.get_to().get_long(),
                ride.get_status(),
                ride.get_date(),
            ),
        )


class RideRepositoryMemory(RideRepository):
    def __init__(self) -> None:
        self.rides = []

    def get_ride_by_id(self, ride_id: str) -> any:
        for ride in self.rides:
            if ride.get_ride_id() == ride_id:
                return ride
        return None

    def save_ride(self, ride: any) -> any:
        self.rides.append(ride)
