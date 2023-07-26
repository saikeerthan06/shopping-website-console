#Main.py

import ecommerce as ECOMM

ECOMM.homepage()
choice = ECOMM.type_handling()

if choice == 1:
    #category_choice = ECOMM.category_choice

    item_choice, category_choice = ECOMM.show_items_for_sale()
    item_choice_list = ECOMM.item_choice_handling(item_choice)

    print(type(item_choice_list))
    cart = {} #store the name + cost

    chosen_dict = ECOMM.category_dictionaries[category_choice-1]

    cart = ECOMM.adding_item_to_cart(cart, item_choice_list, chosen_dict)


