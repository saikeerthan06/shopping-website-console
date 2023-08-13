#SIGNING UP

import re, sys
import datetime
import Group2_EGC151_C6_sending_SMS as SS
import Group2_EGC151_C6_logic as GS

def is_valid_phone_number(phone_number):
    return re.match(r"^\d{8}$", phone_number)

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

def is_valid_birthdate(birthdate):
    try:
        year, month, day = map(int, birthdate.split('-'))
        date_obj = datetime.date(year, month, day)
        current_year = datetime.date.today().year

        if year < 1900 or year > current_year:
            return False

        if month < 1 or month > 12:
            return False

        if day < 1 or day > 31:
            return False

        # Check for February 30 and February 31
        if month == 2 and day > 29:
            return False

        # Check for months with 30 days
        if month in [4, 6, 9, 11] and day > 30:
            return False

        return True

    except ValueError:
        return False



users_info = {}  

def sign_up_for_membership():
    print("\n=== SIGN UP  ===")

    #user specific ditionary 
    new_user = {}

    while True:
        phone_number = input("Enter your phone number (or 'q' to quit): ")
        if phone_number.lower() == 'q':
            print("Thank you for visiting Gundam Store! See you again Soon!")
            sys.exit(1)  #to force exit
        if is_valid_phone_number(phone_number):
            new_user['phone_num'] = phone_number
            break
        print("Invalid phone number format. Please enter a valid phone number.")

    email = input("Enter your email (or 'q' to quit): ")
    if email.lower() == 'q':
        print("Thank you for visiting Gundam Store! See you again Soon!")
        sys.exit(1)
    while not is_valid_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter your email (e.g., example@example.com): ")
        if email.lower() == 'q':
            return False
    else:
        new_user['email'] = email

    full_name = input("Enter your full name as on NRIC: ")
    new_user['name'] = full_name

    while True:
        age_str = input("Enter your age: ")
        if age_str.isdigit():
            age = int(age_str)
            new_user["age"] = age
            break
        else:
            print("Invalid age. Please enter a valid number.")

    while True:
        birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
        if birthdate.lower() == 'q':
            new_user["birthdate"] = birthdate
            return False
        if is_valid_birthdate(birthdate):
            break
        print("Invalid birthdate format. Please enter a valid date in the format YYYY-MM-DD.")

    while True:
        credit_card = input("Please enter your 16 digit credit card number: ")
        if len(credit_card) != 16:
            print('ERROR: Please input a valid 16 digit Credit Card Number')
        else: 
            new_user['credit_card_num'] = credit_card
            break

    while True:
        CVV_number = input("Please enter your CVV Number: ")
        if len(CVV_number) != 3:
            print("ERROR: Please input Valid CVV number")
        else:
            new_user['cvv_num'] = CVV_number
            break

    while True:
        address = input("Please enter delivery address: ")

        if type(address) != str:
            print("Invalid Input! Please enter the correct Address: ")
        else:
            new_user['address'] = address
            break


    print("\n================ MEMBERSHIP DETAILS =====================\n")

    print("Gold Membership: $125, 15% Discount at checkout")
    print("Silver Membership: $90, 10% Discount at checkout")
    print('Bronze Membership: $50, 5% Discount at checkout\n')

    class_ask = input("Please Choose the Membership Class (eg: gold, silver, bronze) OR type 'nil' if you are not interested! : ").strip().lower()

    if class_ask not in ["gold", "silver", "bronze", "nil"]:
        print("ERROR: Please input a valid membership type")
        return sign_up_for_membership(credit_card)
    elif class_ask in ["gold", "silver", "bronze", "nil"]:
        new_user['membership_type'] = class_ask
        if class_ask == "gold":
            pp_ask = input("You have selected the gold membership class, you will be charged $125. Please press 'y' to continue: ")
            if pp_ask == "yes" or pp_ask == "y":
                amt = 125
                memb_id = '1234A'
                users_info[CVV_number] = new_user
       
        elif class_ask == "silver":
            pp_ask = input("You have selected the Silver membership class, you will be charged $90. Please press 'y' to continue: ")
            if pp_ask == "yes" or pp_ask == "y":
                #sending SMS in here
                amt = 90
                memb_id = '5678B'
                users_info[CVV_number] = new_user
        elif class_ask == "bronze":
            pp_ask = input("You have selected the Bronze membership class, you will be charged $50. Please press 'y' to continue: ")
            if pp_ask == "yes" or pp_ask == "y":
                amt = 50
                memb_id = '9101C'
                users_info[CVV_number] = new_user
    
        elif class_ask == "nil":
            users_info[CVV_number] = new_user

    
        if class_ask != "nil":
            print(f"${amt} has been charged to credit card number ending with {credit_card[-4:]}!")
            print(f"Your Membership ID is your CVV Number. Use this in Checkout for a discount!")
            SS.sending_confirmation(amt, credit_card, class_ask)
            print(f"An SMS has already been sent with the details to your number. Thank You for choosing {class_ask} Membership!\n")




#Viewing the Membership Details

def view_membership():
    ID_input = str(input("Please enter your CVV Number: "))

    #1. check if CVV is valid
    if len(ID_input) != 3:
        print("Invalid Input! Please enter a Valid CVV number.")
        return ID_input
    else:
        print("You can now view your Membership Information below: \n")
        if users_info[ID_input]['membership_type'] == "nil":
            print("You have not signed up for membership yet! Please Sign up at the Welcome Page if you are interested!")

    #2. check if it is in users_info
    if ID_input not in users_info:
        print('ERROR: Please input proper ID Input')
        return ID_input
    
   #3. iterate over the key-value item pairs together and display\
    print("\n========= MEMBERSHIP DETAILS =============\n")
    print(f"Name: {users_info[ID_input]['name']}")
    print(f"Email: {users_info[ID_input]['email']}")
    print(f"Age: {users_info[ID_input]['age']}")
    print(f"Phone Number: {users_info[ID_input]['phone_num']}")
    print(f"Membership Class: {users_info[ID_input]['membership_type']}\n\n")






