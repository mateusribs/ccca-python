from dependency_injector.wiring import Provide, inject

from src.infra.mediator.mediator import Mediator
from src.application.use_cases.process_payment import ProcessPayment
from src.infra.repositories.position_repository import PositionRepository
from src.infra.repositories.ride_repository import RideRepository


class FinishRide:
    @inject
    def __init__(
        self,
        position_repository: PositionRepository = Provide['position_repository'],
        ride_repository: RideRepository = Provide['ride_repository'],
        mediator: Mediator = Provide['mediator']
    ) -> None:
        self.position_repository = position_repository
        self.ride_repository = ride_repository
        self.mediator = mediator

    def execute(self, input: any):
        ride_data = self.ride_repository.get_ride_by_id(input['ride_id'])
        if not ride_data:
            raise Exception('ride not found')
        positions = self.position_repository.get_position_by_ride_id(input['ride_id'])
        ride_data.finish(positions)
        self.ride_repository.update_ride(ride_data)
        self.mediator.notify("ride_completed", {'ride_id': ride_data.get_ride_id(), 'amount': ride_data.get_fare()})
