import re
import datetime

"""
Project development
---------------------
1. Complete shopping list and user friendly menu for category selection. Ease of selections.
2. After selecting a category. Ease of items selection and quantity to purchase.
3. Shopping cart showing items purchased,  quantities, total prices. Clarity to viewers.
4. Ent1ries validation, checking for wrong entries.
5. Ease of adding items to the cart.
6. Ease of removing items from the cart.
7. Ease of changing quantity in the cart.
8. Users prompted for discount types upon Check-out
9. Bill statement: Total price before discount & GST, Discount, GST after discount, Total Payable. Alignment & Clarity to viewers.
10. Accuracy of calculations. Total price before discount & GST, Discount, GST after discount, Total Payable.
"""



def get_time_of_day_greeting():
    current_hour = datetime.datetime.now()
    print("Good morning! Current Date and Time: ")
    print(current_hour.strftime("%B %d, %Y %H: %M:%S"))

def welcome_page():
    greeting = get_time_of_day_greeting()
    print(f"{greeting}")
    print("---- WELCOME TO GUNDAM STORE! ----")
    print("1. Sign Up/View Membership details")
    print("2. Enter Shopping Menu")
    print("3. Quit")


def homepage():
    print("----------------------------")
    greeting = get_time_of_day_greeting
    print("f{greeting}")
    print("Welcome To Gundam Store!")
    print("--------------------------\n")
    print("1. Show Items For Sale ")
    print("2. Check Shopping Cart")
    print("3. Check Membership Status and checkout\n")


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

def store_credit_card():
    credit_card = input("Please enter your credit card info: ")
    if len(credit_card) != 16:
        print('ERROR: Please input a valid 16 digit Credit Card Number')
    else: 
        CVV_number = input("Please enter your CVV Number: ")
        if len(CVV_number) != 3:
            print("ERROR: Please input Valid CVV number")
    
    print(f"Your Credit Card Number is{credit_card}")
    print(f"Your CVV number is{CVV_number}")
    cfm = input("Are these correct?(y/n):")

    if cfm == "yes" or cfm == "y":
        print("Thanks for confirming! You can now take a look at our items for sale!")
    elif cfm == "no" or cfm == "n":
        gb_ask = input('Would you like to go back and edit?(y/n): ')

        if gb_ask == "yes" or gb_ask == "y":
            return store_credit_card()
        else:
            homepage()


def homepage():
    print("----------------------------")
    greeting = get_time_of_day_greeting
    print("f{greeting}")
    print("---- Welcome To Gundam Store! ----")
    print("1. Show Items For Sale ")
    print("2. Check Shopping Cart")
    print("3. Check Membership Status and checkout\n")


