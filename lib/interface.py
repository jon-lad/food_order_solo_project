class Interface:
    def __init__(self, menu):
        self.__menu = menu

    def start_ordering(self):
        item_string = ""
        for i, menu_item in enumerate(self.__menu.get_menu()):
            item_string += f"    ({i+1}) {menu_item.format()}\n"

        display_string = f"Welcome! Please enter the item number to add to your order.\n\n{item_string[:-1]}\n\nPlease enter 'order' to see your order."
        print(display_string)
        command = input()
        match command:
            case '1':
                output_string = f"You have added a {self.__menu.get_dish(1).name} to your order\nPlease enter the item number to add another item to your order.\nEnter 'order' to see your order"
                print(output_string)
            case 'quit':
                exit()

    
    def _view_order(self):
        # Side effects:
        #   prints ordered dishes and prices and total price to console
        #   ask if they want to go back to the menu
        #   if so call start_ordering
        #   ask if they want to remove an item 
        #   if they want to remove item
        #   ask if they want to place order
        #   gets order processor to proceess order
        pass

    def _place_order(self):
        # Side effects:
        #   asks customer for phone number
        #   gets order processor process order
        pass