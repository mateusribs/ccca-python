import re
import uuid

from driver_app.account_dao import AccountDAO
from driver_app.validate_cpf import validate_cpf


class Signup:
    def __init__(self, account_dao: AccountDAO) -> None:
        self.account_dao = account_dao

    def execute(self, input: any):
        input['account_id'] = uuid.uuid4()
        account_data = self.account_dao.get_account_by_email(input['email'])
        if account_data:
            raise Exception('duplicated account')
        if not re.match(r'[a-zA-Z]+ [a-zA-Z]+', input['name']):
            raise Exception('invalid name')
        if not re.match(r'^(.+)@(.+)$', input['email']):
            raise Exception('invalid email')
        if not validate_cpf(input['cpf']):
            raise Exception('invalid cpf')
        if input['is_driver'] and not re.match(r'[A-Z]{3}[0-9]{4}', input['car_plate']):
            raise Exception('invalid car plate')
        self.account_dao.save_account(input)

        return {'account_id': input['account_id']}
