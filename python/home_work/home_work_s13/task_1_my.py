from random import randrange
from exceptions_for_1_task import *
import csv

CARMA = 500
PATH = 'excep.csv'
data_debaff = {1: KillError, 2: DrunkError, 3: CarCrashError, 4: GluttonyError, 5: DepressionError}


def one_day():
    rnd_carma = randrange(1, 8)
    rnd_number = randrange(1, 10)
    if rnd_number == 1:  # probability of loss 1 = 10%
        return rnd_carma, randrange(1, len(data_debaff))
    return [rnd_carma]


def load_from_csv(data, path=PATH):
    with open(path, 'a', encoding='utf-8', newline='') as fl_csv:
        wr_csv = csv.writer(fl_csv)
        wr_csv.writerow([data])


count = 0
current_day = 0
while CARMA > count:
    result_funck = one_day()
    carma = result_funck[0]
    error = result_funck[1] if len(result_funck) == 2 else None
    count += carma
    current_day += 1
    if error:
        try:
            raise data_debaff[error]
        except data_debaff[error] as e:
            load_from_csv(e)