def main() -> None:
    import random as r

    print("Коркин Александр вариант 9 задание 5.1")

    count_cols = int(input("Введите количество столбцов матрицы: "))
    count_rows = int(input("Введите количество строк матрицы: "))

    matrix = [[r.randrange(-100, 100) for _ in range(count_cols)] for _ in range(count_rows)]

    for row in matrix:
        print(*row)

    result_arr = []

    max_digit = matrix[0][0]

    for i in range(count_rows):
        for j in range(count_cols):
            if (i + j + 2) % 4 == 0 and max_digit < matrix[i][j]:
                max_digit = matrix[i][j]

    print(max_digit)

main()