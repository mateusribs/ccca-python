import random

import pytest


def test_signup_create_valid_passenger_account(signup, get_account):
    input = {
        'name': 'John Doe',
        'email': f'john.doe{random.randint(1, 200)}@gmail.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': True,
        'is_driver': False,
        'car_plate': '',
    }

    output = signup.execute(input)
    assert output
    output_get_account = get_account.execute(output['account_id'])
    assert output_get_account['name'] == input['name']
    assert output_get_account['email'] == input['email']
    assert output_get_account['cpf'] == input['cpf']
    assert output_get_account['password'] == input['password']
    assert output_get_account['is_passenger'] == input['is_passenger']


def test_signup_create_valid_driver_account(signup, get_account):
    input = {
        'name': 'John Doe',
        'email': f'john.doe{random.randint(1, 200)}@gmail.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': False,
        'is_driver': True,
        'car_plate': 'AAA1234',
    }

    output = signup.execute(input)
    assert output
    output_get_account = get_account.execute(output['account_id'])
    assert output_get_account['name'] == input['name']
    assert output_get_account['email'] == input['email']
    assert output_get_account['cpf'] == input['cpf']
    assert output_get_account['password'] == input['password']
    assert output_get_account['is_driver'] == input['is_driver']
    assert output_get_account['car_plate'] == input['car_plate']


def test_signup_not_create_invalid_passenger_account(signup):
    input = {
        'name': 'John',
        'email': f'john.doe{random.randint(1, 200)}@gmail.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': True,
        'is_driver': False,
        'car_plate': '',
    }

    with pytest.raises(Exception, match='invalid name'):
        signup.execute(input)


def test_signup_not_create_invalid_driver_account(signup):
    input = {
        'name': 'John Doe',
        'email': f'john.doe{random.randint(1, 200)}@gmail.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': False,
        'is_driver': True,
        'car_plate': 'AAA123',
    }

    with pytest.raises(Exception, match='invalid car plate'):
        signup.execute(input)
