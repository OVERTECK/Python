import math as m

print("Коркин Александр вариант 9 задание 2.1")

def f(x : float) -> float:

    y = m.cos(x) ** 2 - m.sin(x) ** 3 + 2 * x ** 2

    return y

x = 0

while x <= 10:
    print(f(x))
    x += 0.5