# Практика использования декоратора @property

class User:
    def __init__(self, fio, age, passport, weight) -> None:
        self.valid_fio(fio)

        self.__fio = fio.split()
        self.age = age
        self.passport = passport
        self.weight = weight

    @staticmethod
    def valid_fio(fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой.")

        fio = fio.split()
        
        if len(fio) != 3:
            raise ValueError("Неверный формат ФИО.")

        for word in fio:
            for letter in word:
                if not letter.isalpha():
                    raise ValueError("ФИО дожно содержать только буквы.")

    @property
    def fio(self):
        return self.__fio

    @staticmethod
    def valid_age(age):
        if type(age) != int:
            raise TypeError("Возраст должен быть целым числом.")

        if age < 14 or age > 120:
            raise ValueError("Возраст должен быть в промежутке [14:120].")
        
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.valid_age(age)

        self.__age = age

    @staticmethod
    def valid_passport(passport):
        if type(passport) != str:
            raise TypeError("Номер паспорта должен быть в виде строки.")

        passport = passport.split()

        if len(passport) != 2 or len(passport[0]) != 4 or len(passport[1]) != 6:
            raise ValueError("Неверный формат паспорта.")
        
        for number in passport:
            for letter in number:
                if not letter.isdigit():
                    raise ValueError("Номер паспорта должен содержать только цифры.")

    @property
    def passport(self):
        return self.__passport
    
    @passport.setter
    def passport(self, value):
        self.valid_passport(value)

        self.__passport = value
    
    @staticmethod
    def valid_weight(weigth):
        if type(weigth) != float:
            raise TypeError("Вес должен быть вещественным числом.")


    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        self.valid_weight(value)

        self.__weight = value
    
user = User("Oleg Korkin Petrov", 14, "1234 213891", 80.0)

print(user.fio)
print(user.age)
print(user.passport)
print(user.weight)

user.age = 15

print(user.fio)
print(user.age)
print(user.passport)
print(user.weight)

user.age = 16

print(user.__dict__)