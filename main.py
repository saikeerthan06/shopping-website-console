#Main.py
"""We have created a separate file for main so that we can separate the other file and make it more organised.
every single action here is needed to be "FP." as we are importing from another file"""

import final_project as FP
import sending_SMS as SS
cart = {} #store the name + cost

choice = -1
while choice < 4:
    FP.homepage()
    choice = FP.type_handling()

    if choice == 1:
        #category_choice = FP.category_choice
        while True:
            item_choice, category_choice = FP.show_items_for_sale(cart)
            item_choice_list = FP.item_choice_handling(item_choice)
            chosen_dict = FP.category_dictionaries[category_choice-1]

            cart = FP.adding_item_to_cart(cart, item_choice_list, chosen_dict)
            option = input('Go back to main page y/n: ')
            if option == 'y':
                break
            else:
                continue

    elif choice == 2:
        FP.display_cart(cart)
        removal_ask = input("Do you want to remove any items(y/n):")
        
        if removal_ask == "yes" or removal_ask == "y":
            pdt_removal = input("Please select the associated number of the products you want to remove: ")
            pdt_removal_list = FP.item_choice_handling(pdt_removal) 
            FP.remove_item_cart(cart, pdt_removal_list)
            FP.display_cart(cart)


        elif removal_ask == "no" or removal_ask == "n":
            #pdt_quantity_ask = 'yes'
            #while pdt_quantity_ask == 'yes' or pdt_quantity_ask == 'y':
            pdt_quantity_ask = input("Would you like to change the quantity of any items?(y/n): ")

            if pdt_quantity_ask == "yes" or pdt_quantity_ask == "y":
                increase_ask = str(input("Would you like to increase the quantity of any of the items? (y/n):")).lower()

                if increase_ask == "yes" or increase_ask == "y":
                    pdt_id = int(input("Please enter the corresponding number of the Product:"))
                    pdt_qty = int(input("Please enter the new quantity of the above Product:"))
                    FP.increase_quantity(cart, pdt_id, pdt_qty)
                    FP.display_cart(cart)

                elif increase_ask == "no" or increase_ask == 'n':
                    decrease_ask =  str(input("Would you like to decrease the quantity of any of the items? (y/n):")).lower()

                    if decrease_ask == "yes" or decrease_ask == "y":
                        pdt_id_dec = int(input("Please enter the corresponding number of the Product:"))
                        pdt_qty_dec = int(input("Please enter the quantity by which you want to decrease: "))
                        FP.decrease_quantity(cart, pdt_id_dec, pdt_qty_dec)
                        FP.display_cart(cart)

            else:
                FP.display_cart(cart)
                
                        

        
                
    elif choice == 3:              
        FP.display_cart(cart)      
        
        checkout_ask = input("Would you like to check out?(y/n)")

        if (checkout_ask == "yes") or (checkout_ask == 'y'):
            FP.checkout(item_choice, cart)

            SS.sending_OTP()
            OTP_confirmation = input("An OTP is sent to the registered phone number ending with 8924.")

            if OTP_confirmation == 69420:
                print("Payment Successful! Thank you for using Gundam Store!")
                print("Have a great day ahead!")
            



        
""" while True:
                OTP_retry = input("ERROR: Please enter valid OTP. Press any key to resend OTP")
                SS.sending_OTP()
                OTP_confirmation_1 = str(input("Please input the OTP sent to your phone number"))
                if OTP_confirmation_1 == "69420":
                    print("Payment Successful! Thank you for using Gundam Store! Have a great day ahead!")"""
                
                
                

"""else:
                print("Payment Successful! Thank you for using Gundam Store! Have a great day ahead!")
            break"""
    
                        
                      

                
"""elif choice == 3:
        
        FP.checkout(item_choice, cart)"""





                
            






   

#question_co = print("Would you like to check out?(yes/no)").lower()
#if question_co == "Yes" or "y":
    #checkout()
#elif question_co == "No" or "n":
    #return show_items_for_sale
#else:
    #print("ERROR: Invalid Input, please try again")