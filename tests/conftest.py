import pytest

from src.application.use_cases.get_account import GetAccount
from src.application.use_cases.get_ride import GetRide
from src.application.use_cases.request_ride import RequestRide
from src.application.use_cases.signup import Signup
from src.infra.di.registry import Registry
from src.infra.repositories.account_repository import AccountRepositoryMemory
from src.infra.repositories.ride_repository import RideRepositoryMemory


@pytest.fixture
def registry():
    registry = Registry()
    registry.account_repository.override(AccountRepositoryMemory())
    registry.ride_repository.override(RideRepositoryMemory())
    registry.wire(
        modules=[
            'src.application.use_cases.signup',
            'src.application.use_cases.get_account',
            'src.application.use_cases.request_ride',
            'src.application.use_cases.get_ride',
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
