from src.account_dao import AccountDAO


class GetAccount:
    def __init__(self, account_dao: AccountDAO) -> None:
        self.account_dao = account_dao

    def execute(self, account_id: str):
        account_data = self.account_dao.get_account_by_id(account_id)
        return account_data
