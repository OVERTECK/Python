class User:
    # def __init__(self, name) -> None:
    #     self.name = name

    name = "Oleg"

user_1 = User()

user_1.name = "Ivan"

print(user_1.__dict__)

user_2 = User()

print(user_2.name)
print(user_2.__dict__)