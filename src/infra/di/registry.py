from dependency_injector import containers, providers

from src.application.use_cases.process_payment import ProcessPayment
from src.infra.mediator.mediator import Mediator
from src.application.use_cases.get_account import GetAccount
from src.application.use_cases.signup import Signup
from src.infra.database.database_connection import PsycoPgAdapter
from src.infra.gateways.mailer_gateway import MailerGatewayMemory
from src.infra.http.http_server import FlaskAdapter
from src.infra.repositories.account_repository import AccountRepositoryDatabase
from src.infra.repositories.position_repository import PositionRepositoryDatabase
from src.infra.repositories.ride_repository import RideRepositoryDatabase


def setup_mediator() -> Mediator: # type: ignore
    mediator = Mediator()
    process_payment = ProcessPayment()
    
    mediator.register("process_payment", process_payment.execute)
    yield mediator


class Registry(containers.DeclarativeContainer):
    config = providers.Configuration()

    database_connection = providers.Singleton(PsycoPgAdapter)
    account_repository = providers.Singleton(
        AccountRepositoryDatabase, connection=database_connection
    )
    ride_repository = providers.Singleton(RideRepositoryDatabase, connection=database_connection)
    position_repository = providers.Singleton(
        PositionRepositoryDatabase, connection=database_connection
    )
    mailer_gateway = providers.Singleton(MailerGatewayMemory)
    http_server = providers.Singleton(FlaskAdapter)
    signup = providers.Factory(Signup)
    get_account = providers.Factory(GetAccount)
    mediator = providers.Resource(setup_mediator)