def count_vowels_letters(string: str) -> int:
    list_vowels_letters = ["ё", "у", "е", "ы", "а", "о", "э", "я", "и", "ю"]

    string = string.lower()

    count_result = 0

    for letter in string:
        if letter in list_vowels_letters:
            count_result += 1

    return count_result

print(count_vowels_letters("Привет, как дела"))