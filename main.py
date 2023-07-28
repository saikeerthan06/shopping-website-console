#Main.py

import final_project as FP
cart = {} #store the name + cost

choice = -1
while choice < 4:
    FP.homepage()
    choice = FP.type_handling()
    if choice == 1:
        #category_choice = FP.category_choice

        item_choice, category_choice = FP.show_items_for_sale(cart)
        item_choice_list = FP.item_choice_handling(item_choice)
        chosen_dict = FP.category_dictionaries[category_choice-1]

        cart = FP.adding_item_to_cart(cart, item_choice_list, chosen_dict)

    elif choice == 2:
        FP.display_cart(cart)
        break





