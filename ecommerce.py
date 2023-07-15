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

def homepage():
    print("Welcome To EZ-Shopping!")
    print("--------------------------\n")
    print("1. Show Items For Sale ")
    print("2. Check Shopping Cart/ Checkout")
    print("3. Check Membership Status\n")

def type_handling():
    try:
        choice = int(input("Choose the category number based on your preferred action: "))
        return choice
    except:
        print("ERROR: Please enter an Integer.")

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
    category_choice = int(input("Please choose the desired Category Number(press 'b' to go back or 'h' for hompage): "))

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

    return item_choice, category_choice

# convert "1,2,4" --> [1,2,4]
def item_choice_handling(item_choice):
    item_choice_list = item_choice.split(",")
    return item_choice_list

#fxn for adding to cart
def adding_item_to_cart(cart, item_choice_list, chosen_dict):
    pdt_names = list(chosen_dict.keys())

    for element in item_choice_list:
        cart[pdt_names[int(element)-1]] = chosen_dict[pdt_names[int(element)-1]]

    return cart


#Option 2 - Check shopping cart / checkout

"""
Functions to be created for this section:

Fxn 1: Display the cart -> inputs: the cart in main.py 

-> ask them if they want to checkout
-> ask them if they want to edit the quantities of the pdt

Fxn 2: Add items to cart - DONE

Fxn 3: Remove items from cart 

Fxn 4: Edit the quanities and the cost of the product

-> ask for membership details 

Fxn 5: verify membership details

Fxn 6: calculate the total cost including corresponding membership discount - 15%, 10%, 5%, including GST etc

Fxn 7: Display the bill with all its sub-parts

Fxn 8: to accept credit card details 

Fxn 9: to send SMS on successful purchase

"""

def shopping_cart_checkout(shopping_cart):
    print("*****Shopping Cart*****")
    shoppingcart_length = len(shopping_cart)

    if shoppingcart_length == 0:
        print("This shopping cart is empty. Thinking of adding anything?")
    else:
        print("No. \tItem \tPrice")
        print("-----------------------")
        for i in range(shoppingcart_length):
            item == shopping_cart[i]
            print(f"{i + 1}. \t{item}")

def membership_check():
    print("***** MEMBERSHIP VERIFICATION *****"):

    M_verify = str(print("Please enter the last five numbers of your Membership number"))

    #Gold = 6785V
    #Silver = 0981Z
    #Bronze = 1324W

    if M_verify == "6785V":
        print("You have the Gold Membership, you are therefore entitled to a 15% Discount at Checkout")
    elif M_verify == "0981Z":
        print("You have the Silver Membership, you are therefore entitled to a 10% discount at Checkout")
    elif M_verify == "1324W":
        print("You have the Bronze Membership, you are therefore entitled to a 5% discount at checkout ")
    elif M_verify != str:
        print("ERROR: Please enter a valid number")
    else:
        print("You look like you dont have a membership, Please purchase one at the checkout if you are interested.")

def calculate_price():



def main():

    while True:
        homepage()
        choice = input("Please enter the number corresponding to the desired action: ")
        type_handling()

        if choice == 1: 
            show_items_for_sale()
        elif choice == 2:
            shopping_cart_checkout()
        elif choice == 3:
            membership_check()




    
    

    











