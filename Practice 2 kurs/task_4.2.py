def numbers_element_less_k() -> None:
    import random as r

    print("Коркин Александр вариант 9 задание 4.2")

    count_cols = int(input("Введите количество столбцов матрицы: "))
    count_rows = int(input("Введите количество строк матрицы: "))

    matrix = [[r.randrange(100) for _ in range(count_cols)] for _ in range(count_rows)]

    k = int(input("Введите K: "))

    result_arr = []

    for i in range(count_rows):
        for j in range(count_cols):
            if matrix[i][j] < k:
                result_arr.append((i + 1, j + 1))

    for i in range(count_rows):
        print(*matrix[i])

    print(*result_arr)

numbers_element_less_k()