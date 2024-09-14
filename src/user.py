from pydantic import BaseModel


class UserSchema(BaseModel):
    account_id: str
    name: str
    cpf: str
    email: str
    is_driver: bool
    is_passenger: bool
    car_plate: str
    password: str
