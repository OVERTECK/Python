# Декоратор - @property.

from typing import Any


class Mortar:
    MAX_RANGE = 1200

    def __init__(self) -> None:
        self.__count_cartridge = {
            "shrapnel": 3,
            "smok": 3
        }

        self.__types_cartridge = ["shrapnel", "smok"]

        self.__current_type_cartridge = "shrapnel"

    @property
    def count_cartridge(self):
        return self.__count_cartridge

    @count_cartridge.setter
    def count_cartridge(self, value):
        raise "Изменение запрещено!"
    
    @property
    def types_cartridge(self):
        return self.__types_cartridge

    @count_cartridge.setter
    def types_cartridge(self, value):
        raise "Изменение запрещено!"
    
    @property
    def current_type_cartridge(self):
        return self.__current_type_cartridge

    @count_cartridge.setter
    def current_type_cartridge(self, value):
        raise "Изменение запрещено!"

    @classmethod
    def __check_range(cls, x, y):
        return x >= cls.MAX_RANGE or y >= cls.MAX_RANGE

    @staticmethod
    def __check_coordinates(x, y):
        return x <= 0 or y <= 0
    
    def __del__(self):
        print("Объект удален.")

    def reload(self):
        print("Перезарядка.")

        self.__count_cartridge[self.__current_type_cartridge] = 3

    def shot(self, x, y):
        if self.__count_cartridge[self.__current_type_cartridge] <= 0:
            self.reload()
        
        if self.__check_coordinates(x, y):
            print("Ошибка. Координаты не должны быть меньше или равны нулю.")

            return
        
        if self.__check_range(x, y):
            print("Ошибка. Координаты не должны быть больше 1200.")

            return
        
        print(f"Выстрел {self.__current_type_cartridge} на координаты: {x}, {y}")

        self.__count_cartridge[self.__current_type_cartridge] -= 1

    def set_cartridge(self, type):
        "Types: [\"shrapnel\", \"smok\"]"

        if type not in self.__types_cartridge:
            print("Тип снаряда не найден!")

            return

        self.__current_type_cartridge = type

    def __getattribute__(self, name: str) -> Any:
        return object.__getattribute__(self, name)

    def __getattr__(self, name: str):
        print("Данного атрибута не существует.")

        return

    def __delattr__(self, name: str) -> None:
        print("Удаление атрибутов запрещено.")

        return

my_mortar = Mortar()

print(my_mortar.count_cartridge)

# my_mortar.count_cartridge = {
#     "shrapnel": 3,
#     "smok": 4
# }

print(my_mortar.current_type_cartridge)

my_mortar.current_type_cartridge = 1

my_mortar.shot(20, 1)
my_mortar.set_cartridge("smok")