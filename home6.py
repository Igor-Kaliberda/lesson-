import re
spisok = "A man, a plan, a canal, Panama"
spisok2 = "Hello, World!"
spisok3 = "a."

def is_palindrome(s):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

print(is_palindrome(spisok))
print(is_palindrome(spisok2))
print(is_palindrome(spisok3))