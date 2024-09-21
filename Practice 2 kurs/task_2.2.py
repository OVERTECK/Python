import math as m
from table import create_table

print("Коркин Александр вариант 9 задание 2.2")

def f(x: float, a: float) -> float:
    if x > 3.5:
        y = m.sin(x) * abs(m.log(x))

        return y

    y = a * m.cos(x) ** 2 + m.e ** x

    return y

# a = float(input("a: "))
# table(["x", "y"], func_on_range(f, 2, 5, 0.25))

create_table(["имя", "фамилия", "дата рождения"], [["Александр", "Коркин", "2999-24-14"], ["Имя", "Фамилия", "2414-12-11"]])
create_table(["x", "y", "3"], [["1", "2", "3"], ["14211111", "4241242222", "3333333"]])
create_table(["x"], [["2221"], ["222"], ["333"]])