from task_1_my import BankAccount, InsufficientFundsError
import pytest


def test_initial_balance():
    account = BankAccount(100)
    assert account.get_balance()

def test_cheak_depos():
    account = BankAccount(100)
    account.deposit(32)
    assert account.get_balance() == 132

def test_cheak_draw():
    account = BankAccount(100)
    account.withdraw(-1000)
    assert account.get_balance() == 1100
def test_cheak_withdraw():
    account = BankAccount(100)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(1000)

def test_cheak_wallet():
    account = BankAccount()
    assert account.get_balance() == 0



