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
        self.email = email
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (len(value.split()) >= 2 and all(word[0].isupper() for word in value.split())):
            raise NameError()
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value or '.' not in value.split('@')[1]:
            raise EmailError()
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (isinstance(value, int) and 0 <= value <= 120):
            raise AgeError()
        self._age = value

# Пример использования:
try:
    user = User(name="John Doe", email="john.doe@example.", age=25)
    print(f"User created: {user.name}, {user.email}, {user.age}")
except (NameError, EmailError, AgeError) as e:
    print(e)
