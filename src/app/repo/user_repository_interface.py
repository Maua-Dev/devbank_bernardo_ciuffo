# src/repo/user_repository_interface.py
from abc import ABC, abstractmethod
from typing import Optional
from ..entities.user import User
from ..entities.transaction import Transaction


class IUserRepository(ABC):

    @abstractmethod
    def get_user(self) -> Optional[User]:
        '''
        Returns the current user
        '''
        pass

    @abstractmethod
    def update_balance(self, new_balance: float) -> None:
        '''
        Updates the user balance
        '''
        pass

    @abstractmethod
    def apply_transaction(self, transaction: Transaction) -> None:
        '''
        Applies a transaction to the user's balance
        '''
        pass
