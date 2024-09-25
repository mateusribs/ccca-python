from abc import ABCMeta, abstractmethod

import psycopg
from decouple import config
from psycopg.rows import namedtuple_row


class DatabaseConnection(metaclass=ABCMeta):
    @abstractmethod
    def get_one(self, statement: str, params: any) -> any:
        raise NotImplementedError

    @abstractmethod
    def persist(self, statement: str, params: any) -> None:
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError


class PsycoPgAdapter(DatabaseConnection):
    def __init__(self) -> None:
        database_url = config('DATABASE_URL', cast=str)
        self.connection = psycopg.connect(database_url)
        self.connection.adapters.register_loader('numeric', psycopg.types.numeric.FloatLoader)
        self.connection.row_factory = namedtuple_row

    def get_one(self, statement: str, params: any) -> any:
        data = self.connection.execute(statement, params).fetchone()
        return data

    def persist(self, statement: str, params: any) -> None:
        self.connection.execute(statement, params)
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
