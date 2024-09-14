import random

import pytest


def test_signup_create_passanger_account(signup, get_account):
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


def test_signup_not_create_with_invalid_name(signup):
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


def test_signup_not_create_with_invalid_email(signup):
    input = {
        'name': 'John Doe',
        'email': 'john.doe.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': True,
        'is_driver': False,
        'car_plate': '',
    }

    with pytest.raises(Exception, match='invalid email'):
        signup.execute(input)


def test_signup_not_create_with_invalid_cpf(signup):
    input = {
        'name': 'John Doe',
        'email': f'john.doe{random.randint(1, 200)}@gmail.com',
        'cpf': '9745632155',
        'password': '123456',
        'is_passenger': True,
        'is_driver': False,
        'car_plate': '',
    }

    with pytest.raises(Exception, match='invalid cpf'):
        signup.execute(input)


def test_signup_not_create_when_duplicated_email(signup):
    input = {
        'name': 'John Doe',
        'email': f'john.doe{random.randint(1, 200)}@gmail.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': True,
        'is_driver': False,
        'car_plate': '',
    }

    signup.execute(input)

    with pytest.raises(Exception, match='duplicated account'):
        signup.execute(input)


def test_signup_not_create_with_invalid_car_plate(signup):
    input = {
        'name': 'John Doe',
        'email': f'john.doe{random.randint(1, 200)}@gmail.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': True,
        'is_driver': True,
        'car_plate': '40000',
    }

    with pytest.raises(Exception, match='invalid car plate'):
        signup.execute(input)
