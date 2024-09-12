a = int(input("Enter the number\n"))

pin = int(input("Enter your pin\n"))
balance = 35000.80
match a:
    case 1:
        if pin == 123:
            accout = int(input("Enter your Account Number\n"))
            name = input("Enter your name\n")
            dob = input("Enter your D.O.B\n")
            phone = int(input("Enter your phone number\n"))
            address = input("Enter your address\n");
            print("Welcome to Sbi bank Account....")
            print("Your Account number is : ",accout)
            print("Your name is : ",name)
            print("Your Date of Birth is ",dob)
            print("Your phone number is :",phone)
            print("Your Address is ",address)
            print("Your Available balance is ",balance)
        else:
            print("Invalid pin Number")
    case 2:
        withdraw = float(input("Enter amount withdraw from your account"))
        availale_balance =balance - withdraw
        print("After You withdraw amount is:",withdraw)
        print("Available balance is:",availale_balance)
    case 3:
        deposit = float(input("Enter amount deposit int your bank account"))
        availale_balance = deposit + balance
        print("After deposit amount your balance is:",deposit)
        print("Available balance is:",availale_balance)
        Exit = input("Remove your card")
        if  Exit == "Amount withdraw successfully":
            print("Remove your card")
        elif Exit =="Amount deposit successfully":
            print("Remove your card")
    case default:
        print("Invalid choice")
