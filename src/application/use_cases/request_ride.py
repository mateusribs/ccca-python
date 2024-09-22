from dependency_injector.wiring import Provide, inject

from src.domain.factories.ride_factory import create_ride
from src.infra.repositories.account_repository import AccountRepository
from src.infra.repositories.ride_repository import RideRepository


class RequestRide:
    @inject
    def __init__(
        self,
        account_repository: AccountRepository = Provide['account_repository'],
        ride_repository: RideRepository = Provide['ride_repository'],
    ) -> None:
        self.account_repository = account_repository
        self.ride_repository = ride_repository

    def execute(self, input: any):
        account_data = self.account_repository.get_account_by_id(input['passenger_id'])
        if not account_data:
            raise Exception('account does not exist')
        if not account_data.is_passenger:
            raise Exception('account must be from a passenger')
        ride = create_ride(
            passenger_id=input['passenger_id'],
            from_lat=input['from_lat'],
            from_long=input['from_long'],
            to_lat=input['to_lat'],
            to_long=input['to_long'],
        )
        self.ride_repository.save_ride(ride)
        return {'ride_id': ride.get_ride_id()}
