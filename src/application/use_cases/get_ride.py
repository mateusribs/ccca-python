from dependency_injector.wiring import Provide, inject

from src.infra.repositories.position_repository import PositionRepository
from src.infra.repositories.ride_repository import RideRepository


class GetRide:
    @inject
    def __init__(
        self,
        ride_repository: RideRepository = Provide['ride_repository'],
        position_repository: PositionRepository = Provide['position_repository'],
    ) -> None:
        self.ride_repository = ride_repository
        self.position_repository = position_repository

    def execute(self, ride_id: str):
        ride = self.ride_repository.get_ride_by_id(ride_id)
        if not ride:
            raise Exception('ride not found')
        positions = self.position_repository.get_position_by_ride_id(ride_id)
        distance = ride.get_distance(positions)
        return {
            'ride_id': ride.get_ride_id(),
            'passenger_id': ride.get_passenger_id(),
            'driver_id': ride.get_driver_id(),
            'from_lat': ride.get_from().get_lat(),
            'from_long': ride.get_from().get_long(),
            'to_lat': ride.get_to().get_lat(),
            'to_long': ride.get_to().get_long(),
            'status': ride.get_status(),
            'positions': positions,
            'distance': distance,
        }
