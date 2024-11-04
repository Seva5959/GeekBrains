class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses should implement this method")

    def __str__(self):
        return f"{self.__class__.__name__} named {self.name}"

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def __str__(self):
        return f"{super().__str__()} of breed {self.breed}"

class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Meow!"

    def __str__(self):
        return f"{super().__str__()} with color {self.color}"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, *args) -> Animal:
        """
        Создает экземпляр животного на основе переданного типа и параметров.
        :param animal_type: Название типа животного (например, 'Dog' или 'Cat')
        :param args: Параметры для конструктора животного
        :return: Экземпляр соответствующего класса животного
        """
        animal_classes = {
            'Dog': Dog,
            'Cat': Cat
        }
        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Создаем экземпляры животных с использованием фабрики
dog = AnimalFactory.create_animal('Dog', 'Buddy', 'Golden Retriever')
cat = AnimalFactory.create_animal('Cat', 'Whiskers', 'Black')

print(dog)  # Вывод: Dog named Buddy of breed Golden Retriever
print(cat)  # Вывод: Cat named Whiskers with color Black
print(dog.speak())  # Вывод: Woof!
print(cat.speak())  # Вывод: Meow!