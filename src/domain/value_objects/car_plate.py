import re


class CarPlate:
    def __init__(self, value: str) -> None:
        self.__value = self.__validate(value)

    def __validate(self, value: str) -> str:
        if not re.match(r'[A-Z]{3}[0-9]{4}', value):
            raise Exception('invalid car plate')
        return value

    def get_value(self) -> str:
        return self.__value
