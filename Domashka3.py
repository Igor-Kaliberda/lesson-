
numbers = [2, 5, 7, 10]

if  len(numbers) > 1:
    numbers.insert(0, numbers[-1])
    print(numbers)
    numbers.pop()
    print(numbers)

else:
    print(numbers)


numbers = [1]

if  len(numbers) > 1:
    numbers.insert(0, numbers[-1])
    print(numbers)
    numbers.pop()
    print(numbers)

else:
    print(numbers)

    numbers = []

    if len(numbers) > 1:
        numbers.insert(0, numbers[-1])
        print(numbers)
        numbers.pop()
        print(numbers)

    else:
        print(numbers)


numbers = [8, 6, 5, 10]

if  len(numbers) > 1:
    numbers.insert(0, numbers[-1])
    print(numbers)
    numbers.pop()
    print(numbers)

else:
    print(numbers)