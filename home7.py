from collections import Counter


numbers1 = [1, 2, 2, 3, 1]
numbers2 = [4, 5, 4, 5, 6]
numbers3 = [1, 5, 6, 6, 5, 1, 0.5]

def find_numbers(numbers):
    count = Counter(numbers)
    for number, freq in count.items():
        if freq == 1:
            return number


print(find_numbers(numbers1))
print(find_numbers(numbers2))
print(find_numbers(numbers3))