def sign_up_for_membership():
    print("\n=== SIGN UP FOR MEMBERSHIP ===")

    while True:
        phone_number = input("Enter your phone number (or 'q' to quit): ")
        if phone_number.lower() == 'q':
            return False
        if is_valid_phone_number(phone_number):
            break
        print("Invalid phone number format. Please enter a valid phone number.")

    email = input("Enter your email (or 'q' to quit): ")
    if email.lower() == 'q':
        return False
    while not is_valid_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter your email (e.g., example@example.com, or 'q' to quit): ")
        if email.lower() == 'q':
            return False

    full_name = input("Enter your full name as on NRIC: ")

    while True:
        age_str = input("Enter your age: ")
        if age_str.isdigit():
            age = int(age_str)
            break
        else:
            print("Invalid age. Please enter a valid number.")

    while True:
        birthdate = input("Enter your birthdate (YYYY-MM-DD, or 'q' to quit): ")
        if birthdate.lower() == 'q':
            return False
        if is_valid_birthdate(birthdate):
            break
        print("Invalid birthdate format. Please enter a valid date in the format YYYY-MM-DD.")
    
    print("Gold Membership: $125, 15% Discount at checkout ")
    print("Silver Membership: $90, 10% Discount at checkout")
    print('Bronze Membership: $50, 5% Discount at checkout')
    class_ask = str(input("Please Choose the a Membership Class:")).lower()

    while True:
        if class_ask != str:
            print("ERROR: Please input valid membership type")

        elif class_ask == "Gold":
            print("You have selected the Gold membrship class, do you wish to proceed?(press 'q' to Quit): ").lower()
            if class_ask == 'y' or class_ask == "yes":
                #enter SMS sending here 
                #print("SMS has been sent to the registered phone number")
                # SMS_confirmation == input("Please enter the OTP sent to you")
                #if SMS_confirmation == SMS
                print(f"$125 has been charged to your Credit Card number: {credit_card}! Thank you for being a member! a 15% discount will be added in checkout")
                print("This is your membership ID: 1234A")

        elif class_ask == "Silver":
            Silver_proceed = print("You have selected the Silver membrship class, do you wish to proceed?(press 'q' to Quit): ")
            if Silver_proceed == "y" or Silver_proceed == "yes":
                #enter SMS sending here 
                #print("SMS has been sent to the registered phone number")
                # SMS_confirmation == input("Please enter the OTP sent to you")
                #if SMS_confirmation == SMS
                print(f"$90 has been charged to your Credit Card! Thank you for being a member! a 10% discount will be added in checkout")
                print("This is your membership ID: 5678B")
            

        elif class_ask == "Bronze":
            bronze_proceed = input("You have selected the bronze membership class, do you wish to proceed?(press 'q' to Quit)(y/n):")

            if class_ask == "yes" or class_ask == "y":
                #enter SMS sending here 
                #print("SMS has been sent to the registered phone number")
                # SMS_confirmation == input("Please enter the OTP sent to you")
                #if SMS_confirmation == SMS
                print(f"$90 has been charged to your Credit Card! Thank you for being a member! a 5% discount will be added in checkout")
                print("This is your membership ID: 9101B")

        else:
            print("ERROR: Please input a valid response")
            return sign_up_for_membership()
        break


    print("\nCongratulations! You have successfully signed up for membership.")
    gb = input("Would you like to see items for sale?(y/n): ")

    if gb == "yes" or "y":
        show_items_for_sale()
    elif gb == "no" or "n":
        welcome_page()
    return True









global catalog_PG, Catalog_RG, Catalog_MG, Catalog_MG1, Catalog_M
catalog_PG = {"Gundam Raiser": 315.0, "Gundam Seed Astray": 320.0, "Wing Gundam": 350.0, "Freedom Gundam": 410.0}
Catalog_RG = {"RG GoldyMarg": 52.0, "RG Gao Gai Gar": 78.0, "God Gundam": 58.0, "Wing Gundam Astray": 38.0}
Catalog_MG = {"Eclipse Gundam": 195.0, "Full Saber": 72.0, "Unicorn Gundam": 64.0, "Gundam Dynames": 56.0}
Catalog_MG1 = {"Messiah Ranka Lee": 95.0, "Ganesa" :20.0, "Arcanadea Lumitea": 75.0, "Tsubasa Kazanari": 90.0}
Catalog_M = {"Little Ryan": 30.0, "Elephant Racer": 17.0, "Zoids Stylaser": 148.0,  "Cannon Bull": 35.0}

global category_dictionaries
category_dictionaries = [catalog_PG, Catalog_RG, Catalog_MG, Catalog_MG1, Catalog_M]

