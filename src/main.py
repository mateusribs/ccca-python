from src.infra.controllers.account_controller import AccountController
from src.infra.di.registry import Registry

registry = Registry()
registry.wire(
    modules=[
        'src.application.use_cases.signup',
        'src.application.use_cases.get_account',
        'src.application.use_cases.request_ride',
        'src.application.use_cases.get_ride',
        'src.infra.repositories.account_repository',
        'src.infra.repositories.ride_repository',
        'src.infra.controllers.account_controller',
    ]
)

AccountController()

http_server = registry.http_server().listen('localhost', 3000)
