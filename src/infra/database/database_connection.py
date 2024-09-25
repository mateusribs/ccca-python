from abc import ABCMeta, abstractmethod

import psycopg
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
        self.connection = psycopg.connect('postgres://postgres:123456@localhost:5432/app')
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
