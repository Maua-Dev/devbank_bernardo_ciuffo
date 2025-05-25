import pytest
from datetime import datetime
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock

class Test_TransactionRepositoryMock:

    def setup_method(self):
        self.repo = TransactionRepositoryMock()

    def test_add_transaction(self):
        transaction = Transaction(value=100.0, curr_balance=100.0, transaction_type=TransactionTypeEnum.DEPOSIT, timestamp = datetime.now().timestamp())
        result = self.repo.transaction(transaction)
        assert result == transaction
        assert self.repo.transactions[1] == transaction

    def test_multiple_transactions(self):
        t1 = Transaction(value=20.0, curr_balance=20.0, transaction_type=TransactionTypeEnum.DEPOSIT, timestamp = datetime.now().timestamp())
        t2 = Transaction(value=10.0, curr_balance=10.0, transaction_type=TransactionTypeEnum.WITHDRAW, timestamp = datetime.now().timestamp())
        self.repo.transaction(t1)
        self.repo.transaction(t2)
        assert len(self.repo.transactions) == 2
        assert self.repo.transactions[1] == t1
        assert self.repo.transactions[2] == t2

    def test_get_history(self):
        t1 = Transaction(value=200.0, curr_balance=200.0, transaction_type=TransactionTypeEnum.DEPOSIT, timestamp = datetime.now().timestamp())
        t2 = Transaction(value=100.0, curr_balance=100.0, transaction_type=TransactionTypeEnum.WITHDRAW, timestamp = datetime.now().timestamp())
        self.repo.transaction(t1)
        self.repo.transaction(t2)
        history = self.repo.get_history()
        assert history == [t1, t2]
