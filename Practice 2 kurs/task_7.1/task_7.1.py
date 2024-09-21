def count_lower_letters(path_to_file: str) -> int:
    with open(path_to_file, "r", encoding="utf-8") as file:
        text = file.read()

        count_result = 0

        for letter in text:
            if letter.islower():
                count_result += 1

    return count_result

print(count_lower_letters("file.txt"))