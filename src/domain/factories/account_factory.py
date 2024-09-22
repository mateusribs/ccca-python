import uuid

from src.domain.account import Account


def create_account(
    name: str,
    email: str,
    cpf: str,
    car_plate: str,
    password: str,
    is_passenger: bool,
    is_driver: bool,
) -> Account:
    account_id = uuid.uuid4()
    return Account(
        account_id=account_id,
        name=name,
        email=email,
        cpf=cpf,
        car_plate=car_plate,
        password=password,
        is_passenger=is_passenger,
        is_driver=is_driver,
    )
