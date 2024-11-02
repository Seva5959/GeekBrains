from random import randint  as rnd
def random_data(min_bit,max_bit):
    data = ""
    numbers = [str(i) for i in range(10)]
    for i in range(rnd(min_bit,max_bit)):
        data += numbers[rnd(0, 9)]
    return data
def random_name(min_len,max_len):
    alpfabet = []
    name = ""
    for i in range(ord("a"), ord("z") + 1):
        alpfabet.append(chr(i))
    for i in range(rnd(min_len,max_len)):
        name += alpfabet[rnd(0,25)]
    numbers = [str(i) for i in range(10)]
    return name+"TEST.txt"


def crate_file(min_len,max_len,min_bit,max_bit,quantity_file):
    for i in range(quantity_file):
        with open(random_name(min_len,max_len),"w", encoding="utf-8") as f:
            f.write(random_data(min_bit,max_bit))

crate_file(10,20,30,600,5)