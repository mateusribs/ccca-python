class Coord:
    def __init__(self, lat: float, long: float) -> None:
        self.__lat, self.__long = self.__validate_coords(lat, long)

    def __validate_coords(self, lat: float, long: float) -> tuple[float]:
        if lat < -90 or lat > 90:
            raise Exception('invalid latitude')

        if long < -180 or long > 180:
            raise Exception('invalid longitude')

        return lat, long

    def get_lat(self) -> float:
        return self.__lat

    def get_long(self) -> float:
        return self.__long
