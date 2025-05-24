from fastapi.exceptions import HTTPException
import pytest
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.user_repository_mock import UserRepositoryMock
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock
from src.app.main import get_user, get_transactions, post_deposit, post_withdraw


class Test_Main:


    def test_get_user(self):
        expected = {
            "name": 'Bernardo Ciuffo',
            "agency": "1111",
            "user": "11111-1",
            "current_balance": 1000.0
        }
        assert get_user() == expected
         
    def test_make_deposit(self):

        request = {
                "2": 0,
                "5": 2,
                "10": 0,
                "20": 0,
                "50": 0,
                "100": 0,
                "200": 2
        }

        response = post_deposit(request)

        expected = {
            "current_balance": 1410.0,
            "timestamp": response["timestamp"]
        }

        assert response == expected

    
    def test_make_withdraw(self):

        request = {
                "2": 0,
                "5": 0,
                "10": 0,
                "20": 5,
                "50": 0,
                "100": 1,
                "200": 0
        }

        response = post_withdraw(request)

        expected = {
            "current_balance": 1210.0,
            "timestamp": response["timestamp"]
        }

        assert response == expected

    
    def test_make_withdraw_with_invalid_value(self):

        request = {
                "2": 0,
                "5": 0,
                "10": 0,
                "20": 0,
                "50": 0,
                "100": 0,
                "200": 100
        }

        with pytest.raises(HTTPException):
            response = post_withdraw(request)

    @pytest.mark.skip(reason='Nao funciona corretamente se todos rodarem ao mesmo tempo')
    def test_get_history(self):

        deposit = {
                "2": 0,
                "5": 2,
                "10": 0,
                "20": 0,
                "50": 0,
                "100": 0,
                "200": 2
        }

        response_deposit = post_deposit(deposit)

        withdraw = {
                "2": 0,
                "5": 0,
                "10": 0,
                "20": 5,
                "50": 0,
                "100": 1,
                "200": 0
        }

        response_withdraw = post_withdraw(withdraw)

        transactions = get_transactions()

        expected = [
            {
            "type": TransactionTypeEnum.DEPOSIT.value,
            "value": 410.0,
            "current_balance": 1410.0,
            "timestamp": response_deposit["timestamp"]
            },
            {
            "type": TransactionTypeEnum.WITHDRAW.value,
            "value": 200.0,
            "current_balance": 1210.0,
            "timestamp": response_withdraw["timestamp"]
            }
        ]

        assert transactions == expected



    


        