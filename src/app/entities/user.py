from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class User:
    name: str
    balance: int

    def __init__(self, name: str, balance: int = 0):
        validation_name = self.validate_name(name)
        if not validation_name[0]:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_balance = self.validate_balance(balance)
        if not validation_balance[0]:
            raise ParamNotValidated("balance", validation_balance[1])
        self.balance = balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return False, "Name is required"
        if not isinstance(name, str):
            return False, "Name must be a string"
        if len(name) < 2:
            return False, "Name must be at least 2 characters long"
        return True, ""

    @staticmethod
    def validate_balance(balance: int) -> Tuple[bool, str]:
        if balance is None:
            return False, "Balance is required"
        if not isinstance(balance, int):
            return False, "Balance must be an integer"
        if balance < 0:
            return False, "Balance cannot be negative"
        return True, ""

    def to_dict(self):
        return {
            "name": self.name,
            "balance": self.balance
        }

    def __repr__(self):
        return f"User(name={self.name}, balance={self.balance})"
