from dependency_injector.wiring import Provide, inject

from src.application.use_cases.get_account import GetAccount
from src.application.use_cases.signup import Signup
from src.infra.http.http_server import HttpServer


class AccountController:
    @inject
    def __init__(
        self,
        http_server: HttpServer = Provide['http_server'],
        signup: Signup = Provide['signup'],
        get_account: GetAccount = Provide['get_account'],
    ) -> None:
        self.http_server = http_server
        self.http_server.register('post', '/signup', callback=lambda _, body: signup.execute(body))
        self.http_server.register(
            'get',
            '/accounts/<account_id>',
            callback=lambda params, _: get_account.execute(params['account_id']),
        )
