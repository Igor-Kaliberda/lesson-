import re
from re import match

text = "Hello, world!"
def first_word(text):

    text = text.lstrip(' .,')


    match = re.search(r'\b\w[\w\']*\b', text)
    if match:
        return match.group(0)
    return ""




print(first_word(text))

