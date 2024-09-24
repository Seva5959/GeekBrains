import os
import json
class Factorial:
    data = []
    def __init__(self,amount: int,file_name: str = 'json_result'):
        self.amount = amount
        self.file_name = file_name + ".json"
        self._in_factorial = None
    @staticmethod
    def _factorial(num):
        if num in (0,1):
            return 1
        fact = 1
        for row in range(2,num+1):
            fact *= row
        return fact

    def _write_json(self, json_data):
        dict_json = {}
        if os.path.exists(self.file_name): # проверяет существует ли файл
            with open(self.file_name,'r',encoding='utf-8')as file:
                dict_json = json.load(file)
        dict_json.update(json_data)
        with open(self.file_name,'w',encoding='utf-8')as file:
            json.dump(dict_json,file)
    def __call__(self, fact_number):
        self._in_factorial = Factorial._factorial(fact_number)
        Factorial.data.append(self._in_factorial)
        return self._in_factorial

    def __enter__(self):
        return  self

    def __exit__(self, exc_type, exc_val, exc_tb):
        fact_data = {str(self._in_factorial):self.show_last()}
        self._write_json(fact_data)
    def show_last(self):
        return Factorial.data[-self.amount:]


with Factorial(3) as fact:
    fact(3)
    fact(4)
    fact(5)
    fact(6)
    fact(7)
print(fact.show_last())

