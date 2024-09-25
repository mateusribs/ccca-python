import random

import pytest

from src.application.use_cases.accept_ride import AcceptRide
from src.application.use_cases.get_account import GetAccount
from src.application.use_cases.get_ride import GetRide
from src.application.use_cases.request_ride import RequestRide
from src.application.use_cases.signup import Signup
from src.application.use_cases.start_ride import StartRide
from src.infra.di.registry import Registry


@pytest.fixture
def registry():
    registry = Registry()
    # registry.account_repository.override(AccountRepositoryMemory())
    # registry.ride_repository.override(RideRepositoryMemory())
    registry.wire(
        modules=[
            'src.application.use_cases.signup',
            'src.application.use_cases.get_account',
            'src.application.use_cases.request_ride',
            'src.application.use_cases.get_ride',
            'src.application.use_cases.accept_ride',
            'src.application.use_cases.start_ride',
            'src.infra.repositories.account_repository',
            'src.infra.repositories.ride_repository',
            'src.infra.controllers.account_controller',
        ]
    )
    yield registry
    registry.unwire()


@pytest.fixture(scope='function')
def signup(registry):
    return Signup()


@pytest.fixture(scope='function')
def get_account(registry):
    return GetAccount()


@pytest.fixture(scope='function')
def request_ride(registry):
    return RequestRide()


@pytest.fixture(scope='function')
def get_ride(registry):
    return GetRide()


@pytest.fixture(scope='function')
def accept_ride(registry):
    return AcceptRide()


@pytest.fixture(scope='function')
def start_ride(registry):
    return StartRide()


@pytest.fixture
def passenger(signup):
    input_signup = {
        'name': 'John Doe',
        'email': f'john.doe{random.randint(1, 2000)}@gmail.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': True,
        'is_driver': False,
        'car_plate': '',
    }

    output_signup = signup.execute(input_signup)
    return output_signup


@pytest.fixture
def driver(signup):
    input_signup = {
        'name': 'Joao Gomes',
        'email': f'joao.gomes{random.randint(1, 2000)}@gmail.com',
        'cpf': '97456321558',
        'password': '123456',
        'is_passenger': False,
        'is_driver': True,
        'car_plate': 'AAA1234',
    }

    output_signup = signup.execute(input_signup)
    return output_signup


@pytest.fixture
def ride_requested(passenger, request_ride):
    input_request_ride = {
        'passenger_id': passenger['account_id'],
        'from_lat': -27.584905257808835,
        'from_long': -48.545022195325124,
        'to_lat': -27.496887588317275,
        'to_long': -48.522234807851476,
    }

    output_request_ride = request_ride.execute(input_request_ride)
    return output_request_ride


@pytest.fixture
def ride_accepted(ride_requested, driver):
    input_accept_ride = {
        'ride_id': ride_requested['ride_id'],
        'driver_id': driver['account_id'],
    }

    accept_ride.execute(input_accept_ride)
