def main() -> None:

    def count_letters_in_word(word: str) -> dict:
        dict_ = {}

        for letter in word:
            if letter.isalpha():
                dict_[letter] = word.count(letter)

        return dict_

    with open("words_true.txt", "r", encoding="utf-8") as file:
        words_true = list(map(str.strip, file.readlines()))

    # print(words_true)

    # words_true = [
    #     "привет",
    #     "как",
    #     "тебя",
    #     "дела",
    #     "сегодня",
    #     "пошёл",
    #     "магазин",
    #     "встретил",
    #     "там",
    #     "своего",
    #     "друга",
    #     "мы",
    #     "потом",
    #     "делали",
    #     "покупка"
    # ]

    # print(count_letters_in_word(words_true[0]))

    with open("file.txt", "r+", encoding="utf-8") as file:
        list_rows = file.readlines()

    list_rows = [row.split() for row in list_rows]

    count_letter_word = []

    dict_count_true_letter = {}

    for row_list in list_rows:

        for word in row_list:
            
            word = word.lower()

            if word in words_true:
                continue
            if len(word) == 1:
                continue            
            
            print(word)

            for word_true in words_true:

                dict_count_letter = count_letters_in_word(word)

                dict_count_letter_true = count_letters_in_word(word_true)

                count = 0

                for tuple_count_letter_true in count_letters_in_word(word_true).items():  

                    letter_true, count_letter_true = tuple_count_letter_true

                    # print(letter_true, word, count_letter_true, dict_count_letter.get(letter_true))

                    if letter_true in word and count_letter_true == dict_count_letter.get(letter_true):
                        count += 1
                    elif letter_true not in word:
                        count -= 1

                dict_count_true_letter[word_true] = count

            # row_list[word] = max(dict_count_true_letter.values())

            for key_word, value_count in dict_count_true_letter.items():
                if value_count == max(dict_count_true_letter.values()):
                    print(key_word)
            # print(dict_count_true_letter)

    # with open("result_file.txt", "w", encoding="utf-8") as file:
    #     file.writelines(list_rows)

main()