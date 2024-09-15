from src.account_dao import AccountDAODatabase
from src.get_account import GetAccount
from src.signup import Signup
from src.user import UserSchema
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
