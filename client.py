class User:
    def __init__(self, name, status):
        self.name = name
        self.status = status
        self.is_active = True

    def act(self, action):
        if action.lower() == 'q':
            self.is_active = False
        elif action == "help":
            return "Q/q - выход"


class Room:
    def __init__(self):
        from typing import List
        self.users: List[User] = []

    def __str__(self):
        if len(self.users) == 0:
            room_status = "В комнате пусто"
        else:
            room_status = "В комнате находятся:\n" +\
                ', '.join({user.name for user in self.users})
        return f"{'-' * 20}\n{room_status}"


def main():
    user = User(input("Введите своё имя?"),
                input("Как Ваше настроение?"))
    room = Room()
    while user.is_active:
        print(room)
        action = input("Введите Ваше действие (help - помощь): ")
        user.act(action)


if __name__ == "__main__":
    main()
