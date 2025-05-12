import pytest
from datetime import datetime
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated


class Test_Transaction:

    def test_transaction_valid(self):
        transaction = Transaction(value=100, transaction_type=TransactionTypeEnum.DEPOSIT)
        assert transaction.value == 100
        assert transaction.transaction_type == TransactionTypeEnum.DEPOSIT
        assert isinstance(transaction.timestamp, datetime)

    def test_transaction_to_dict(self):
        transaction = Transaction(value=200, transaction_type=TransactionTypeEnum.WITHDRAW)
        result = transaction.to_dict()
        assert result["value"] == 200
        assert result["transaction_type"] == "WITHDRAW"
        assert isinstance(result["timestamp"], str)

    def test_transaction_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=None, transaction_type=TransactionTypeEnum.DEPOSIT)

    def test_transaction_value_is_not_int(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value="100", transaction_type=TransactionTypeEnum.DEPOSIT)

    def test_transaction_value_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=-10, transaction_type=TransactionTypeEnum.WITHDRAW)

    def test_transaction_value_is_zero(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=0, transaction_type=TransactionTypeEnum.DEPOSIT)

    def test_transaction_value_not_multiple_of_note(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=3, transaction_type=TransactionTypeEnum.DEPOSIT)

    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=100, transaction_type=None)

    def test_transaction_type_invalid_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=100, transaction_type="DEPOSIT")

    def test_transaction_repr(self):
        transaction = Transaction(value=200, transaction_type=TransactionTypeEnum.DEPOSIT)
        repr_str = repr(transaction)
        assert "Transaction(value=200" in repr_str
        assert "type=TransactionTypeEnum.DEPOSIT" in repr_str
