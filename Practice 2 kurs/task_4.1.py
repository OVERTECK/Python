def create_matrix() -> None:
    print("Коркин Александр вариант 9 задание 4.1")

    count_cols = int(input("Введите количество столбцов матрицы: "))
    count_rows = int(input("Введите количество строк матрицы: "))

    matrix = [[0]*count_cols for _ in range(count_rows)]

    for i in range(count_rows):
        for j in range(count_cols):
            if i == j:
                matrix[i][j] = 1
            elif i < j:
                matrix[i][j] = 3
            else:
                matrix[i][j] = 2

    for i in range(count_rows):
        print(*matrix[i])

create_matrix()