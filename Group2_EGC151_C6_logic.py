import re
import datetime
import Group2_EGC151_C6_sending_SMS as SS
import Group2_EGC151_C6_sign_up as SU

def get_time_of_day_greeting():
    current_hour = datetime.datetime.now()
    return current_hour.strftime("Greetings! Current Date and Time: %B %d, %Y %H:%M:%S")

def welcome_page():
    print("\n====== WELCOME TO GUNDAM STORE! ======")
    print("1. View Membership details")
    print("2. Enter Shopping Menu")
    print("3. Show Shopping Cart")
    print("4. Checkout")
    print("5. Quit")
    

def homepage():
    print("----------------------------")
    greeting = get_time_of_day_greeting()
    print(f"{greeting}")
    print("---- Welcome To Gundam Store! ----")
    print("1. Show Items For Sale ")
    print("2. Check Shopping Cart")
    print("3. Check Membership Status and checkout\n")


global catalog_PG, Catalog_RG, Catalog_MG, Catalog_MG1, Catalog_M
catalog_PG = {"Gundam Raiser": 315.0, "Gundam Seed Astray": 320.0, "Wing Gundam": 350.0, "Freedom Gundam": 410.0}
Catalog_RG = {"RG GoldyMarg": 52.0, "RG Gao Gai Gar": 78.0, "God Gundam": 58.0, "Wing Gundam Astray": 38.0}
Catalog_MG = {"Eclipse Gundam": 195.0, "Full Saber": 72.0, "Unicorn Gundam": 64.0, "Gundam Dynames": 56.0}
Catalog_MG1 = {"Messiah Ranka Lee": 95.0, "Ganesa" : 20.0, "Arcanadea Lumitea": 75.0, "Tsubasa Kazanari": 90.0}
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

    item_choice = input("Please Select the item Number(s)(separated by commas): ")

    selected_products = []  # empty list, nothing is added yet.

    return item_choice, category_choice


def item_choice_handling(item_choice):
    item_choice_list = item_choice.split(",")
    return item_choice_list


def adding_item_to_cart(cart, item_choice_list, chosen_dict):
    pdt_names = list(chosen_dict.keys())

    for element in item_choice_list:
        cart[pdt_names[int(element) - 1]] = chosen_dict[pdt_names[int(element) - 1]]

    return cart


def display_cart(cart):

    print("Name\t\t          |\t Cost")
    print("----------------------------------------")

    if len(cart) != 0:
        counter = 1
        for key, value in cart.items():
            if (key == "Full Saber") or (key == "Ganesa") or (key == "Wing Gundam") or (key == "RG GoldyMarg") or (key == "God Gundam") or (key == "Little Ryan") or (key == "Cannon Bull"):
                print(f"{counter}. {key}\t\t\t {value}")
            else:
                print(f"{counter}. {key}\t\t {value}")
            counter += 1
    else:
        print("Cart is Empty! Please add in items to Purchase!")


def remove_item_cart(cart, pdt_removal_list):
    if len(cart) != 0:
        pdt_list = list(cart.keys())
        for i in pdt_removal_list:
            del cart[pdt_list[int(i) - 1]]
    else:
        print("Cart is empty! Unable to remove further!")

def increase_quantity(cart, pdt_id, pdt_qty):
    cart_item_names = list(cart.keys())
    cart[cart_item_names[pdt_id - 1]] = cart[cart_item_names[pdt_id - 1]] * pdt_qty


def decrease_quantity(cart, pdt_id, pdt_qty):
    cart_item_names = list(cart.keys())

    for category in category_dictionaries:
        if cart_item_names[pdt_id-1] in category:
            if cart[cart_item_names[pdt_id - 1]] > category[cart_item_names[pdt_id-1]]:
                cart[cart_item_names[pdt_id - 1]] = cart[cart_item_names[pdt_id - 1]] / (pdt_qty + 1)
            else:
                remove_item_cart(cart, str(pdt_id))

def calculate_total_amount(cart, membership_type):
    #define membership type and corresponding discount
    if membership_type == 'gold':
        discount = 0.15
    elif membership_type == 'silver':
        discount= 0.10
    elif membership_type == 'bronze':
        discount = 0.05
    elif membership_type == "nil":
        discount = 1

    #constant - therefore variable name in Capslock
    GST = 0.08

    #getting the sum of all the products in the cart
    total_sum = sum(list(cart.values()))

    #calculating the discounted amount
    if membership_type != "nil":
        discounted_amount = discount * total_sum
    else:
        discounted_amount = 0

    discounted_price = total_sum - discounted_amount

    #final price after GST
    final_price = discounted_price + (GST * discounted_price)

    return total_sum, discounted_amount, discounted_price, final_price









    



