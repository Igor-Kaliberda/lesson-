spisok1 = "hello, world"
spisok2 = "good bue, world"


def correct_spisok(spisok1, spisok2):
    def correct_noviy_spisok(spisok):
        if not spisok:
            return spisok
        sentence = spisok[0].upper() + spisok[1:]
        if not sentence.endswith('.'):
            sentence += '.'
        return sentence

    corrected_sentence1 = correct_noviy_spisok(spisok1)
    corrected_sentence2 = correct_noviy_spisok(spisok2)

    return corrected_sentence1, corrected_sentence2


corrected_spisok1, corrected_spisok2 = correct_spisok(spisok1, spisok2)

print(corrected_spisok1)
print(corrected_spisok2)