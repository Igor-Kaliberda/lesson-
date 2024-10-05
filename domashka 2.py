numbers = [10, 15, 8, 19, 7, 21]

part1 = numbers[:len(numbers)// 2]
part2 = numbers[len(numbers) // 2:]
result = [part1, part2]
print(result)

numbers1 = [2, 6, 9]
part3 = numbers1[len(numbers1) // -1:2]
part4 = numbers1[len(numbers1) -1]
result1 = [part3, part4]
print(result1)

numbers2 = [3, 5, 8, 9, 1]
part5 = numbers2[len(numbers2) // -1:3]
part6 = numbers2[len(numbers2) //  -3::]
result2 = [part5, part6]
print(result2)

numbers3 = [1]
part7 = numbers3[len(numbers3) // -1:]
part8 = numbers3[len(numbers3) // 1:]
result3 = [part7, part8]
print(result3)
