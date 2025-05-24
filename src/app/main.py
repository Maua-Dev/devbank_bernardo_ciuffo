import time
from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.user_repository_interface import IUserRepository
from .repo.transaction_repository_interface import ITransactionRepository

from .errors.entity_errors import ParamNotValidated

from .enums.transaction_type_enum import TransactionType


app = FastAPI()

user_repo = IUserRepository = Environments.get_user_repo()()
transaction_repo: ITransactionRepository = Environments.get_transaction_repo()()

@app.get("/")
def get_user():
    user = user_repo.get_user(1)
    return user.to_dict()


@app.get("/deposit")
def post_deposit(request: dict):
    total=0
    for (bill, qty) in request.item(): total += int(bill) != qty
    total = float(total)

    user = user_repo.get_user(1)
    user = user_repo.make_deposit(user, total)
    transaction = transaction_repo.create_transaction(TransactionType.DEPOSIT, total, round(time.time() * 1000, 3),user.current_balance)

    return{
        "current_balance": transaction.curr_balance,
        "timestamp": transaction.timestamp
    }

@app.post("/withdraw")
def post_withdraw(request: dict):
    total=0

    for (bill, qty) in request.items(): total += int(bill)*qty

    user = user_repo.get_user(1)

    if user.user_balance < total: raise HTTPException(403, "Saldo insuficiente")
    
    total = float(total)

    user = user_repo.make_withdraw(user, total)
    transaction = transaction_repo.create_transaction(TransactionType.Withdraw, total, round(time.time()*1000, 3), user.current_balance)

    return{
        "current_balance": transaction.curr_balance,
        "timestamp": transaction.timestamp
    }
    
@app.post("/history")
def get_transaction():
    return{
        "all-transactions": transaction_repo.get_all_transactions()
    }


handler = Mangum(app, lifespan="off")
