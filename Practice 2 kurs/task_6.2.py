def zero_one(size_string: int) -> str:
    if size_string < 2:
        raise Exception("Длина строки должна быть больше 2.")

    string = ""

    for i in range(size_string):
        if i % 2 == 0:
            string += "0"
        else:
            string += "1"

    return string

print(zero_one(9))
