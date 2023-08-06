#MAIN
import Group2_EGC151_C6 as GS
import sign_up as SU
import sending_SMS as SS
#from  Group2_EGC151_C6 import shopping_list
#from Group2_EGC151_C6 import membership_type


cart = {}
choice = -1

greeting = GS.get_time_of_day_greeting()
print(greeting,"\n")
print("================ Welcome to Gundam Store! ================")
print("Please Sign Up to Proceed:\n")
SU.sign_up_for_membership()
print("\n")
#GS.welcome_page()



while choice < 6:
    GS.welcome_page()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        SU.view_membership()
        continue
    
    elif choice == 2:
        while True:
            item_choice, category_choice = GS.show_items_for_sale()
            item_choice_list = GS.item_choice_handling(item_choice)
            chosen_dict = GS.category_dictionaries[category_choice - 1]

            cart = GS.adding_item_to_cart(cart, item_choice_list, chosen_dict)
            option = input('Go back to main page y/n: ')
            if option == 'y':
                break
            else:
                continue 

    elif choice == 3:
        GS.display_cart(cart)

        if len(cart) != 0:
            removal_ask = input("Do you want to remove any items(y/n):")
        
            if removal_ask == "yes" or removal_ask == "y":
                pdt_removal = input("Please select the associated number of the products you want to remove: ")
                pdt_removal_list = GS.item_choice_handling(pdt_removal) 
                GS.remove_item_cart(cart, pdt_removal_list)
                GS.display_cart(cart)


            elif removal_ask == "no" or removal_ask == "n":
                pdt_quantity_ask = input("Would you like to change the quantity of any items?(y/n): ")

                if pdt_quantity_ask == "yes" or pdt_quantity_ask == "y":
                    increase_ask = str(input("Would you like to increase the quantity of any of the items? (y/n):")).lower()

                    if increase_ask == "yes" or increase_ask == "y":
                        pdt_id = int(input("Please enter the corresponding number of the Product:"))
                        pdt_qty = int(input("Please enter the new quantity of the above Product:"))
                        GS.increase_quantity(cart, pdt_id, pdt_qty)
                        GS.display_cart(cart)

                    elif increase_ask == "no" or increase_ask == 'n':
                        decrease_ask =  str(input("Would you like to decrease the quantity of any of the items? (y/n):")).lower()

                        if decrease_ask == "yes" or decrease_ask == "y":
                            pdt_id_dec = int(input("Please enter the corresponding number of the Product:"))
                            pdt_qty_dec = int(input("Please enter the quantity by which you want to decrease: "))
                            GS.decrease_quantity(cart, pdt_id_dec, pdt_qty_dec)
                            GS.display_cart(cart)

                
    elif choice == 4:
        CVV_number = input("Please enter your CVV number to proceed: ")

        while len(CVV_number) != 3:
            CVV_number = input("Invalid Input! Please enter your CVV number correctly to proceed: ")
        else:
            print("\n============== BILL STATEMENT ==============\n")
            GS.display_cart(cart)
            print("\n")

            total_sum, discounted_amount, discounted_price, final_price = GS.calculate_total_amount(cart, SU.users_info[CVV_number]['membership_type'])

            print(f"Total Price before Discount: {total_sum:.2f}")
            print(f"Discounted Amount: {discounted_amount:.2f}")
            print(f"Total Price after Discount: {discounted_price:.2f}")
            print(f"GST Amount (8%): {(0.08 * discounted_price):.2f}\n")

            print(f"Total Amount Payable: {final_price:.2f}\n")

          
            system_OTP = SS.sending_OTP()
      
            OTP_input = int(input(f"Please enter the OTP sent to your phone number ending with {SU.users_info[CVV_number]['phone_num'][-5:]} to pay: "))

            if OTP_input == int(system_OTP):
                print("Payment Succesful! Items Purchased will be delivered within 3 working days!")
            else:
                print("Error! Please enter a valid OTP: ")

    elif choice == 5:
        print("Thank you for shopping with Gundam Store!")
        break
        
cart = {} #store the name + cost