def show_items_for_sale():
    print("\n PRODUCTS FOR SALE")
    print("---------------------------")
    print("Categories")
    print("---------------------")
    print("1. Perfect Grade")
    print("2. Real Grade")
    print("3. Master Grade")
    print("4. Mecha Girl")
    print("5. Motorized")

    global category_choice
    category_choice = int(input("Please choose the desired Category Number: "))

    if category_choice == 1:
        print("\n==== Perfect Grade ====\n")

        #dictionary to store the product name and its cost
        counter_PG = 1

        print("Product\t\t\t|\t Cost")
        print("---------------------------------------------")
        for key, val in catalog_PG.items():
            if key == "Wing Gundam":
                print(f"{counter_PG}. {key}\t\t\t ${val}")
            else:
                print(f"{counter_PG}. {key}\t\t ${val}")
            counter_PG += 1

    elif category_choice == 2:
        print("\n==== Real Grade ====\n")
        counter_RG = 1

        print("Product\t\t\t|\t Cost")
        print("---------------------------------------------")
        for key, val in Catalog_RG.items():
            if key == "RG GoldyMarg" or key == "God Gundam":
                print(f"{counter_RG}. {key}\t\t\t ${val}")
            else:
                print(f"{counter_RG}. {key}\t\t ${val}")
            counter_RG += 1

    elif category_choice == 3:
        print("\n==== Master Grade ====\n")

        counter_MG = 1

        print("Product\t\t|\t Cost")
        print("---------------------------------------------")
        for key, val in Catalog_MG.items():
            if key == "Full Saber":
                print(f"{counter_MG}. {key}\t\t ${val}")
            else:
                print(f"{counter_MG}. {key}\t ${val}")
            counter_MG += 1

    elif category_choice == 4:
        print("\n==== Mecha Girl ====")

        counter_MG1 = 1

        print("Product\t\t |\tCost")
        print("---------------------------------------------")
        for key, val in Catalog_MG1.items():
            if key == "Ganesa":
                print(f"{counter_MG1}. {key}\t\t ${val}")
            else:
                print(f"{counter_MG1}. {key}\t ${val}")
            counter_MG1 += 1

    elif category_choice == 5:
        print("\n==== Motorised ====")

        counter_M = 1

        print("Product\t\t |\tCost")
        print("---------------------------------------------")
        for key, val in Catalog_M.items():
            if key == "Little Ryan" or key == "Cannon Bull":
                print(f"{counter_M}. {key}\t\t ${val}")
            else:
                print(f"{counter_M}. {key}\t ${val}")
            counter_M += 1

    item_choice = input("Please Select the item Number(s)(seperated by commas):")



    selected_products = [] #empty list nothing is added yet.



    return item_choice, category_choice


# convert "1,2,4" --> [1,2,4]
def item_choice_handling(item_choice):
    item_choice_list = item_choice.split(",")
    return item_choice_list
  

# fxn for adding to cart
def adding_item_to_cart(cart, item_choice_list, chosen_dict):

    pdt_names = list(chosen_dict.keys())

    for element in item_choice_list:
        cart[pdt_names[int(element) - 1]] = chosen_dict[pdt_names[int(element) - 1]]

    return cart






"""# convert "1,2,4" --> [1,2,4]
def item_choice_handling(item_choice):
    item_choice_list = item_choice.split(",")
    return item_choice_list

#fxn for adding to cart
def adding_item_to_cart(cart, item_choice_list, chosen_dict):
    pdt_names = list(chosen_dict.keys())

    for element in item_choice_list:
        cart[pdt_names[int(element)-1]] = chosen_dict[pdt_names[int(element)-1]]

    return cart"""


#Option 2 - Check shopping cart / checkout

"""
Functions to be created for this section:

Fxn 1: Display the cart -> inputs: the cart in main.py[DONE]

-> ask them if they want to checkout
-> ask them if they want to edit the quantities of the pdt

Fxn 2: Add items to cart - DONE

Fxn 3: Remove items from cart - DONE

Fxn 4: Edit the quanities and the cost of the product- DONE

-> ask for membership details- DONE

Fxn 5: verify membership details[IN PROGRESS]-DONE

Fxn 6: calculate the total cost including corresponding membership discount - 15%, 10%, 5%, including GST etc

Fxn 7: Display the bill with all its sub-parts

Fxn 8: to accept credit card details-DONE

Fxn 9: to send SMS on successful purchase-DONE

"""

