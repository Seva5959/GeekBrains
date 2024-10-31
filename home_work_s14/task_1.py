class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__("Недостаточно средств на счете.")

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError()
        self.balance -= amount

    def get_balance(self):
        return self.balance
