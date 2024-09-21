def main():
    def perfect_number(number: int) -> bool:
        dividers = []

        for i in range(1, number):
            if number % i == 0:
                dividers.append(i)

        return sum(dividers) == number

    with open("result.txt", "w") as file:    
        for i in range(1, 10001):
            if perfect_number(i):
                file.write(str(i) + "\n")

main()