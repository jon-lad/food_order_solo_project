from lib.order import Order
from lib.order_processor import OrderProcessor
from twilio.rest import Client
from lib.auth import account_sid, auth_token

class Interface:
    def __init__(self, menu):
        self.__menu = menu
        self.__order = Order()
        self._order_processor = OrderProcessor(Client(account_sid, auth_token))

    def start_ordering(self) -> None:
        self._print_menu()

        command = self._get_user_input()
        
        inputting = True

        while inputting:
            if command.isnumeric() and int(command) in range(1, len(self.__menu.get_menu()) +1 ):
                self._add_item_to_order(int(command))
                command = self._get_user_input()
                continue
            
            if command == "order":
                self._view_order()

            if command =="quit":
                return

            inputting = False
    
    def _print_menu(self):
        print("Welcome! Please enter the item number to add to your order.\n")
        print(self._format_menu_items())
        print("Enter 'order' to see your order, or 'quit' to exit.\n")

    def _print_order(self):
        print("Your order:\n")
        print(self._format_order_items())
        print(f"Total: {self._format_price(self.__order.get_total_price())}\n")
        print("Enter item number to remove from your order.")
        print("Enter 'menu' to return to the menu.")
        print("Enter 'place' to place your order, or 'quit' to exit.\n")

    def _print_dish_added_to_order(self, dish):
        print(f"You have added a {dish.name} to your order")
        print("Please enter the item number to add another item to your order.")
        print("Enter 'order' to see your order, or 'quit' to exit.\n")

    def _print_confirmation(self, phone_number):
        print("Your order has been placed we will send a text to")
        print(f"{phone_number} to confim an expected delivery time.")

    def _format_menu_items(self) -> str:
        item_string = ""
        for i, menu_item in enumerate(self.__menu.get_menu(), 1):
            item_string += f"    ({i}) {menu_item.format()}\n"
        return item_string
    
    def _format_order_items(self) -> str:
        item_string = ""
        for i, order_item in enumerate(self.__order.get_dishes(), 1):
            item_string += f"    ({i}) {order_item.format()}\n"
        return item_string
    
    def _format_price(self, price: int) -> str:
        pounds, pence = divmod(price, 100)
        return f"£{pounds}.{pence:02}"
    
    def _get_user_input(self) -> str:
        return input().strip()
    
    def _add_item_to_order(self, item_number: int) -> None:
        dish = self.__menu.get_dish(item_number)
        self.__order.add_dish(dish)
        self._print_dish_added_to_order(dish)
    
    def _view_order(self):
        self._print_order()

        command = self._get_user_input()
        
        inputting = True

        while inputting:
            if command.isnumeric() and int(command) in range(1, len(self.__order.get_dishes()) +1 ):
                self.__order.remove_dish(int(command))
                self._print_order()
                command = self._get_user_input()
                continue
            
            if command == "menu":
                self.start_ordering()

            if command =="quit":
                return
            
            if command == "place":
                self._place_order()
                return       


            inputting = False

    def _place_order(self):
        print("Please enter a mobile number for confirmation.")
        phone_number = input().strip()
        self._order_processor.process_order(self.__order, phone_number)
        self._print_confirmation(phone_number)