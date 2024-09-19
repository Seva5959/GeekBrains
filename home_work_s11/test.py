class Calculator:
    def __init__(self, expression):
        self.expression = expression

    # Метод для вычисления выражения с использованием eval
    def calculate(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Ошибка вычисления: {e}"

# Пример использования класса
calc = Calculator("2 + 3 * 4 - 5")
print(f"Выражение: {calc.expression}")
print(f"Результат: {calc.calculate()}")
