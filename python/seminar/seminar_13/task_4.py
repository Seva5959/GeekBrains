import json


class User:
    def __init__(self, name, user_id, user_lvl):
        self.name = name
        self.user_id = user_id
        self.user_lvl = user_lvl

    def __repr__(self):
        return f'{self.name} ({self.user_id}, {self.user_lvl})'



def load_user(path: str) -> set[User]:
    result = set()
    with open(path, 'r', encoding='utf-8') as f_js:
        for level, user in json.load(f_js).items():
            for user_id, name in user.items():
                result.add(User(name, user_id, level))
    return result

a =load_user('file.json')
print(a)
