import re


class Name:
    def __init__(self, value: str) -> None:
        self.__value = self.__validate(value)

    def __validate(self, value: str) -> str:
        if not re.match(r'[a-zA-Z]+ [a-zA-Z]+', value):
            raise Exception('invalid name')
        return value

    def get_value(self) -> str:
        return self.__value
