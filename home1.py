def number(digit):
    if digit % 2 == 0:
        return True
    else:
        return False



assert number(2) == True, 'Test1'
assert number(5) == False, 'Test2'
assert number(0) == True, 'Test3'


print(number(2))
print(number(5))
print(number(0))