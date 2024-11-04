import json
from task_3 import *


class User:
    def __init__(self, name, user_id, user_lvl):
        self.name = name
        self.id = user_id
        self.level = user_lvl

    def __repr__(self):
        return f'{self.name} ({self.id}, {self.level})'

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name and self.id == other.id
        raise TypeError

    def __hash__(self):
        return hash(self.name + self.id + self.level)


class Company:
    def __init__(self, name, user_db_path):
        self.name = name
        self.path = user_db_path
        self.authorized_user = None

    def _loaf_json(self):
        result = set()
        with open(self.path, 'r', encoding='utf-8') as fl_js:
            for level, user in json.load(fl_js).items():
                for user_id, name in user.items():
                    result.add(User(name, user_id, level))
        return result

    def _save_json(self, new_user):
        user_set = self.users
        user_set.add(new_user)
        dict_to_write = {}
        for user in user_set:
            if user in dict_to_write:
                dict_to_write[user.level][user.id] = user.name
            else:
                dict_to_write[user.level] = {user.id: user.name}
        with open(self.path, 'w', encoding='utf-8')as fl_js:
            json.dump(dict_to_write,fl_js, indent=4, ensure_ascii=False)

    @property
    def users(self) -> set[User]:
        return self._loaf_json()

    @users.setter
    def users(self, new_users: User):
        self._save_json(new_users)

    def login(self, user_name, user_id):
        login_user = User(user_name, user_id, 0)
        for user in self.users:
            if user == login_user:
                self.autorized = user
                print(f'Привет, {user.name}! Твой уровень доступа {user.level}!')
                return user.level
        raise AccessError

    def logout(self):
        print(f'Goodbye {self.autorized.name} !')
        self.autorized = None

    def _check_id(self, user_id):
        for user in self.users:
            if user_id == user_id:
                return True
        return False

    def add_user(self, user_name, user_id, user_lvl):
        if not self.authorized_user:
            raise AccessError
        if int(self.authorized_user.level) <= int(user_lvl):
            raise LevelError(self.authorized_user.level)
        if self._check_id(user_id):
            raise IdError(user_id)
        new_user = User(user_name, user_id, user_lvl)
        self.users = new_user
        print(f'Пользователь "{new_user.name}" успешно создан')


a = Company('Nike', 'file.json')
print(a.login('Рус', '30'))
print(a.autorized)
print(a.logout())
