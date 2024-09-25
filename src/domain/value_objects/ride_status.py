class RideStatus:
    def __init__(self, status: str) -> None:
        self.__value = status

    def get_value(self) -> str:
        return self.__value

    def accept(self):
        if self.__value != 'requested':
            raise Exception('invalid status')
        self.__value = 'accepted'

    def in_progress(self):
        if self.__value != 'accepted':
            raise Exception('invalid status')
        self.__value = 'in_progress'
