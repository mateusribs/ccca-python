from abc import ABCMeta

import psycopg


class AccountDAO(metaclass=ABCMeta):
    def get_account_by_email(email: str) -> any:
        raise NotImplementedError

    def get_account_by_id(account_id: str) -> any:
        raise NotImplementedError

    def save_account(account: any) -> any:
        raise NotImplementedError


class AccountDAODatabase(AccountDAO):
    def get_account_by_email(self, email: str) -> any:
        with psycopg.connect('postgres://postgres:123456@localhost:5432/app') as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM ccca.account WHERE email = %s', [email])
                account_data = cursor.fetchone()
        return account_data

    def get_account_by_id(self, account_id: str) -> any:
        with psycopg.connect('postgres://postgres:123456@localhost:5432/app') as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM ccca.account WHERE account_id = %s', [account_id])
                account_data = cursor.fetchone()
        return account_data

    def save_account(self, account: any) -> any:
        with psycopg.connect('postgres://postgres:123456@localhost:5432/app') as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO ccca.account
                    (account_id, name, email, cpf, car_plate, is_driver, password)
                    VALUES
                    (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        account.account_id,
                        account.name,
                        account.email,
                        account.cpf,
                        account.car_plate,
                        account.is_driver,
                        account.password,
                    ),
                )
                connection.commit()


class AccountDAOMemory(AccountDAO):
    def __init__(self) -> None:
        self.accounts = []

    def get_account_by_email(self, email: str) -> any:
        for account in self.accounts:
            if account['email'] == email:
                return account
        return None

    def get_account_by_id(self, account_id: str) -> any:
        for account in self.accounts:
            if account['account_id'] == account_id:
                return account
        return None

    def save_account(self, account: any) -> any:
        self.accounts.append(account)
