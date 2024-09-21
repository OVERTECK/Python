# Урок про атрибуты класса и еги объектов.

class User:
    "User class"

    name = "Oleg"
    age = 20

a = User()

print(getattr(a, "age"))

print(hasattr(User, "121"))

print(delattr(User, "age"))

print(User.__dict__)

setattr(a, "sex", "man")

print(a.sex)