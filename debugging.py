from  lib.interface import Interface
from lib.dish import Dish
from lib.menu import Menu

burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)
menu = Menu()
menu.add_dish(burger)
menu.add_dish(pizza)
interface = Interface(menu)

interface.start_ordering()
