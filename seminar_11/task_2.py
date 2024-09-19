class NumArchiva:
    archive = None

    def __new__(cls, number: int, string: str):
        instance = super().__new__(cls)
        instance.string = string
        instance.number = number
        instance.archive = NumArchiva.archive.copy()  # зачем мы сделали эту строку ?
        NumArchiva.archive.append(instance)  # что добавляет этот код в архив
        return instance
