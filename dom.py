numbers = [1, 3, 6, 8]
def Sumlist(numbers):
    suma = 0
    for i in range(len(numbers)):
        suma += numbers[i]
        return suma

resultat = Sumlist(numbers)
print(resultat)