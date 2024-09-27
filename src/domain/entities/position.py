from datetime import datetime

from src.domain.value_objects.coord import Coord


class Position:
    def __init__(
        self,
        position_id: str,
        ride_id: str,
        lat: float,
        long: float,
        date: datetime,
    ) -> None:
        self.__position_id = position_id
        self.__ride_id = ride_id
        self.__coord = Coord(lat=lat, long=long)
        self.__date = date

    def get_position_id(self) -> str:
        return self.__position_id

    def get_ride_id(self) -> str:
        return self.__ride_id

    def get_coord(self) -> Coord:
        return self.__coord

    def get_date(self) -> datetime:
        return self.__date