def display_cart(cart):
    print("Name\t    Cost")
    print("----------------")

    #traversal through a dict:
    # in a dict = key = product name, and then your value = price
    counter = 1
    for key,value in cart.items(): #key= name, value = price
        print(f"{counter}. {key}\t {value}") # f for formatting, {} - refers to variable, we are "printing" the name and the associated price
        counter += 1

def remove_item_cart(cart, pdt_removal_list):
    
    pdt_list = list(cart.keys()) #function to convert dictionary keys into a list of keys 
    for i in pdt_removal_list:
        del cart[pdt_list[int(i)-1]]

    
def increase_quantity(cart, pdt_id, pdt_qty):
    cart_item_names = list(cart.keys())
    cart[cart_item_names[pdt_id-1]] = cart[cart_item_names[pdt_id-1]] * pdt_qty

def decrease_quantity(cart, pdt_id, pdt_qty):
    cart_item_names = list(cart.keys())
    cart[cart_item_names[pdt_id-1]] = cart[cart_item_names[pdt_id-1]] / (pdt_qty+1)
    
   
    
def membership_check():

    #Gold Membership: 1234A
    #Silver Membership: 5678B
    #Bronze Membership: 9101C

    m_check = str(input("Please enter the last five numbers of your Membership ID: "))
    trim_m_check = m_check.strip

    if len(trim_m_check) != 5:
        print("ERROR: Please enter Valid Membership ID: ")
    elif trim_m_check == "1234A" :
        discount = 0.15
        print(f"You are eligible for a 15% discount at checkout ")
    elif trim_m_check == "5678B":
        print(f"You are eligible to a 10% discount at checkout")
        discount = 0.10
    elif trim_m_check == "9101C":
        print(f"You are eligible for a 5% discount at checkout")
        discount = 0.05
    else:
        discount = 0
        print("It looks like you do not have a membership yet, would you like to purchase one at checkout?")

    
        



    
    








def checkout(item_choice ,cart):

    CC_number = str(input("Please enter your credit card number."))
    CVV_number = int(input("Please eneter your CVV Number"))

    if (len(CC_number) != 16) and (CVV_number != int):
      print("ERROR: Please inuput the correct Credit Card Number ")
    else:
      print("Your Credit Card has been registered.")

    subtotal = 0

    for item_choice in cart:
        #price = (item_choice.split("\t")[-1].strip("$"))
        price = float(cart[item_choice])
        subtotal += price 
    gst =  subtotal * 0.08
    total_amount = subtotal + gst

    #Define membership rates:

    membership_rates = {
        "1234A": 0.15,  #Gold Membership
        "5678B": 0.10,  #Silver Membership
        "9101C": 0.05   #Bronze Membership 

    }
    

    m_check = str(input("Please enter the last five numbers of your Membership ID: "))
    #trim_m_check = m_check.strip

    if len(m_check) != 5:
        print("ERROR: Please enter Valid Membership ID: ")
    elif m_check == "1234A" :
        discount = 0.15
        print(f"You are eligible for a 15% discount at checkout ")
    elif m_check == "5678B":
        print(f"You are eligible to a 10% discount at checkout")
        discount = 0.10
    elif m_check == "9101C":
        print(f"You are eligible for a 5% discount at checkout")
        discount = 0.05
    else:
        discount = 0
        print("It looks like you do not have a membership yet, would you like to purchase one at checkout?")

    

    final_price = total_amount - discount

    return subtotal, gst, total_amount, final_price


def main():
    shopping_list = []
    signed_up_for_membership = False

    while True:
        if not signed_up_for_membership:
            welcome_page()

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                sign_up_result = sign_up_for_membership()
                if sign_up_result:
                    signed_up_for_membership = True
                continue
            elif choice == "3":
                print("Thank you for using the Shopping List Program. Goodbye!")
                return
            elif choice != "2":
                print("Invalid choice.")
                continue
        show_items_for_sale()


        # Once signed up for membership or directly via option 2
        
        choice = input("Enter your choice (1-5): ")




if __name__ == "__main__":
    main()





