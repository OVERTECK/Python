def create_table(titles: list[str], rows: list[list[str, int]]) -> None:
    for i in range(len(rows)):
        rows[i] = list(map(str, rows[i]))

    max_width_cols = []
    count_cols = len(titles)

    for col in zip(titles, *rows):
        max_width_cols.append(len(max(col, key=len)))

    width_table = sum(max_width_cols)

    string = " ┌"

    for width_col, i in zip(max_width_cols, range(len(max_width_cols))):
        for index in range(-2, width_table + (count_cols * 3)):
            if i == len(max_width_cols) - 1:
                string += "─" * (width_col + 2)
                break

            if index == width_col:
                string += "┬"
                break

            string += "─"

    string += "┐"

    print(string)

    copy_values = rows[:]
    copy_values.insert(0, titles)

    all_table = copy_values

    for row, j in zip(all_table, range(len(all_table))):
        for width_col, col in zip(max_width_cols, row):
            print(" │ " + col.ljust(width_col), end="")

        print(" │")

        if j == len(all_table) - 1:
            break

        string = " ├"

        for width_col, i in zip(max_width_cols, range(len(max_width_cols))):
            for index in range(-2, width_table + (count_cols * 3) - 1):
                if i == len(max_width_cols) - 1:
                    string += "─" * (width_col + 2)
                    break

                if index == width_col:
                    string += "┼"
                    break

                string += "─"

        string += "┤"

        print(string)

    string = " └"

    for width_col, i in zip(max_width_cols, range(len(max_width_cols))):
        for index in range(-2, width_table + (count_cols * 3) - 1):
            if i == len(max_width_cols) - 1:
                string += "─" * (width_col + 2)
                break

            if index == width_col:
                string += "┴"
                break

            string += "─"

    string += "┘"

    print(string)

if __name__ == "__main__":
    create_table(["1", "2", "3"], [["1, 2, 3, 4, 5, 6", 1, 5], ["1, 412fsdfdsvcx", "sdfsdfsd", 3], ["123", "123", 5]])
    create_table(["x", "y", "3"], [[1, 2, 3], [14211111, 4241242222, 3333333]])
    create_table(["x", "F", "Y", "n", "F - Y"], [["0246", "2", "04446", "gf124124dv", "02446"], ["04896", "42412", "3333333", "123", "gf124124dvc"]])
    create_table(["x", "F", "Y", "n",], [[0.2915, 24444, 3, 4], ["-0.2446", "4241242222", "3333333", "123"]])