import pytest

from src.account_dao import AccountDAOMemory
from src.get_account import GetAccount
from src.signup import Signup


@pytest.fixture(scope='function')
def account_dao():
    return AccountDAOMemory()


@pytest.fixture(scope='function')
def signup(account_dao):
    return Signup(account_dao)


@pytest.fixture(scope='function')
def get_account(account_dao):
    return GetAccount(account_dao)
