import math as m

print("Коркин Александр вариант 9 задание 1.1")

def f(x : float, y : float, z : float) -> float:
    
    result = ((1 + y) * m.sqrt(m.sin(z) ** 2) - (abs(y - x) / 5)) ** 3

    return result

x, y, z = float(input("x: ")), float(input("y: ")), float(input("z: "))

print(f"f = {f(x, y, z)}")