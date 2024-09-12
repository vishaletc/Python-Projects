a = int(input("Enter the number\n"))

num1 = int(input("Enter the number 1\n"))
num2 = int(input("Enter the number 2\n"))

match a:
    case 1:
        add = num1 + num2
        print(add)
    case 2:
        sub = num1 - num2
        print(sub)
    case 3:
        mul = num1 * num2
        print(mul)
    case 4:
        div = num1 / num2
        print(div)
    case 5:
        mod = num1 % num2
        print(mod)
    case other:
        print("Invalid number")