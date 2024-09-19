def count(value):
    def decorater(funck):
        count = 0
        def wrapper(*args):
            nonlocal count
            res = funck(args[0],args[1],args[2])
            count += 1
            if count > value:
                return f"Вы исчерапли попытки использовать функцию : {funck.__name__} "
            return f'Площадь треугольника {res}.Попытка номер {count}, осталось {value - count}'
        return wrapper
    return decorater
@count(1)
def simple_funck(a,b,c):
    p = (a + b + c)/2
    square = (p-a)*(p-b)
    return square

c_1 = simple_funck(1,2,3)
c_2 = simple_funck(3,43,2)
c_3= simple_funck(322,4,23)
print(c_1)
print(c_2)
print(c_3)