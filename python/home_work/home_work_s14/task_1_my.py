class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__('Error Error Error Error Error')


class BankAccount:
    def __init__(self, wallet=0):
        self.__wallet = wallet

    def deposit(self, money):
        self.__wallet += money

    def withdraw(self, money):
        if self.__wallet > money:
            self.__wallet -= money
        else:
            raise InsufficientFundsError

    def get_balance(self):
        return self.__wallet
