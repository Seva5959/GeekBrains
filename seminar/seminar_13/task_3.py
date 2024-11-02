class MyExeptions(Exception):
    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

class LevelError(MyExeptions):
    def __init__(self, user_id = None):
        self.user_id = user_id
        if user_id is None:
            message = f'Ошибка доступа! Пользователь не авторизирован!'
        else:
            message = f'Пользователя с ID {user_id} не существует!'
            super().__init__(message)

class IdError(MyExeptions):
    def __init__(self, user_id):
        super().__init__(f'ID ({user_id}) уже занят!')

class AccessError(MyExeptions):
    pass
