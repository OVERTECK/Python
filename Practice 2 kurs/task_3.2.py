def max_element() -> None:
    print("Коркин Александр вариант 9 задание 3")
    import random as r

    size_arr = int(input("Введите размер массива: "))

    list_ = []

    for _ in range(size_arr):
        list_.append(round(r.uniform(-100, 100), 2))

    print(*list_)

    print(max(list_))
    print(list_.index(max(list_)))

# max_element()

def main() -> None:
    print("Коркин Александр вариант 9 задание 3")
    import random as r

    size_arr = int(input("Введите размер массива: "))

    list_ = []

    for _ in range(size_arr):
        list_.append(r.randrange(100))

    print(*list_)

    filter_arr = list(filter(lambda x: x % 2 == 0 and (list_.index(x) + 1) % 2 == 0, list_))

    print(*filter_arr)
    print(len(filter_arr))

main()