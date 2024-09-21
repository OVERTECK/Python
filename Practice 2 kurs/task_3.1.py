def count_digit_more_0() -> None:
    print("Коркин Александр вариант 9 задание 3")
    import random as r

    size_arr = int(input("Введите размер массива: "))

    list_ = []

    for _ in range(size_arr):
        list_.append(round(r.uniform(-100, 100), 2))

    print(*list_)

    filter_arr = list(filter(lambda x: x >= 0, list_))

    print(*filter_arr)
    print(len(filter_arr))

count_digit_more_0()