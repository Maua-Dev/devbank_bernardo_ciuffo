import pytest
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repositories.transaction_repository_mock import TransactionRepositoryMock
from src.app.errors.entity_errors import ParamNotValidated


class Test_TransactionRepositoryMock:

    def setup_method(self):
        self.repo = TransactionRepositoryMock()

    def test_deposit_transaction(self):
        transaction = Transaction(value=100, transaction_type=TransactionTypeEnum.DEPOSIT)
        result = self.repo.deposit(transaction)
        assert result == transaction
        assert self.repo.transactions[1] == transaction

    def test_withdraw_transaction(self):
        transaction = Transaction(value=50, transaction_type=TransactionTypeEnum.WITHDRAW)
        result = self.repo.withdraw(transaction)
        assert result == transaction
        assert self.repo.transactions[1] == transaction

    def test_multiple_transactions(self):
        t1 = Transaction(value=20, transaction_type=TransactionTypeEnum.DEPOSIT)
        t2 = Transaction(value=10, transaction_type=TransactionTypeEnum.WITHDRAW)
        self.repo.deposit(t1)
        self.repo.withdraw(t2)
        assert len(self.repo.transactions) == 2
        assert self.repo.transactions[1] == t1
        assert self.repo.transactions[2] == t2

    def test_get_history(self):
        t1 = Transaction(value=200, transaction_type=TransactionTypeEnum.DEPOSIT)
        t2 = Transaction(value=100, transaction_type=TransactionTypeEnum.WITHDRAW)
        self.repo.deposit(t1)
        self.repo.withdraw(t2)
        history = self.repo.get_history()
        assert history == [t1, t2]
