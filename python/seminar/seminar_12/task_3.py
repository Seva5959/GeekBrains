class Generator:
    def __init__(self, *args):
        self.start, self.step = 1, 1
        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start, self.stop = args[0], args[1]
        else:
            self.start, self.stop, self.step = args
        self.range = [*range(self.start, self.stop + 1, self.step)]

    @staticmethod
    def _factorial(num):
        if num in (0, 1):
            return 1
        fact = 1
        for row in range(2, num + 1):
            fact *= row
        return fact

    def __iter__(self):
        return self

    def __next__(self):
        while self.range:
            return self._factorial(self.range.pop(0))
        raise StopIteration()


gen_fact = Generator(2,10,1)
for i in gen_fact:
    print(i)
