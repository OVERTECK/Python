# Декораторы @staticmethod и @classmethod

class Mortar:
    MAX_RANGE = 1200

    @classmethod
    def check_range(cls, x, y):
        return x >= cls.MAX_RANGE or y >= cls.MAX_RANGE

    @staticmethod
    def check_coordinates(x, y):
        return x <= 0 or y <= 0

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
        
        if self.check_coordinates(x, y):
            print("Ошибка. Координаты не должны быть меньше или равны нулю.")

            return
        
        if self.check_range(x, y):
            print("Ошибка. Координаты не должны быть больше 1200.")

            return
        
        print(f"Выстрел {self.current_type_cartridge} на координаты: {x}, {y}")

        self.count_cartridge[self.current_type_cartridge] -= 1

    def set_cartridge(self, type):
        "Types: [\"shrapnel\", \"smok\"]"

        if type not in self.types_cartridge:
            print("Тип снаряда не найден!")

            return

        self.current_type_cartridge = type

my_mortar = Mortar()

my_mortar.shot(1240, 1)
my_mortar.check_range(1, 5)