from dependency_injector.wiring import Provide, inject

from src.infra.repositories.account_repository import AccountRepository


class GetAccount:
    @inject
    def __init__(
        self, account_repository: AccountRepository = Provide['account_repository']
    ) -> None:
        self.account_repository = account_repository

    def execute(self, account_id: str):
        account_data = self.account_repository.get_account_by_id(account_id)
        return {
            'account_id': account_data.account_id,
            'name': account_data.get_name(),
            'cpf': account_data.get_cpf(),
            'email': account_data.get_email(),
            'password': account_data.get_password(),
            'car_plate': account_data.get_car_plate(),
            'is_passenger': account_data.is_passenger,
            'is_driver': account_data.is_driver,
        }
