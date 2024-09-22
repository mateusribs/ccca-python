import re


class Email:
    def __init__(self, value: str) -> None:
        self.__value = self.__validate(value)

    def __validate(self, value: str) -> str:
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
            raise Exception('invalid email')
        return value

    def get_value(self) -> str:
        return self.__value
