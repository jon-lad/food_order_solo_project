class Order:
    def __init__(self):
        self.__ordered_items = []
    
    def add_dish(self, dish):
        self.__ordered_items.append(dish)

    def remove_dish(self, item_number):
        self.__ordered_items.pop(item_number - 1)

    def get_dishes(self):
        return self.__ordered_items

    def get_total_price(self):
        return sum(dish.price for dish in self.__ordered_items)