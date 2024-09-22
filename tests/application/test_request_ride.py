import random

import pytest


def test_request_ride(signup, request_ride, get_ride):
    input_signup = {
        'name': 'John Doe',
        'email': f'john.doe{random.randint(1, 200)}@gmail.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': True,
        'is_driver': False,
        'car_plate': '',
    }

    output_signup = signup.execute(input_signup)
    output_account_id = output_signup['account_id']

    input_request_ride = {
        'passenger_id': output_account_id,
        'from_lat': -27.584905257808835,
        'from_long': -48.545022195325124,
        'to_lat': -27.496887588317275,
        'to_long': -48.522234807851476,
    }

    output_request_ride = request_ride.execute(input_request_ride)
    assert output_request_ride['ride_id']
    output_get_ride = get_ride.execute(output_request_ride['ride_id'])
    assert output_get_ride['ride_id'] == output_request_ride['ride_id']
    assert output_get_ride['passenger_id'] == input_request_ride['passenger_id']
    assert pytest.approx(output_get_ride['from_lat']) == input_request_ride['from_lat']
    assert pytest.approx(output_get_ride['from_long']) == input_request_ride['from_long']
    assert pytest.approx(output_get_ride['to_lat']) == input_request_ride['to_lat']
    assert pytest.approx(output_get_ride['to_long']) == input_request_ride['to_long']
    assert output_get_ride['status'] == 'requested'


def test_not_request_ride_when_not_is_passenger(signup, request_ride):
    with pytest.raises(Exception, match='account must be from a passenger'):
        input_signup = {
            'name': 'John Doe',
            'email': f'john.doe{random.randint(1, 200)}@gmail.com',
            'cpf': '97456321558',
            'password': '123456',
            'is_passenger': False,
            'is_driver': True,
            'car_plate': 'AAA1234',
        }

        output_signup = signup.execute(input_signup)
        output_account_id = output_signup['account_id']

        input_request_ride = {
            'passenger_id': output_account_id,
            'from_lat': -27.584905257808835,
            'from_long': -48.545022195325124,
            'to_lat': -27.496887588317275,
            'to_long': -48.522234807851476,
        }

        request_ride.execute(input_request_ride)
