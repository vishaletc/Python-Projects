
while True:
    print("Enter your choice...")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exit")

    a = int(input("Enter the number\n"))
    match a:
        case 1:
            num1 = int(input("Enter the number 1\n"))
            num2 = int(input("Enter the number 2\n"))
            add = num1 + num2
            print("Addition of two numbers is:",add)
        case 2:
            num1 = int(input("Enter the number 1\n"))
            num2 = int(input("Enter the number 2\n"))
            sub = num1 - num2
            print("Subtraction of two numbers is:",sub)
        case 3:
            num1 = int(input("Enter the number 1\n"))
            num2 = int(input("Enter the number 2\n"))
            mul = num1 * num2
            print("Multiplication of two numbers is:",mul)
        case 4:
            num1 = int(input("Enter the number 1\n"))
            num2 = int(input("Enter the number 2\n"))
            div = num1 / num2
            print("Divide of two numbers is:",div)
        case 5:
            num1 = int(input("Enter the number 1\n"))
            num2 = int(input("Enter the number 2\n"))
            mod = num1 % num2
            print("Modulus of two numbers is:",mod)
        case other:
            exit(0)
