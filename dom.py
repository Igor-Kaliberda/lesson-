

while True:
    kalk = int(input("1. +\n2. -\n3. *\n4. /\n5. exit "))

    match kalk:
            case 1:
                n1 = int(input("Enter 1 number "))
                n2 = int(input("Enter 2 number "))
                result = n1 + n2
                print(result)
                continue
            case 2:
                n1 = int(input("Enter 1 number "))
                n2 = int(input("Enter 2 number "))
                result2 = n1 - n2
                print(result2)
                continue
            case 3:
                n1 = int(input("Enter 1 number "))
                n2 = int(input("Enter 2 number "))
                result3 = n1 * n2
                print(result3)
                continue
            case 4:
                n1 = int(input("Enter 1 number "))
                n2 = int(input("Enter 2 number "))
                result4 = n1 / n2
                print(result4)
            case 5:
                end = int(input("exit"))
                print(end)
                break




