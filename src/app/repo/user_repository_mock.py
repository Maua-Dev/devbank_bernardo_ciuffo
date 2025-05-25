# src/repo/user_repository_mock.py
from ..entities.user import User
from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated
from ..repo.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    user: User

    def __init__(self):
        self.user = User(
            name="Usuário Exemplo",
            agency="1234",
            account="12345-6",
            curr_balance=0.0
        )

    def get_user(self) -> User:
        return self.user

    def update_balance(self, new_balance: float) -> None:
        self.user.curr_balance = new_balance

    def apply_transaction(self, transaction: Transaction) -> None:
        if transaction.transaction_type == TransactionTypeEnum.DEPOSIT:
            self.user.curr_balance += transaction.value
        elif transaction.transaction_type == TransactionTypeEnum.WITHDRAW:
            if transaction.value > self.user.curr_balance:
                raise ParamNotValidated("value", "Insufficient balance for withdrawal")
            self.user.curr_balance -= transaction.value
        else:
            raise ParamNotValidated("transaction_type", "Unsupported transaction type")
