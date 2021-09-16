# main menu
import math
print("\nWelcome to the triangle area calculation tool.")
while True:
    print("\nMenu:","1. Calculate triangle area by base and height","2. Calculate triangle area by 2 sides and angle between them","3. Exit", sep = "\n")
    mitem = input("Enter menu item number: ")
    if mitem == "1":
        print("\nEnter base and height (space separated): ", end = "")
        while True:
            inp = input().split(" ")
            try:
                base, height = map(float, inp)
                print(f"\nbase = {base}, height = {height}") 
                if base > 0 and height > 0:
                    print("Area is: ", base * height / 2)
                    break
                else:
                    print("The side lengths of the triangle must be positive numbers. Please enter 2 positive numbers: ", end = "")
            except ValueError: #could not convert string to float or too many/few values to unpack
                if len(inp) == 2:
                    err = "non-numeric"
                else:
                    err = len(inp)
                print("\nYou entered ", err," value(s). Please enter 2 numeric values space separated: ", end = "")
    elif mitem == "2":
        print("\nEnter 2 sides and angle(degrees) between them (space separated): ", end = "")
        while True:
            inp = input().split(" ")
            try:
                side1, side2, angle = map(float, inp)
                print(f"\nside1 = {side1}, side2 = {side2}, angle = {angle}")
                if side1 > 0 and side2 > 0 and angle > 0 and angle < 180:
                    print("Area is: ", round((side1 * side2 * math.sin(math.radians(angle)) / 2), 2))
                    break
                else:
                    print("The lengths of the sides of the triangle must be positive numbers, the angle between the sides of the triangle is greater than zero and less than 180 degrees. Please enter 3 numbers in valid ranges: ", end = "")
            except ValueError: #could not convert string to float or too many/few values to unpack
                if len(inp) == 3:
                    err = "non-numeric"
                else:
                    err = len(inp)
                print("\nYou entered ", err," value(s). Please enter 3 numeric values space separated: ", end = "")
    elif mitem == "3":
        print("Goodbye!")
        exit()
    else:
        print('\n', "Please enter correct menu item number!")
