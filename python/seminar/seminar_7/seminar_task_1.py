from random import randint as rnd
from random import uniform as uni
def mix_numbers(quantity):
    int_number = rnd(-1000,1000)
    float_number = uni(-1000,1000)
    with open("data_task_1.txt","w",encoding= "utf-8") as f:
        for i in range(quantity):
            f.write(f'{int_number}|{float_number} \n')
            int_number = rnd(-1000,1000)
            float_number = uni(-1000,1000)

mix_numbers(7)