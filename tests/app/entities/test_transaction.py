import pytest
import time
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.entities.transaction import Transaction
from src.app.errors.entity_errors import ParamNotValidated


class Test_Transaction:

    def test_transaction_valid(self):
        transaction = Transaction(value=100.0, curr_balance=100.0, transaction_type=TransactionTypeEnum.DEPOSIT, timestamp=time.time())
        assert transaction.value == 100.0
        assert transaction.transaction_type == TransactionTypeEnum.DEPOSIT
        assert transaction.curr_balance == 100.0
        assert isinstance(transaction.timestamp, float)

    def test_transaction_to_dict(self):
        transaction = Transaction(value=200.0, curr_balance=300.0, transaction_type=TransactionTypeEnum.WITHDRAW, timestamp=time.time())
        result = transaction.to_dict()
        assert result["value"] == 200.0
        assert result["curr_balance"] == 300.0
        assert result["transaction_type"] == "WITHDRAW"
        assert isinstance(result["timestamp"], str)

    def test_transaction_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=None, curr_balance=0.0, transaction_type=TransactionTypeEnum.DEPOSIT)

    def test_transaction_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value="100", curr_balance=0.0, transaction_type=TransactionTypeEnum.DEPOSIT)

    def test_transaction_value_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=-10.0, curr_balance=0.0, transaction_type=TransactionTypeEnum.WITHDRAW)

    def test_transaction_value_is_zero(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=0.0, curr_balance=0.0, transaction_type=TransactionTypeEnum.DEPOSIT)

    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=100.0, curr_balance=0.0, transaction_type=None)

    def test_transaction_type_invalid_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=100.0, curr_balance=0.0, transaction_type="DEPOSIT")

    def test_transaction_repr(self):
        transaction = Transaction(value=200.0, curr_balance=500.0, transaction_type=TransactionTypeEnum.DEPOSIT, timestamp=time.time())
        repr_str = repr(transaction)
        assert "Transaction(value=200.0" in repr_str
        assert "type=TransactionTypeEnum.DEPOSIT" in repr_str
