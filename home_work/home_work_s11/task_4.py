class Stack:
    def __init__(self):
        # Инициализация стека как пустого списка
        self.__stack = list()

    def pop(self):
        # Извлечение элемента из стека, если он не пуст
        if self.is_empty():
            return None
        return self.__stack.pop()

    def push(self, item):
        # Добавление элемента в стек
        self.__stack.append(item)

    def is_empty(self):
        # Проверка, пуст ли стек
        return len(self.__stack) == 0

    def top(self):
        # Получение верхнего элемента стека без удаления
        if self.is_empty():
            return None
        return self.__stack[-1]


class TaskManager:
    def __init__(self):
        # Инициализация словаря для хранения стека задач по приоритетам
        self.tasks = dict()

    def new_task(self, text, priority):
        # Добавление новой задачи в стек с заданным приоритетом
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        # Добавляем задачу в стек для данного приоритета
        self.tasks[priority].push(text)

    def remove_task(self, text):
        # Удаление задачи по тексту из всех стеков
        for stack in self.tasks.values():
            # Используем временный стек для хранения задач, которые не нужно удалять
            temp_stack = Stack()
            while not stack.is_empty():
                task = stack.pop()
                if task != text:
                    temp_stack.push(task)
            # Перемещаем оставшиеся задачи обратно в основной стек
            while not temp_stack.is_empty():
                stack.push(temp_stack.pop())

    def __str__(self):
        # Отображение задач, отсортированных по приоритету
        sorted_keys = sorted(self.tasks.keys())
        out = []
        for key in sorted_keys:
            task_line = [str(key)]  # Начинаем строку с приоритета
            temp_stack = Stack()
            while not self.tasks[key].is_empty():
                task = self.tasks[key].pop()
                temp_stack.push(task)
            while not temp_stack.is_empty():
                task_line.append(temp_stack.pop())
            # Добавляем задачи на текущей строке
            out.append(' '.join(task_line))
        return '\n'.join(out)


def main():
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    # Печать списка задач
    print(manager)
    # Удаление задачи и повторный вывод
    manager.remove_task("поесть")
    print("\nПосле удаления задачи:")
    print(manager)


main()
