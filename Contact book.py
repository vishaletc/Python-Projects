contact = {}

def display_contacts():
   print("Name\t\tContact Number")
   for key in contact:
       print("{}\t\t{}".format(key,contact.get(key)))
while True:
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Add Exit")

    choice = int(input("Enter your choice\n"))
    match choice:
        case 1:
            Name = input("Enter Contact Name\n")
            Phone= (input("Enter Phone Number\n"))
            Email = input("Enter the Email Address\n")
            Address = input("Enter the Address\n")
            print("Your Name is",Name)
            print("Your Phone Number is",Phone)
            print("Your Email Address is",Email)
            print("Your Address is",Address)
            contact[Name] = Phone
        case 2:
            Search_Name = input("Enter the Contact name\n")
            if Search_Name in contact:
                print(Search_Name,"'s Contact number is",contact[Search_Name])
            else:
                print("Name is not found in contact book")
        case 3:
            if not contact :
                print("Empty contact book")
            else:
                display_contacts()
        case 4:
            Edit_Contact = input("Enter the contact to be edited\n")
            if Edit_Contact in contact:
                Phone = input("Enter the Mobile Number")
                contact[Edit_Contact] = Phone
                print("Contact completed")
                display_contacts()
            else:
                print("Name is not found in contact book")
        case 5:
            Del_Contact = input("Enter the contact to be deleted\n")
            if Del_Contact in contact:
                confirm = input("Enter the contact to be delete y/n?\n")
                if confirm == 'y' or confirm == 'Y':
                    contact.pop(Del_Contact)

                    display_contacts()
                else:
                    print("Name is not found in contact book")
            else:
                break
        case 6:
            exit(0)