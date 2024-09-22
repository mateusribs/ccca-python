from datetime import datetime

from src.domain.coord import Coord


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
    ) -> None:
        self.__ride_id = ride_id
        self.__passenger_id = passenger_id
        self.__from = Coord(from_lat, from_long)
        self.__to = Coord(to_lat, to_long)
        self.__status = status
        self.__date = date

    def get_ride_id(self) -> str:
        return self.__ride_id

    def get_passenger_id(self) -> str:
        return self.__passenger_id

    def get_from(self) -> Coord:
        return self.__from

    def get_to(self) -> Coord:
        return self.__to

    def get_status(self) -> str:
        return self.__status

    def get_date(self) -> datetime:
        return self.__date
