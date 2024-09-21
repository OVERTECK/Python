# Дескрипторы (data descriptor и not-data descriptor)

class Valid_String:
    @staticmethod
    def valid_string(value):
        if type(value) != str:
            raise TypeError("Значение должно быть строковым типом данных.")

    def valid_integer(value):
        if type(value) != int:
            raise TypeError("Значение должно быть целочисленным типом данных.")
        
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __set__(self, instance, value):
        self.valid_string(value)

        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class User:
    name = Valid_String()
    age = Valid_String()
    sex = Valid_String()
    mail = Valid_String()
    phone_number = Valid_String()
    

    def __init__(self, name, age, sex, mail, phone_number) -> None:
        self.name = name
        self.age = age
        self.sex = sex
        self.mail = mail
        self.phone_number = phone_number

user_1 = User("Alex", "20", "man", "alex20@gmail.com", "79123648573")

print(user_1.age)