from typing import Tuple
from ..errors.entity_errors import ParamNotValidated


class User:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str=None, agency: str=None, account: str=None, current_balance: float=None):
        validation_name = self.validate_name(name)
        if not validation_name[0]:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency)
        if not validation_agency[0]:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account)
        if not validation_account[0]:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_balance = self.validate_balance(current_balance)
        if not validation_balance[0]:
            raise ParamNotValidated("current_balance", validation_balance[1])
        self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return False, "Name is required"
        if not isinstance(name, str):
            return False, "Name must be a string"
        if len(name.strip()) < 2:
            return False, "Name must be at least 2 characters long"
        return True, ""

    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return False, "Agency is required"
        if not isinstance(agency, str):
            return False, "Agency must be a string"
        if not agency.isdigit() or len(agency) != 4:
            return False, "Agency must be exactly 4 digits"
        return True, ""

    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return False, "Account is required"
        if not isinstance(account, str):
            return False, "Account must be a string"
        if len(account) != 7 or account[5] != '-' or not (account[:5] + account[6]).isdigit():
            return False, "Account must follow the format XXXXX-X"
        return True, ""

    @staticmethod
    def validate_balance(balance: float) -> Tuple[bool, str]:
        if balance is None:
            return False, "Balance is required"
        if not isinstance(balance, float):
            return False, "Balance must be a float"
        if balance < 0:
            return False, "Balance cannot be negative"
        return True, ""

    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }

    def __repr__(self):
        return (
            f"User(name={self.name}, agency={self.agency}, "
            f"account={self.account}, current_balance={self.current_balance})"
        )