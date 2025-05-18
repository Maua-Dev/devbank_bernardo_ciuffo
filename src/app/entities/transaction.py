from typing import Tuple
from datetime import datetime
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum  # DEPOSIT, WITHDRAW


class Transaction:
    value: float
    curr_balance: float
    transaction_type: TransactionTypeEnum
    timestamp: float  # usar float 

    def __init__(
        self,
        value: float = None,
        curr_balance: float = None,
        transaction_type: TransactionTypeEnum = None,
        timestamp: float = None
    ):
        validation_value = self.validate_value(value)
        if not validation_value[0]:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value

        validation_balance = self.validate_curr_balance(curr_balance)
        if not validation_balance[0]:
            raise ParamNotValidated("curr_balance", validation_balance[1])
        self.curr_balance = curr_balance

        validation_type = self.validate_transaction_type(transaction_type)
        if not validation_type[0]:
            raise ParamNotValidated("transaction_type", validation_type[1])
        self.transaction_type = transaction_type

        validation_timestamp = self.validate_timestamp(timestamp)
        if not validation_timestamp[0]:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp

    @staticmethod
    def validate_transaction_type(transaction_type: TransactionTypeEnum) -> Tuple[bool, str]:
        if transaction_type is None:
            return False, "Transaction type is required"
        if not isinstance(transaction_type, TransactionTypeEnum):
            return False, "Transaction type must be a valid TransactionTypeEnum"
        return True, ""

    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return False, "Transaction value is required"
        if not isinstance(value, float):
            return False, "Transaction value must be a float"
        if value < 0:
            return False, "Transaction value must be positive"
        return True, ""

    @staticmethod
    def validate_curr_balance(curr_balance: float) -> Tuple[bool, str]:
        if curr_balance is None:
            return False, "Current balance is required"
        if not isinstance(curr_balance, float):
            return False, "Current balance must be a float"
        if curr_balance < 0:
            return False, "Current balance cannot be negative"
        return True, ""

    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return False, "Timestamp is required"
        if not isinstance(timestamp, float):
            return False, "Timestamp must be a float"
        if timestamp < 0:
            return False, "Timestamp must be non-negative"
        return True, ""

    def to_dict(self):
        return {
            "type": self.transaction_type.value,
            "value": self.value,
            "current_balance": self.curr_balance,
            "timestamp": self.timestamp
        }

    def __eq__(self, other):
        return (
            self.transaction_type == other.transaction_type and
            self.value == other.value and
            self.curr_balance == other.curr_balance and
            self.timestamp == other.timestamp
        )

    def __repr__(self):
        return (
            f"Transaction(type={self.transaction_type}, value={self.value}, "
            f"curr_balance={self.curr_balance}, timestamp={self.timestamp})"
        )
