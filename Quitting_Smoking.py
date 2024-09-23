import matplotlib.pyplot as plt
import numpy as np

# Ваши данные
data_prog = {
    '14.08': 16, '15.08': 15, '16.08': 16, '17.08': 15, '18.08': 15, '19.08': 15, '20.08': 15, '21.08': 12, '22.08': 17,
    '23.08': 16, '24.08': 15, '25.08': 17, '26.08': 15, '27.08': 15, '28.08': 13, '29.08': 12, '30.08': 12, '31.08': 11,
    '01.09': 12, '02.09': 12, '03.09': 13, '04.09': 11, '05.09': 10, '06.09': 10, '07.09': 8, '08.09': 10, '09.09': 10,
    '10.09': 9, '11.09': 11, '12.09': 10, '13.09': 8, '14.09': 8, '15.09': 7, '16.09': 7, '17.09': 6,
    '18.09': 8, '19.09': 5, '20.09': 4, '21.09': 4, '22.09':4,'23.09':2,'24.09':1,'25.09':0
}

# Преобразование словаря в списки для оси X и Y
days = list(data_prog.keys())
cigarettes = list(data_prog.values())

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(days, cigarettes, marker='o', linestyle='-', color='b', label='Cigarettes per day')

# Установка частых меток на оси Y, начиная с 0
plt.yticks(np.arange(0, max(cigarettes) + 1, 1))

# Установка лимитов по оси Y, чтобы она начиналась с 0
plt.ylim(0, max(cigarettes) + 1)

# Настройки графика
plt.xlabel('Day')
plt.ylabel('Number of cigarettes')
plt.title('Progress in Quitting Smoking')

# Сетка для обеих осей
plt.grid(True, which='both', axis='both')

plt.xticks(rotation=45)  # Поворот меток на оси X для удобства
plt.legend()

# Отображение графика
plt.tight_layout()  # Для корректного отображения всех элементов
plt.show()
