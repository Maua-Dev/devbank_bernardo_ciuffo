import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated


class Test_User:

    def test_create_valid_user(self):
        user = User(name="XXXXX", agency="1234", account="12345-6", balance=100.0)
        assert user.name == "XXXXX"
        assert user.agency == "1234"
        assert user.account == "12345-6"
        assert user.balance == 100.0

    def test_user_to_dict(self):
        user = User(name="XXXXX", agency="1234", account="12345-6", balance=200.0)
        assert user.to_dict() == {
            "name": "XXXXX",
            "agency": "1234",
            "account": "12345-6",
            "balance": 200.0
        }

    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name=None, agency="1234", account="12345-6", balance=100.0)

    def test_user_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name=123, agency="1234", account="12345-6", balance=100.0)

    def test_user_name_too_short(self):
        with pytest.raises(ParamNotValidated):
            User(name="A", agency="1234", account="12345-6", balance=100.0)

    def test_user_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="XXXXX", agency="1234", account="12345-6", balance=None)

    def test_user_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            User(name="XXXXX", agency="1234", account="12345-6", balance="cem")

    def test_user_balance_negative(self):
        with pytest.raises(ParamNotValidated):
            User(name="XXXXX", agency="1234", account="12345-6", balance=-50.0)

    def test_invalid_agency_format(self):
        with pytest.raises(ParamNotValidated):
            User(name="XXXXX", agency="12", account="12345-6", balance=0.0)

    def test_invalid_account_format(self):
        with pytest.raises(ParamNotValidated):
            User(name="XXXXX", agency="1234", account="123456", balance=0.0)
