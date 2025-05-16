from typing import Tuple
from datetime import datetime
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum  # DEPOSIT, WITHDRAWW


class Transaction:
    value: float
    current_balance: float
    transaction_type: TransactionTypeEnum
    timestamp: datetime

    def __init__(
        self,
        value: float = None,
        current_balance: float = None,
        transaction_type: TransactionTypeEnum = None,
        timestamp: datetime = None
    ):
        validation_value = self.validate_value(value)
        if not validation_value[0]:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value

        validation_balance = self.validate_current_balance(current_balance)
        if not validation_balance[0]:
            raise ParamNotValidated("current_balance", validation_balance[1])
        self.current_balance = current_balance

        validation_type = self.validate_transaction_type(transaction_type)
        if not validation_type[0]:
            raise
