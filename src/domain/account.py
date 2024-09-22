from src.domain.car_plate import CarPlate
from src.domain.cpf import CPF
from src.domain.email import Email
from src.domain.name import Name
from src.domain.password import Password


class Account:
    def __init__(
        self,
        account_id: str,
        name: str,
        email: str,
        cpf: str,
        car_plate: str,
        password: str,
        is_passenger: bool,
        is_driver: bool,
    ):
        self.__name = Name(name)
        self.__email = Email(email)
        self.__cpf = CPF(cpf)
        self.__password = Password(password)
        self.__car_plate = CarPlate(car_plate) if is_driver else ''

        self.account_id = account_id
        self.is_passenger = is_passenger
        self.is_driver = is_driver

    def get_email(self) -> str:
        return self.__email.get_value()

    def get_name(self) -> str:
        return self.__name.get_value()

    def get_cpf(self) -> str:
        return self.__cpf.get_value()

    def get_password(self) -> str:
        return self.__password.get_value()

    def get_car_plate(self) -> str:
        return self.__car_plate.get_value() if self.is_driver else ''
