import math
num = 0
while num != 3:
    print('\nMenu:\n1. Calculate triangle area by base and height\n2. Calculate triangle area by 2 sides and angle between them\n3. Exit\n')
    num = input("Enter menu item number: ")
    if not num.isdecimal():
        continue
    num = int(num)
    if num == 1:
        strInput = input("Enter base and height: ")
        listInput = strInput.split()
        if len(listInput) != 2:
            continue
        base = int(listInput[0])
        height = int(listInput[1])
        print("Area is: {:.2f}".format(base * height / 2))
    if num == 2:
        strInput = input("Enter 2 sides and angle(degrees) between them: ")
        listInput = strInput.split()
        if len(listInput) != 3:
            continue
        sideA = int(listInput[0])
        sideB = int(listInput[1])
        angle = int(listInput[2])
        print("Area is: {:.2f}".format(sideA * sideB * math.sin(math.radians(angle)) / 2))

print("\nGoodbye!")