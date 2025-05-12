from ..entities.user import User

class UserRepositoryMock:
    user: User

    def __init__(self):
        # Você pode mudar "Usuário Exemplo" por outro nome
        self.user = User(name="Usuário Exemplo", balance=0)

    def get_user(self) -> User:
        return self.user

    def update_balance(self, new_balance: int) -> None:
        self.user.balance = new_balance
        #fazer diferenciação de withdraw e dep
    



