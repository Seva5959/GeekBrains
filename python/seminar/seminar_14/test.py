from string import ascii_letters

data = 'dskfjds'
dsm = []
for i in data:
    if i in data:
        dsm.append(i)

print(''.join(dsm))