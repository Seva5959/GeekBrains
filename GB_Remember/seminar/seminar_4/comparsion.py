import task_1
import task_2
import task_3

COUNT_ATTEMPT = 10


def cheak_time():
    asyn_time_rez = 0
    thr_time_rez = 0
    proc_time_rez = 0
    for _ in range(COUNT_ATTEMPT):
        time_tiken_asyn = task_3.psevdo_main()
        asyn_time_rez += time_tiken_asyn

        time_taken_thr = task_1.psevdo_main()
        thr_time_rez += time_taken_thr

        time_taken_proc = task_2.psevdo_main()
        proc_time_rez += time_taken_proc

    ahm_mean_asyn = round(asyn_time_rez / COUNT_ATTEMPT, 3)
    ahm_mean_thr = round(thr_time_rez / COUNT_ATTEMPT, 3)
    ahm_mean_proc = round(proc_time_rez / COUNT_ATTEMPT, 3)

    msg = (f'Всего было провидено опытов: {COUNT_ATTEMPT}\n'
           f'Среднее арифметическое многопоточного способа: {ahm_mean_thr}\n'
           f'Среднее арифметическое мультипроцессорного способа: {ahm_mean_proc}\n'
           f'Среднее арифметическое асинхронного способа: {ahm_mean_asyn}\n\n')

    with open('rezult_comparsion.txt', mode='a', encoding='utf-8') as f:
        f.write(msg)

    return msg


if __name__ == '__main__':
    print(cheak_time())
