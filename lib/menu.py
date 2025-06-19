class Menu:
    def __init__(self):
        self.__food_items = []

    def add_dish(self, dish):
        self.__food_items.append(dish) 

    def get_menu(self):
        return self.__food_items

    def get_dish(self, item_number):
        return self.get_menu()[item_number - 1]