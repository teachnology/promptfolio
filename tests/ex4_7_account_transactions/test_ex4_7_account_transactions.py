import sys
import os
import numbers
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import Account
except ImportError:
    class Account:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("Class Account is not defined")


def test_account_transactions_and_values():
    account = Account("Marijan", "321321321", initial_amount=1000)
    assert account.name == "Marijan"
    assert account.number == "321321321"
    assert account.balance == 1000
    assert account.transactions == 0

    for _ in range(10):
        account.deposit(10)
    assert np.isclose(account.balance, 1100)
    assert account.transactions == 10

    for _ in range(10):
        account.withdraw(5)
    assert np.isclose(account.balance, 1050)
    assert account.transactions == 20


def test_account_types_and_methods():
    account = Account("Alice", "000", initial_amount=0)
    assert isinstance(account, Account)
    assert isinstance(account.name, str)
    assert isinstance(account.number, str)
    assert isinstance(account.balance, numbers.Real)
    assert isinstance(account.transactions, numbers.Real)
    assert account.deposit(2) is None
    assert account.withdraw(2) is None
    assert account.dump() is None
    assert callable(account.deposit)
    assert callable(account.withdraw)
    assert callable(account.dump)


