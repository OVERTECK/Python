# Паттерн моносостояние

class User:
    __shared_attrs = {
        "name": "Alex",
        "age": 20
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_attrs

user_1 = User()
user_2 = User()

user_1.att = 1
user_1.att123 = "ку"
user_2.att = 1

print(user_1.__dict__)
print(user_2.__dict__)


