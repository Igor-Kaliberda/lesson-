numbers1 = (5, -5)
def min_max(numbers1):
    if not numbers1:
        return 0
    max_value = max(numbers1)
    min_value = min(numbers1)
    return round(max_value - min_value, 2)

print(min_max(numbers1))

numbers2 = [10.2, -2.2, 0, 1.1, 0.5]
def min_max(numbers2):
    if not numbers2:
        return 0
    max_value = max(numbers2)
    min_value = min(numbers2)
    return round(max_value - min_value, 2)
print(min_max(numbers2))


