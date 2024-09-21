# Магические метод __new__. Паттерн Singleton.

class Mortar:
    __instance = None

    puk = 2

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        self.count_cartridge = {
            "shrapnel": 3,
            "smok": 3
        }

        self.types_cartridge = ["shrapnel", "smok"]

        self.current_type_cartridge = "shrapnel"

    def __del__(self):
        print("Объект удален.")

    def reload(self):
        print("Перезарядка.")

        self.count_cartridge[self.current_type_cartridge] = 3

    def shot(self, x, y):
        if self.count_cartridge[self.current_type_cartridge] <= 0:
            self.reload()
        
        print(f"Выстрел {self.current_type_cartridge} на координаты: {x}, {y}")

        self.count_cartridge[self.current_type_cartridge] -= 1

    def set_cartridge(self, type):
        "Types: [\"shrapnel\", \"smok\"]"

        if type not in self.types_cartridge:
            print("Тип снаряда не найден!")

            return

        self.current_type_cartridge = type

my_mortar = Mortar()
my_mortar_2 = Mortar()

print(id(my_mortar), id(my_mortar_2))