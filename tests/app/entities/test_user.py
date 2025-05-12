import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated


class Test_User:
    def test_create_valid_user(self):
        user = User(name="XXXXX", balance=100)
        assert user.name == "XXXXX"
        assert user.balance == 100

    def test_user_to_dict(self):
        user = User(name="XXXXX", balance=200)
        assert user.to_dict() == {"name": "XXXXX", "balance": 200}

    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name=None, balance=100)

    def test_user_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name=123, balance=100)

    def test_user_name_too_short(self):
        with pytest.raises(ParamNotValidated):
            User(name="A", balance=100)

    def test_user_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="XXXXX", balance=None)

    def test_user_balance_is_not_int(self):
        with pytest.raises(ParamNotValidated):
            User(name="XXXXX", balance="cem")

    def test_user_balance_negative(self):
        with pytest.raises(ParamNotValidated):
            User(name="XXXXX", balance=-50)
