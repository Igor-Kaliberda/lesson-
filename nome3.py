def funk_gen(func, number, n):
    current = number
    for _ in range(n):
        yield current
        current = func(current)



def kvadrat(x):
    return x ** 2

gen = funk_gen(kvadrat, 2, 5)
for number in gen:
    print(number)