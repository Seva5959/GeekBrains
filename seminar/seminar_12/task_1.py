class Factorial:
    data = []
    def __init__(self,amount: int):
        self.amount = amount

    @staticmethod
    def _factorial(num):
        if num in (0,1):
            return 1
        fact = 1
        for row in range(2,num+1):
            fact *= row
        return fact

    def __call__(self, fact_number):
        current_num = Factorial._factorial(fact_number)
        Factorial.data.append(current_num)
        return current_num
    def show_last(self):
        return Factorial.data[-self.amount:]


a = Factorial(2)
print(a(5))
print(a(5))
print(a(5))
print(a(5))

print(a.show_last())