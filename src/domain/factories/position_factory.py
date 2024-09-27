import uuid
from datetime import datetime

from src.domain.entities.position import Position


def create_position(
    ride_id: str, lat: float, long: float, date: datetime = datetime.now(), position_id: str = ''
):
    if not position_id:
        position_id = uuid.uuid4()
    return Position(position_id=position_id, ride_id=ride_id, lat=lat, long=long, date=date)
