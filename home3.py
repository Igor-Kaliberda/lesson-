def second_occurrence(substring, string):
    first_index = string.find(substring)
    if first_index == -1:
        return -1
    second_index = string.find(substring, first_index + len(substring))

    return second_index
print(second_occurrence("s", "sims"))
print(second_occurrence("e", "find the river"))
print(second_occurrence("h", "hi"))
print(second_occurrence("lo", "Hello, hello"))
