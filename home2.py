
def common_elements():
    list1 = list(range(0, 100, 2))
    list2 = list(range(0, 100, 5))
    common = [element for element in list1 if element in list2]

    return common


print(common_elements())