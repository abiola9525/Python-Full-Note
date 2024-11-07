arithmetic = dict()

choice = None

while choice != "0":
    print(
                '''
                Arithmetic Operation

                0 - Exit
                1 - Addition
                2 - Subtraction
                3 - Multiplication
                4 - Division
                5 - Exponential
                ''')
    choice = input("choice: ")

    if choice == "0":
        print("You can now click on the close button")
        break

    elif choice == "1":
        x = float(input("Enter the first nuumber: "))
        y = float(input("Enter the second number: "))
        print("the sum is ", x + y)

    elif choice == "2":
        x = float(input("Enter the first nuumber: "))
        y = float(input("Enter the second number: "))
        print("the difference is ", x - y)

    elif choice == "3":
        x = float(input("Enter the first nuumber: "))
        y = float(input("Enter the second number: "))
        print("the product is ", x * y)

    elif choice == "4":
        x = float(input("Enter the first nuumber: "))
        y = float(input("Enter the second number: "))
        print("the division is ", x / y, "\n OR")
        print("the division is ", int(x // y) , "remainder ", int(x % y))

    elif choice == "5":
        x = float(input("Enter the nuumber: "))
        y = float(input("Enter the power: "))
        print("the difference is ", x ** y)

    else:
        print("INVALID INPUT. PLEASE CHECK THE OPTION AND TRY AGAIN")



