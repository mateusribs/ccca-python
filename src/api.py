from driver_app.account_dao import AccountDAODatabase
from driver_app.get_account import GetAccount
from driver_app.signup import Signup
from driver_app.user import UserSchema
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post('/signup')
def signup(user: UserSchema):
    try:
        account_dao = AccountDAODatabase()
        signup = Signup(account_dao)
        output = signup.execute(user)
        return output
    except Exception as err:
        raise HTTPException(status_code=422, detail=err)


@app.get('/accounts/{account_id}')
def get_account_by_id(account_id: str):
    account_dao = AccountDAODatabase()
    get_account = GetAccount(account_dao)
    output = get_account.execute(account_id)
    return output
