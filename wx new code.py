import re
import datetime


def get_time_of_day_greeting():
    current_hour = datetime.datetime.now()
    print("Good morning! Current Date and Time: ")
    print(current_hour.strftime("%B %d, %Y %H: %M:%S"))



def show_welcome_page():
    greeting = get_time_of_day_greeting()
    print(f"{greeting}!")
    print("=== Welcome to the Shopping List Program! ===")
    print("1. Sign up for membership")
    print("2. Enter shopping menu")
    print("3. Quit")


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


def show_menu():
    print("\n==== SHOPPING LIST MENU ====")
    print("1. Show items for sale")
    print("2. Show shopping list and edit item quantity")
    print("3. Clear all shopping items")
    print("4. Pay for items")
    print("5. Quit")


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

    print("\nCongratulations! You have successfully signed up for membership.")
    return True


def add_item_to_shopping_list(shopping_list, item_name, item_price, quantity):
    existing_item_index = -1
    for idx, item in enumerate(shopping_list):
        if item[0] == item_name:
            existing_item_index = idx
            break

    if existing_item_index != -1:
        _, _, existing_quantity = shopping_list[existing_item_index]
        shopping_list[existing_item_index] = (item_name, item_price, existing_quantity + quantity)
    else:
        shopping_list.append((item_name, item_price, quantity))


def clear_shopping_list(shopping_list):
    choice = input("Are you sure you want to clear all shopping items? (y/n): ").lower()
    if choice == "y":
        shopping_list.clear()
        print("Shopping list has been cleared.")
    else:
        print("Operation cancelled. Shopping list not cleared.")


def show_shopping_list(shopping_list):
    print("\n=== SHOPPING LIST ===")

    list_length = len(shopping_list)
    if list_length == 0:
        print("The shopping list is empty.")
    else:
        print("No. \tItem \tPrice \tQuantity")
        print("--------------------")

        # Simple counter to track the item numbers
        item_number = 1

        for item in shopping_list:
            item_name, item_price, item_quantity = item
            print(f"{item_number}. \t{item_name} \t${item_price:.2f} \t{item_quantity}")
            item_number += 1

        print("--------------------")


def show_items_for_sale(shopping_list):
    while True:
        print("\n=== ITEMS FOR SALE ===")
        print("No \tCategory")
        print("1. Perfect Grade")
        print("2. Real Grade")
        print("3. Master Grade")
        print("4. Mecha Girl")
        print("5. Motorized")
        print("6. Go back to shopping menu")

        category_choice = input("Enter the category number to view items (or '6' to go back to the shopping menu): ")

        if category_choice == "6":
            return

        items = []

        if category_choice == "1":
            print("\n==== Perfect Grade ====")

            items = [
                ("GUNDAM RAISER", 315.0),
                ("Gundam SEED Astray", 320.0),
                ("Wing Gundam", 350.0),
                ("Freedom Gundam", 410.0),
            ]

        elif category_choice == "2":
            print("\n==== Real Grade ====")

            items = [
                ("RG GoldyMarg", 52.0),
                ("RG Gao Gai Gar", 78.0),
                ("God Gundam", 58.0),
                ("Wing Gundam Astray", 38.0),
            ]

        elif category_choice == "3":
            print("\n==== Master Grade ====")

            items = [
                ("Eclipse Gundam", 195.0),
                ("Full Saber", 72.0),
                ("Unicorn Gundam", 64.0),
                ("Gundam Dynames", 56.0),
            ]

        elif category_choice == "4":
            print("\n==== Mecha Girl ====")

            items = [
                ("Messiah Ranka Lee", 95.0),
                ("Ganesa", 20.0),
                ("Arcanadea Lumitea", 75.0),
                ("Tsubasa Kazanari", 90.0),
            ]

        elif category_choice == "5":
            print("\n==== Motorized ====")

            items = [
                ("Little Ryan", 30.0),
                ("Elephant Racer", 17.0),
                ("Zoids Stylaser", 148.0),
                ("Cannon Bull", 35.0),
            ]

        else:
            print("Invalid category choice.")
            continue

        selected_items = []

        while True:
            print("\n=== ITEMS FOR SALE ===")
            print("No \tItem\t\tPrice")

            for i in range(len(items)):
                item_name, item_price = items[i]
                print(f"{i + 1}\t{item_name}\t${item_price:.2f}")

            print()
            item_choice = input("Enter the item number to buy (or 'q' to go back to toy categories): ")

            if item_choice == "q":
                break

            try:
                item_number = int(item_choice)
                if 1 <= item_number <= len(items):
                    item_name, item_price = items[item_number - 1]
                    quantity = int(input("Enter the quantity to buy: "))
                    if quantity > 0:
                        add_item_to_shopping_list(shopping_list, item_name, item_price, quantity)
                        selected_items.append((item_name, item_price, quantity))
                    else:
                        print("Invalid quantity. Please enter a valid positive number.")
                else:
                    print(f"Invalid item number: {item_number}")

            except ValueError:
                print("Invalid input.")

        if selected_items:
            print("You have purchased:")
            for item in selected_items:
                item_name, item_price, item_quantity = item
                print(f"{item_name} - Price: ${item_price:.2f} - Quantity: {item_quantity}")
            print()

        print("Updated shopping list:")
        show_shopping_list(shopping_list)


