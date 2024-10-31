import csv
from random import randrange
import os

CONSTANTA = 777
FILE_NAME = 'out_file.txt'


class RandomError(Exception):
    def __str__(self):
        return 'You"re out of luck'


def find_file(file_name=FILE_NAME):
    return True if file_name in os.listdir() else False

def start_csv(data, file_name=FILE_NAME):
    with open(file_name,'a',encoding='utf-8',newline='') as fl_csv:
        wr_csv = csv.writer(fl_csv)
        wr_csv.writerow([data])

def remove_file(file_name=FILE_NAME):
    if find_file():
        os.remove(file_name)
def vicious_cycle():
    count = 0
    remove_file()
    while True:
        try:
            user_num = int(input("Write please number: "))
            count += user_num
            start_csv(user_num)
        except ValueError:
            print('You stupid niga!')
            continue
        if count >= CONSTANTA:
            print("You can leave from vicious cycle!")
            break
        elif randrange(0, 14) == 1:  # probability of loss 1 == 13 %
            raise RandomError

vicious_cycle()