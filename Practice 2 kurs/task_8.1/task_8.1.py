def main() -> None:
    with open("file.txt", "r+", encoding="utf-8") as file:
        list_rows = file.readlines()

    for i in range(5, len(list_rows) + 1, 6):
        list_rows.insert(i, "***********\n")

    list_rows.insert(len(list_rows), "***********")

    with open("result_file.txt", "w", encoding="utf-8") as file:
        file.writelines(list_rows)

main()