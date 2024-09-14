import pytest
from driver_app.account_dao import AccountDAOMemory
from driver_app.get_account import GetAccount
from driver_app.signup import Signup


@pytest.fixture(scope='function')
def account_dao():
    return AccountDAOMemory()


@pytest.fixture(scope='function')
def signup(account_dao):
    return Signup(account_dao)


@pytest.fixture(scope='function')
def get_account(account_dao):
    return GetAccount(account_dao)
