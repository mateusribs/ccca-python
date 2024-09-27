from dependency_injector.wiring import Provide, inject

from src.domain.factories.position_factory import create_position
from src.infra.repositories.position_repository import PositionRepository
from src.infra.repositories.ride_repository import RideRepository


class UpdatePosition:
    @inject
    def __init__(
        self,
        position_repository: PositionRepository = Provide['position_repository'],
        ride_repository: RideRepository = Provide['ride_repository'],
    ) -> None:
        self.position_repository = position_repository
        self.ride_repository = ride_repository

    def execute(self, input: any):
        ride_data = self.ride_repository.get_ride_by_id(input['ride_id'])
        if not ride_data:
            raise Exception('ride not found')
        position = create_position(ride_id=input['ride_id'], lat=input['lat'], long=input['long'])
        self.position_repository.save_position(position)
