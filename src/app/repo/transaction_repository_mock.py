from typing import Dict, List
from ..entities.transaction import Transaction


class TransactionRepositoryMock:
    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {}

    def transaction(self, transaction: Transaction) -> Transaction:
        transaction_id = len(self.transactions) + 1
        self.transactions[transaction_id] = transaction
        return transaction

    def get_history(self) -> List[Transaction]:
        return list(self.transactions.values())

#oi

