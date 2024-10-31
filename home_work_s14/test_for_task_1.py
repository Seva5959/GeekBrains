import pytest
from task_1 import BankAccount, InsufficientFundsError

@pytest.fixture
def bank_account():
    # Подготовка тестового состояния
    return BankAccount(100)  # Начальный баланс 100

def test_initial_balance(bank_account):
    # Проверка начального баланса
    assert bank_account.get_balance() == 100

def test_deposit(bank_account):
    # Проверка депозита
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150

def test_withdraw(bank_account):
    # Проверка снятия средств
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 70

def test_withdraw_insufficient_funds(bank_account):
    # Проверка снятия больше средств, чем доступно
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(200)

def test_deposit_negative_amount(bank_account):
    # Проверка депозита отрицательной суммы
    with pytest.raises(ValueError):
        bank_account.deposit(-10)
