import pytest

from src.domain.account import Account


def test_valid_account_creation():
    account = Account(
        account_id='1234',
        name='John Doe',
        email='john.doe@gmail.com',
        cpf='97456321558',
        password='123456',
        car_plate='3214214',
        is_passenger=True,
        is_driver=False,
    )

    assert account
    assert account.get_car_plate() == ''


def test_invalid_account_creation():
    with pytest.raises(Exception, match='invalid car plate'):
        Account(
            account_id='1234',
            name='John Doe',
            email='john.doe@gmail.com',
            cpf='97456321558',
            car_plate='',
            password='123456',
            is_passenger=False,
            is_driver=True,
        )
