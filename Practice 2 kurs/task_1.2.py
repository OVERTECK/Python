import math as m

print("Коркин Александр вариант 9 задание 1.2")

def f(b : float) -> float:

    if (isinstance(b, str)):
        raise Exception("Аргумент должен быть типа float") 

    def ctan(x : float) -> float:
        return m.cos(x) / m.sin(x)

    if b <= 0:
        b **= 2
    
    a = (1 + 4 * b) / (3 * b)
    
    x = a * m.cos(b) + m.sin(b ** 2)

    y = m.e ** x * ctan(x) - ((m.sqrt(x ** 2 + 2)) / m.log(abs(x)))

    return b, a, x, y

x = float(input("b: "))

b, a, x, y = f("f")

print(f"""
b: {b}
a: {a}
x: {x}
y: {y}""")

