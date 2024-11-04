class Chat:
    def __init__(self, filename='chat.txt'):
        self.filename = filename

    def display_messages(self):
        """Отображает все сообщения из файла."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                messages = file.readlines()
                print("".join(messages))
        except FileNotFoundError:
            print("Служебное сообщение: пока что ничего нет\n")

    def add_message(self, name, message):
        """Добавляет новое сообщение в файл."""
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"{name}: {message}\n")

    def run(self):
        """Запускает основной цикл чата."""
        name = input("Как вас зовут? ")
        while True:
            print("Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2")
            response = input("Введите 1 или 2: ")
            if response == '1':
                self.display_messages()
            elif response == '2':
                new_message = input("Введите сообщение: ")
                self.add_message(name, new_message)
            else:
                print("Неизвестная команда\n")

# Запуск программы
if __name__ == "__main__":
    chat = Chat()
    chat.run()
