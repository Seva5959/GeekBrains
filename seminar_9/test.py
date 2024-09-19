from random import randrange
random_info = list(randrange(0,10) for i in range(0,3))

print(*random_info)