from lib.menu import Menu
from lib.dish import Dish
import pytest

'''
Given a Dish
we can add it to the menu
'''
def test_adding_dish_to_menu():
    menu = Menu()
    burger = Dish("Burger", 599)

    menu.add_dish(burger)

    actual = menu.get_menu()

    expected = [burger]

    assert actual == expected

'''
Given multiple of the same Dish
get_menu only returns unique dishes
'''
@pytest.mark.skip(reason="Not core functionality")
def test_adding_the_same_dish_only_adds_one():
    menu = Menu()
    burger = Dish("Burger", 599)

    menu.add_dish(burger)
    menu.add_dish(burger)

    actual = menu.get_menu()

    expected = [burger]

    assert actual == expected

'''
Given different Dishes with the same attributes
get_menu only returns unique dishes
'''
@pytest.mark.skip(reason="Not core functionality")
def test_adding_identical_dishes_adds_one():
    menu = Menu()
    burger = Dish("Burger", 599)
    burger_1 = Dish("Burger", 599)

    menu.add_dish(burger)
    menu.add_dish(burger_1)

    actual = menu.get_menu()

    expected = [burger]

    assert actual == expected

'''
Given multiple Dishes
we can select one by item number
'''
def test_we_can_select_dish_by_number():
    menu = Menu()
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)

    menu.add_dish(burger)
    menu.add_dish(pizza)

    actual = menu.get_dish(1)

    expected = burger

    assert actual == expected