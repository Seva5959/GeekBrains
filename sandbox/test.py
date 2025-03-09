import time

# start_time = time.time()
#
# for i in range(1_000_000):
#     print(i)
# per_1 = float(f'{time.time() - start_time:.2f}')
#
# for i in range(1_000_000):
#     print(i)
# per_2 = float(f'{time.time() - start_time:.2f}')
#
# for i in range(1_000_000):
#     print(i)
# per_3 = float(f'{time.time() - start_time:.2f}')
#
# for i in range(1_000_000):
#     print(i)
# per_4 = float(f'{time.time() - start_time:.2f}')
#
# for i in range(1_000_000):
#     print(i)
# per_5 = float(f'{time.time() - start_time:.2f}')
#
# rez_first_var = (per_5 + per_4 + per_3 + per_2 + per_1) / 5

start_time = time.time()

for i in range(1_000_000):
    if i == 999_999:
        break
per_1 = float(f'{time.time() - start_time:.2f}')

for i in range(1_000_000):
    if i == 999_999:
        break
per_2 = float(f'{time.time() - start_time:.2f}')

for i in range(1_000_000):
    if i == 999_999:
        break
per_3 = float(f'{time.time() - start_time:.2f}')

for i in range(1_000_000):
    if i == 999_999:
        break
per_4 = float(f'{time.time() - start_time:.2f}')

for i in range(1_000_000):
    if i == 999_999:
        break
per_5 = float(f'{time.time() - start_time:.2f}')

rez_second_var = (per_5 + per_4 + per_3 + per_2 + per_1) / 5

with open('data.txt', mode='a', encoding='utf-8') as f:
    f.write(f'\nrez_first_var=\n{rez_second_var=}')




