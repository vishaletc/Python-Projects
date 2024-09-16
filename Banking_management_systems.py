
while True:
    balance = 35000.80
    print("1.Enter your PIN")
    print("2.Amount to Withdraw")
    print("3.Amount to deposit")
    print("4.Exit")
    a = int(input("Enter the number\n"))
    match a:  
        case 1:
            pin = int(input("Enter your pin\n"))
            if pin == 123:
                        accout = int(input("Enter your Account Number\n"))
                        name = input("Enter your name\n")
                        dob = input("Enter your D.O.B\n")
                        phone = int(input("Enter your phone number\n"))
                        address = input("Enter your address\n")
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
            withdraw = float(input("Enter amount withdraw from your account\n"))
            availale_balance =balance - withdraw
            print("After You withdraw amount is:",withdraw)
            print("Available balance is:",availale_balance)
        case 3:
                deposit = float(input("Enter amount deposit int your bank account\n"))
                availale_balance = deposit + balance
                print("After deposit amount your balance is:",deposit)
                print("Available balance is:",availale_balance)
                Exit = input("Remove your card")
                if  Exit == "Amount withdraw successfully":
                    print("Remove your card")
                elif Exit =="Amount deposit successfully":
                    print("Remove your card")
        case default:
            exit()
