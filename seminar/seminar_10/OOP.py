'''
import  math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, other_point):
        return round(math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2), 2)


class RedButton:
    def __init__(self):
        self.clicking = 0
    def click(self):
        self.clicking += 1
        print("Тревога!")


    def count(self):
        return self.clicking
first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())

# Задача о праграмmистах
class Programmer:
    def __init__(self,name,current_position):
        self.name = name
        self.current_position = current_position
        self.salary = 0
        self.allowance = 0
        self.time = 0


    def work(self,time):
        self.time += time
        if self.current_position == "Junior":
            self.salary += time * 10
        elif self.current_position == "Middle":
            self.salary += time * 15
        else:
            self.salary += time * (20 + self.allowance)
        return self.salary


    def rise(self):
        if self.current_position == "Junior":
            self.current_position = "Middle"
            return self.current_position
        elif self.current_position == "Middle":
            self.current_position = "Senior"
            return self.current_position
        else:
            self.allowance +=1
            return self.allowance

    def info(self):
        return f'{self.name} {self.time} ч. {self.salary} тгр.'


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

Реализуйте класс Queue, который не имеет параметров инициализации, но поддерживает методы:
push(item) — добавить элемент в конец очереди;
pop() — «вытащить» первый элемент из очереди;
is_empty() — проверят очередь на пустоту
'''


class Stack:
    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def is_empty(self):
        return len(self.data) == 0

    def pop(self):
        if not self.is_empty():
            return self.data.pop()


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")
























