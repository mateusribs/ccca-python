from abc import ABCMeta

from src.domain.account import Account
from src.infra.database.database_connection import DatabaseConnection


class AccountRepository(metaclass=ABCMeta):
    def get_account_by_email(email: str) -> Account:
        raise NotImplementedError

    def get_account_by_id(account_id: str) -> Account:
        raise NotImplementedError

    def save_account(account: Account) -> None:
        raise NotImplementedError


class AccountRepositoryDatabase(AccountRepository):
    def __init__(self, connection: DatabaseConnection) -> None:
        self.connection = connection

    def get_account_by_email(self, email: str) -> Account:
        account_data = self.connection.get_one(
            'SELECT * FROM ccca.account WHERE email = %s', [email]
        )
        if not account_data:
            return
        return Account(
            account_id=account_data.account_id,
            name=account_data.name,
            email=account_data.email,
            cpf=account_data.cpf,
            car_plate=account_data.car_plate,
            password=account_data.password,
            is_passenger=account_data.is_passenger,
            is_driver=account_data.is_driver,
        )

    def get_account_by_id(self, account_id: str) -> Account:
        account_data = self.connection.get_one(
            'SELECT * FROM ccca.account WHERE account_id = %s', [account_id]
        )
        if not account_data:
            return
        return Account(
            account_id=account_data.account_id,
            name=account_data.name,
            email=account_data.email,
            cpf=account_data.cpf,
            car_plate=account_data.car_plate,
            password=account_data.password,
            is_passenger=account_data.is_passenger,
            is_driver=account_data.is_driver,
        )

    def save_account(self, account: Account) -> None:
        self.connection.create(
            """
            INSERT INTO ccca.account
            (account_id, name, email, cpf, car_plate, is_driver, is_passenger, password)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                account.account_id,
                account.get_name(),
                account.get_email(),
                account.get_cpf(),
                account.get_car_plate(),
                account.is_driver,
                account.is_passenger,
                account.get_password(),
            ),
        )


class AccountRepositoryMemory(AccountRepository):
    def __init__(self) -> None:
        self.accounts = []

    def get_account_by_email(self, email: str) -> any:
        for account in self.accounts:
            if account.get_email() == email:
                return account
        return None

    def get_account_by_id(self, account_id: str) -> any:
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def save_account(self, account: any) -> any:
        self.accounts.append(account)
