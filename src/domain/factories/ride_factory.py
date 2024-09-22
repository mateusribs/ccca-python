import uuid
from datetime import datetime

from src.domain.ride import Ride


def create_ride(
    passenger_id: str, from_lat: float, from_long: float, to_lat: float, to_long: float
) -> Ride:
    ride_id = uuid.uuid4()
    return Ride(
        ride_id=ride_id,
        passenger_id=passenger_id,
        from_lat=from_lat,
        from_long=from_long,
        to_lat=to_lat,
        to_long=to_long,
        status='requested',
        date=datetime.now(),
    )
