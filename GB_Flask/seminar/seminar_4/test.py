import time

few = 1_000_000
midle = 10_000_000
large = 1_000_000_000
def time_decor(func):
    def wrapper(*args, **kwargs):
        start_t = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        return f'Result: {result}. It took {finish-start_t:.2f} seconds'
    return wrapper

@time_decor
def count_add(num):
    ct = 0
    while ct < num:
        ct += 1
    return ct

print(count_add(midle))

