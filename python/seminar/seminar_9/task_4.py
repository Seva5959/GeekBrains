"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.

"""
import json
import os

def repeater(count : int):
    deco_res= []
    def inner(func):
        def wripper(*args,**kwargs):
            for i in range(count):
                deco_res.append(func(*args,**kwargs))
            return deco_res
        return wripper
    return inner
def read_json_file(file_name):
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def write_json_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def args_deco(func):
    def inner(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        res_dict = read_json_file(file_name)
        res_func = func(*args, **kwargs)
        key = f"call_{len(res_dict) + 1}"
        res_dict[key] = {
            "result": res_func,
            "args": [str(i) for i in args],
            "kwargs": kwargs
        }
        write_json_file(file_name, res_dict)
        return res_func
    return inner

@repeater(3)
def def_kj(*args, **kwargs):
    res = []
    for key, value in kwargs.items():
        print(key, value, sep=' => ')
    for i in args:
        if isinstance(i, int) or (isinstance(i, str) and i.isdigit()):
            res.append(int(i))
    for value in kwargs.values():
        if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
            res.append(int(value))
    return sum(res)

print(def_kj(2, 3, 5, "21", name="vasa", len="150", siti="Moskva"))
print(def_kj(0, 43, 43, "31", name="KOLa", len="190", siti="PERM"))