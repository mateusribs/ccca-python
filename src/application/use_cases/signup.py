from dependency_injector.wiring import Provide, inject

from src.domain.factories.account_factory import create_account
from src.infra.gateways.mailer_gateway import MailerGateway
from src.infra.repositories.account_repository import AccountRepository


class Signup:
    @inject
    def __init__(
        self,
        account_repository: AccountRepository = Provide['account_repository'],
        mailer_gateway: MailerGateway = Provide['mailer_gateway'],
    ) -> None:
        self.account_repository = account_repository
        self.mailer_gateway = mailer_gateway

    def execute(self, input: any):
        account = create_account(
            name=input['name'],
            email=input['email'],
            cpf=input['cpf'],
            car_plate=input['car_plate'],
            password=input['password'],
            is_passenger=input['is_passenger'],
            is_driver=input['is_driver'],
        )

        account_data = self.account_repository.get_account_by_email(input['email'])
        if account_data:
            raise Exception('duplicated account')
        self.account_repository.save_account(account)
        self.mailer_gateway.send(account.get_email(), 'Welcome!', '...')

        return {'account_id': account.account_id}
