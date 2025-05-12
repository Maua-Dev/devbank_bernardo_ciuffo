import pytest
from src.app.repositories.user_repository_mock import UserRepositoryMock

class Test_UserRepositoryMock:

    def test_initial_balance(self):
        repo = UserRepositoryMock()
        user = repo.get_user()
        assert user.balance == 0

    def test_update_balance_deposit(self):
        repo = UserRepositoryMock()
        repo.update_balance(100)
        assert repo.get_user().balance == 100

    def test_update_balance_withdraw(self):
        repo = UserRepositoryMock()
        repo.update_balance(100)
        repo.update_balance(-50)
        assert repo.get_user().balance == 50

