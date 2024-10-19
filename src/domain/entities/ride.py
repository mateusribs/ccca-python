from datetime import datetime

from src.domain.services.distance_calculator import calculate_distance_by_positions
from src.domain.value_objects.coord import Coord
from src.domain.value_objects.ride_status import RideStatus


class Ride:
    def __init__(
        self,
        ride_id: str,
        passenger_id: str,
        from_lat: float,
        from_long: float,
        to_lat: float,
        to_long: float,
        status: str,
        date: datetime,
        driver_id: str = '',
        distance: int = 0,
        fare: float = 0.0,
    ) -> None:
        self.__ride_id = ride_id
        self.__passenger_id = passenger_id
        self.__driver_id = driver_id
        self.__from = Coord(from_lat, from_long)
        self.__to = Coord(to_lat, to_long)
        self.__status = RideStatus(status)
        self.__date = date
        self.__distance = distance
        self.__fare = fare

    def get_ride_id(self) -> str:
        return self.__ride_id

    def get_passenger_id(self) -> str:
        return self.__passenger_id

    def get_from(self) -> Coord:
        return self.__from

    def get_to(self) -> Coord:
        return self.__to

    def get_status(self) -> str:
        return self.__status.get_value()

    def get_date(self) -> datetime:
        return self.__date

    def get_driver_id(self) -> str:
        return self.__driver_id

    def accept(self, driver_id: str) -> None:
        self.__driver_id = driver_id
        self.__status.accept()

    def start(self) -> None:
        self.__status.in_progress()

    def get_fare(self) -> float:
        return self.__fare

    def get_distance(self) -> int:
        return self.__distance

    def finish(self, positions: list):
        distance = calculate_distance_by_positions(positions)
        self.__distance = distance
        self.__fare = distance * 2.1
        self.__status.finish()
