text = """When I was One I had just begun When I was Two I was nearly new"""
words = ['i', 'was', 'three', 'near']

def Text_words(text, words):

    text = text.lower()
    word_list = text.split()
    word_count = {word: 0 for word in words}
    for word in words:
        word_count[word] = word_list.count(word)
        return word_count

print(Text_words(text, words))
