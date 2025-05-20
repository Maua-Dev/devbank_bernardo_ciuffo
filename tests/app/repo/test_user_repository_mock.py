import pytest
from src.app.repo.user_repository_mock import UserRepositoryMock
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class Test_UserRepositoryMock:

    def test_initial_balance(self):
        repo = UserRepositoryMock()
        user = repo.get_user()
        assert user.balance == 0.0

    def test_apply_deposit_transaction(self):
        repo = UserRepositoryMock()
        t = Transaction(value=100.0, current_balance=0.0, transaction_type=TransactionTypeEnum.DEPOSIT)
        repo.apply_transaction(t)
        assert repo.get_user().balance == 100.0

    def test_apply_withdraw_transaction(self):
        repo = UserRepositoryMock()
        # Primeiro depositamos
        repo.apply_transaction(Transaction(value=200.0, current_balance=0.0, transaction_type=TransactionTypeEnum.DEPOSIT))
        # Agora sacamos
        t = Transaction(value=50.0, current_balance=200.0, transaction_type=TransactionTypeEnum.WITHDRAW)
        repo.apply_transaction(t)
        assert repo.get_user().balance == 150.0

    def test_withdraw_more_than_balance_raises_error(self):
        repo = UserRepositoryMock()
        with pytest.raises(ParamNotValidated):
            t = Transaction(value=100.0, current_balance=0.0, transaction_type=TransactionTypeEnum.WITHDRAW)
            repo.apply_transaction(t)
