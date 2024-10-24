numbers1 = [1, 2, 3, 4]
numbers2 = [9, 9, 9,]
def add_one(digits):
    number1 = int(''.join(map(str, digits)))
    number1 += 1
    return [int(digit) for digit in str(number1)]


print(add_one(numbers1))
print(add_one(numbers2))
