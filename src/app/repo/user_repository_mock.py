from ..entities.user import User
from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated


class UserRepositoryMock:
    user: User

    def __init__(self):
        self.user = User(name="Usuário Exemplo", balance=0)

    def get_user(self) -> User:
        return self.user

    def update_balance(self, new_balance: int) -> None:
        self.user.balance = new_balance

    def apply_transaction(self, transaction: Transaction) -> None:
        if transaction.transaction_type == TransactionTypeEnum.DEPOSIT:
            self.user.balance += transaction.value
        elif transaction.transaction_type == TransactionTypeEnum.WITHDRAW:
            if transaction.value > self.user.balance:
                raise ParamNotValidated("value", "Insufficient balance for withdrawal")
            self.user.balance -= transaction.value
        else:
            raise ParamNotValidated("transaction_type", "Unsupported transaction type")




