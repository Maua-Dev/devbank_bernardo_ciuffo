from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum


class ITransactionRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> Optional[List[Transaction]]:
        '''
        Returns all the transactions
        '''
        pass

    @abstractmethod
    def create_transaction(self, transaction_type: TransactionTypeEnum, transaction_value: float, transaction_time: float, curr_balance: float) -> Optional[Transaction]:
        '''
        Creates a new transaction, given its type, value, timestamp, and current balance
        '''
        pass
