import time

class Mystring(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls,value)
        instance.author = author
        instance.time = time.time()

        return instance

my_str = Mystring("Новый текст",'Oleg')
print(my_str)
print(my_str.author)
print(my_str.time)
print(my_str.split())
