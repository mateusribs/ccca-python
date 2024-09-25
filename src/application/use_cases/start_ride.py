from dependency_injector.wiring import Provide, inject

from src.infra.repositories.ride_repository import RideRepository


class StartRide:
    @inject
    def __init__(
        self,
        # account_repository: AccountRepository = Provide['account_repository'],
        ride_repository: RideRepository = Provide['ride_repository'],
    ) -> None:
        # self.account_repository = account_repository
        self.ride_repository = ride_repository

    def execute(self, input: any):
        ride_data = self.ride_repository.get_ride_by_id(input['ride_id'])
        # account_data = self.account_repository.get_account_by_id(input['driver_id'])
        # if not account_data.is_driver:
        # raise Exception('must be driver to accept ride')
        ride_data.start()
        self.ride_repository.update_ride(ride_data)
