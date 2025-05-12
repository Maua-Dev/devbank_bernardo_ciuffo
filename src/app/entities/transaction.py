from typing import Tuple
from datetime import datetime
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum  # DEPOSIT, WITHDRAW


class Transaction:
    value: int
    transaction_type: TransactionTypeEnum
    timestamp: datetime

    def __init__(
        self,
        value: int = None,
        transaction_type: TransactionTypeEnum = None,
        timestamp: datetime = None
    ):
        validation_value = self.validate_value(value)
        if not validation_value[0]:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value

        validation_type = self.validate_transaction_type(transaction_type)
        if not validation_type[0]:
            raise ParamNotValidated("transaction_type", validation_type[1])
        self.transaction_type = transaction_type

        self.timestamp = timestamp if timestamp else datetime.utcnow()

    @staticmethod
    def validate_value(value: int) -> Tuple[bool, str]:
        if value is None:
            return False, "Transaction value is required"
        if type(value) != int:
            return False, "Transaction value must be an integer"
        if value <= 0:
            return False, "Transaction value must be greater than zero"
        return True, ""

    @staticmethod
    def validate_transaction_type(transaction_type: TransactionTypeEnum) -> Tuple[bool, str]:
        if transaction_type is None:
            return False, "Transaction type is required"
        if not isinstance(transaction_type, TransactionTypeEnum):
            return False, "Invalid transaction type"
        return True, ""

    def to_dict(self):
        return {
            "value": self.value,
            "transaction_type": self.transaction_type.value,
            "timestamp": self.timestamp.isoformat()
        }

    def __eq__(self, other):
        return (
            self.value == other.value and
            self.transaction_type == other.transaction_type and
            self.timestamp == other.timestamp
        )

    def __repr__(self):
        return (
            f"Transaction(value={self.value}, type={self.transaction_type}, time={self.timestamp})"
        )
