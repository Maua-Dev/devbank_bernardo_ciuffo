from typing import Dict, List, Optional
from ..entities.transaction import Transaction
from ..repo.transaction_repository_interface import ITransactionRepository
from ..enums.transaction_type_enum import TransactionTypeEnum


class TransactionRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transaction]
    transactions_counter: int

    def __init__(self):
        self.transactions = {}
        self.transactions_counter = 0

    def get_all_transactions(self) -> Optional[List[Transaction]]:
        return list(self.transactions.values())

    def create_transaction(
        self,
        transaction_type: TransactionTypeEnum,
        transaction_value: float,
        transaction_time: float,
        curr_balance: float
    ) -> Optional[Transaction]:
        self.transactions_counter += 1
        transaction = Transaction(
            transaction_type=transaction_type,
            value=transaction_value,
            timestamp=transaction_time,
            current_balance=curr_balance
        )
        self.transactions[self.transactions_counter] = transaction
        return transaction
