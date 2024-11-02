from string import ascii_letters


def sumbol_deleter(data: str):
    return ''.join([i for i in data if i in ascii_letters])

print(sumbol_deleter('kdsjfмсвыаолмылjbvs'))