def calculate_total_amount(shopping_list, membership_type):
    subtotal = 0

    for _, item_price, item_quantity in shopping_list:
        subtotal += item_price * item_quantity

    gst = subtotal * 0.08
    total_amount = subtotal + gst

    # Define membership discount rates
    membership_discounts = {
        "8976B": 0.15,  # Gold Membership - 15% discount
        "3501W": 0.10,  # Silver Membership - 10% discount
        "2347V": 0.05   # Bronze Membership - 5% discount
    }

    while True:
        if membership_type in membership_discounts:
            discount = total_amount * membership_discounts[membership_type]
            print(f"Membership Status: {membership_type}, You are entitled to a {int(membership_discounts[membership_type] * 100)}% discount at checkout")
            break
        elif membership_type.lower() == "none" or membership_type == "":
            discount = 0
            print("You have chosen not to apply a membership discount.")
            break
        else:
            print("Invalid membership code.")
            membership_type = input("Please enter the last 5 digits of your membership number (or 'none' to proceed without a membership discount): ").upper()

    total_amount_after_discount = total_amount - discount
    return subtotal, gst, total_amount, total_amount_after_discount


def edit_item_quantity(shopping_list):
    while True:
        if not shopping_list:
            return

        item_number1 = input("Do you want to edit an item's quantity (y/n)? ").lower()
        if item_number1 == "y":
            item_number_and_quantity = input("Enter the item number and new quantity to edit (e.g., '1:2' to set 2 items of number 1): ")

            edited_items = []
            try:
                items_to_edit = item_number_and_quantity.split(",")
                for item in items_to_edit:
                    item_number, quantity = map(int, item.strip().split(":"))
                    if 1 <= item_number <= len(shopping_list):
                        item_name, item_price, _ = shopping_list[item_number - 1]
                        if quantity == 0:
                            # Remove the item from the shopping list if the quantity is 0
                            del shopping_list[item_number - 1]
                            edited_items.append((item_name, item_price, 0))
                        else:
                            shopping_list[item_number - 1] = (item_name, item_price, quantity)
                            edited_items.append((item_name, item_price, quantity))
                    else:
                        print(f"Invalid item number: {item_number}")
            except ValueError:
                print("Invalid input.")

            if edited_items:
                print("Items edited:")
                for item in edited_items:
                    item_name, item_price, item_quantity = item
                    print(f"{item_name} - Price: ${item_price:.2f} - New Quantity: {item_quantity}")
                print()

            list_length = len(shopping_list)

            if list_length == 0:
                print("The shopping list is now empty.")
                return

            print("Updated shopping list:")
            show_shopping_list(shopping_list)

        else:
            return


def main():
    shopping_list = []
    signed_up_for_membership = False

    while True:
        if not signed_up_for_membership:
            show_welcome_page()

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

        # Once signed up for membership or directly via option 2
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_items_for_sale(shopping_list)
        elif choice == "2":
            show_shopping_list(shopping_list)
            edit_item_quantity(shopping_list)
        elif choice == "3":
            clear_shopping_list(shopping_list)
        elif choice == "4":
            if not shopping_list:
                print("The shopping list is empty. Please add items before proceeding with payment.")
            else:
                membership_type = input("Please enter the last 5 digits of your membership number (or 'none' to proceed without a membership code): ").upper()
                subtotal, gst, total_amount, total_amount_after_discount = calculate_total_amount(
                    shopping_list, membership_type
                )
                print("No. \tItem \tPrice \tQuantity")
                print("--------------------")
                for i, item in enumerate(shopping_list, start=1):
                    item_name, item_price, item_quantity = item
                    print(f"{i}. \t{item_name} \t${item_price:.2f} \t{item_quantity}")
                print("--------------------")

                print(f"\nSubtotal: ${subtotal:.2f}")
                print(f"GST (8%): ${gst:.2f}")
                print(f"Total amount to pay (including GST): ${total_amount:.2f}")
                print(f"Total price after discount: ${total_amount_after_discount:.2f}")

                credit_card_info_choice = input("\nEnter 1 to proceed with payment, or any other key to go back: ")
                if credit_card_info_choice == "1":
                    # Get and validate credit card details
                    while True:
                        credit_card = input("Enter your 16-digit credit card number: ")
                        if len(credit_card) == 16 and credit_card.isdigit():
                            break
                        else:
                            print("Invalid credit card number. Please enter a 16-digit number.")

                    while True:
                        expiration_date = input("Enter the expiration date (MM/YY): ")
                        if len(expiration_date) == 5 and expiration_date[2] == '/' and expiration_date[:2].isdigit() and expiration_date[3:].isdigit():
                            break
                        else:
                            print("Invalid expiration date. Please use the format MM/YY.")

                    while True:
                        cvv = input("Enter the 3-digit CVV code: ")
                        if len(cvv) == 3 and cvv.isdigit():
                            break
                        else:
                            print("Invalid CVV code. Please enter a 3-digit number.")

                            # Perform payment processing (not implemented in this code)

                    print("\nPayment processed. Thank you for your purchase!")
                    print(f"\nTotal amount paid: ${total_amount_after_discount:.2f}")
                    print("\nThank you for using the Shopping List Program. Goodbye!")

                    shopping_list.clear()
                    return  # Exit the program after successful payment
        elif choice == "5":
            print("Have a great day ahead!")
            return
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()