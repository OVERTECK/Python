from decimal import Decimal
from typing import Union

def change(get_money: Decimal, result_price: Decimal) -> Union[dict[str, int], str]:

    if result_price > get_money:
        return "Недостаточно денег"

    denomination = list(map(Decimal, ["2", "1", "0.25", "0.1", "0.05", "0.01"]))

    change_digit = get_money - result_price

    result_count = {}

    index_money = 0

    while change_digit > 0:

        money = denomination[index_money]

        if change_digit - money >= 0:
            change_digit -= money
            result_count[str(money)] = result_count.get(str(money), 0) + 1
        else:
            index_money += 1

    return result_count

get_money = Decimal(input("Введите количество полученных денег: "))
result_price = Decimal(input("Введите общую сумму покупки: "))

print(change(get_money, result_price))
        