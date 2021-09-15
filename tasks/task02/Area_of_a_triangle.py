# main menu
import math
print("Welcome to the triangle area calculation tool.")
while True:
    print("\n","Menu:","1. Calculate triangle area by base and height","2. Calculate triangle area by 2 sides and angle between them","3. Exit", sep = "\n")
    print("Enter menu item number: ", end = "")
    mitem = input()
    if mitem == "1":
        print("Enter base and height (space separated): ", end = "")
        while True:
            inp = input().split(" ")
            try:
                base, height = [float(x) for x in inp]
                print("\nbase =", base, " height =", height) 
                print("Area is: ", base * height / 2)
                break
            except ValueError: #could not convert string to float or too many/few values to unpack
                if len(inp) == 2:
                    err = "non-numeric"
                else:
                    err = len(inp)
                print("\nYou entered ", err," value(s). Please enter 2 numeric values space separated: ", end = "")
    elif mitem == "2":
        print("Enter 2 sides and angle(degrees) between them (space separated): ", end = "")
        while True:
            inp = input().split(" ")
            try:
                side1, side2, angle = [float(x) for x in inp]
                print("side1 =", side1, " side2 =", side2, " angle =", angle)
                print("Area is: ", (side1 * side2 * math.sin(angle * math.pi / 180) / 2))
                break
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
