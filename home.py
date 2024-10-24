import string

ALL_LETTERS = string.ascii_letters
SEPARATOR = "-"

user_input = input("Enter letters in format: 'a-c' ").strip()

if len(user_input) == 3:
    first_letter = user_input[0]
    second_letter = user_input[2]
    separator = user_input[1]

    if first_letter.isalpha() and second_letter.isalpha() and separator == SEPARATOR:
        start_index = ALL_LETTERS.index(first_letter)
        end_index = ALL_LETTERS.index(second_letter)

        if start_index > end_index:
            start_index, end_index = end_index, start_index

        result = ALL_LETTERS[start_index:end_index + 1]
        print(result)
