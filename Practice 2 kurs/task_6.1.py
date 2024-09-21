def digit_to_string(string: str) -> str:
    dict_ = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    for key, value in dict_.items():
        string = string.replace(key, value)

    return string

print(digit_to_string("Привет 1 я 2 как дела 9 я тут 6 и тут 5"))