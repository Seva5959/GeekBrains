class NameError(Exception):
    def __init__(self):
        super().__init__("Имя должно состоять из хотя бы двух слов, каждое из которых начинается с заглавной буквы.")


class EmailError(Exception):
    def __init__(self):
        super().__init__("Электронная почта должна содержать символ '@' и точку '.' после '@'.")


class AgeError(Exception):
    def __init__(self):
        super().__init__("Возраст должен быть целым числом от 0 до 120.")


class User:
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.istitle() and len(value.split()) >= 2:
            self._name = value
        else:
            raise NameError()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise AgeError
        if 0 < value < 120:
            self._age = value
        else:
            raise AgeError()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        flag = 0
        for i, j in enumerate(value, start=0):
            if j == '@':
                flag += 1
            if flag == 1 and j == '.':
                flag += 1
        if flag == 2:
            self._email = value
        else:
            raise EmailError()


try:
    user = User(name="John Doe", email="john.doe@example.com", age=25)
    print(f"User created: {user.name}, {user.email}, {user.age}")
except (NameError, EmailError, AgeError) as e:
    print(e)
