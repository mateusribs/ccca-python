from abc import ABCMeta, abstractmethod

from src.domain.entities.position import Position
from src.domain.factories.position_factory import create_position
from src.infra.database.database_connection import DatabaseConnection


class PositionRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_position_by_ride_id(self, ride_id: str) -> Position:
        raise NotImplementedError

    @abstractmethod
    def save_position(self, position: Position) -> None:
        raise NotImplementedError


class PositionRepositoryDatabase(PositionRepository):
    def __init__(self, connection: DatabaseConnection) -> None:
        self.connection = connection

    def get_position_by_ride_id(self, ride_id: str) -> Position:
        positions_data = self.connection.get_all(
            'SELECT * FROM ccca.position WHERE ride_id = %s order by date', [ride_id]
        )
        if not positions_data:
            raise Exception('positions not found')
        return [
            create_position(
                ride_id=position.ride_id,
                lat=position.lat,
                long=position.long,
                date=position.date,
                position_id=position.position_id,
            )
            for position in positions_data
        ]

    def save_position(self, position: Position) -> None:
        self.connection.persist(
            """
            INSERT INTO ccca.position
            (position_id, ride_id, lat, long, date)
            VALUES
            (%s, %s, %s, %s, %s)
            """,
            (
                position.get_position_id(),
                position.get_ride_id(),
                position.get_coord().get_lat(),
                position.get_coord().get_long(),
                position.get_date(),
            ),
        )
