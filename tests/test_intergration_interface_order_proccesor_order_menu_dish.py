from lib.dish import Dish
from lib.menu import Menu
from lib.interface import Interface
from lib.order import Order
from lib.order_processor import OrderProcessor
import pytest
from unittest.mock import Mock
from unittest.mock import patch

'''
Given a menu
interface.start_ordering prints menu to the console 
'''
def test_interface_prints_menu(capsys):
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)
    menu = Menu()
    menu.add_dish(burger)
    menu.add_dish(pizza)
    interface = Interface(menu)

    interface.start_ordering()
    captured = capsys.readouterr()

    actual = captured.out.strip()

    expected = "Welcome! Please enter the item number to add to your order.\n\n    (1) Burger : £5.99\n    (2) Pizza : £10.99\n\nPlease enter 'order' to see your order."
    
    assert actual == expected

'''
Given a menu and a user inputting 1
interface.start_ordering prints you have ordered a burger
'''
def test_ordering_item_prints_message(capfd, monkeypatch):
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)
    menu = Menu()
    menu.add_dish(burger)
    menu.add_dish(pizza)
    interface = Interface(menu)

    inputs = iter(['1', 'quit'])
    monkeypatch.setattr('builtins.input', lambda *args: next(inputs))

    interface.start_ordering()
    captured = capfd.readouterr().out.strip()
    lines = captured.splitlines()

    actual = "\n".join(lines[-3:])

    expected = "You have added a Burger to your order\nPlease enter the item number to add another item to your order.\nEnter 'order' to see your order"

    assert actual == expected

# '''
# Given a menu and a user inputting 1 then 2 then 'order'
# order is output to the console with total price
# '''
# #@patch('builtins.input')
# #def test_
# burger = Dish("Burger", 599)
# pizza = Dish("Pizza", 1099)
# menu = Menu()
# menu.add_dish(burger)
# menu.add_dish(pizza)
# interface = Interface(menu)

# mock_inputs.side_effect = ['1', 'order']

# actual = capsys.interface.start_ordering()

# expected = """Your order:

# (1) Burger : £5.99
# (2) Pizza : £10.99

# Total: £16.98

# Please enter item number to remove from your order.
# Please enter 'menu' to return to the menu.
# please enter 'place' to place your order."""

# '''
# Given a menu and a user inputting 1 then order then menu
# order is output to the console with total price
# '''
# #@patch('builtins.input')
# #def test_
# burger = Dish("Burger", 599)
# pizza = Dish("Pizza", 1099)
# menu = Menu()
# menu.add_dish(burger)
# menu.add_dish(pizza)
# interface = Interface(menu)

# mock_inputs.side_effect = ['1', 'order', 'menu']

# actual = capsys.interface.start_ordering()

# expected = """Welcome! Please enter the item number to add_dish to your order.

# (1) Burger : £5.99
# (2) Pizza : £10.99

# Please enter 'order' to see your order."""

# '''
# Given a menu and a user inputting 1 then order then 1
# an empty order is output to the console with 0 total price
# '''
# #@patch('builtins.input')
# #def test_
# burger = Dish("Burger", 599)
# pizza = Dish("Pizza", 1099)
# menu = Menu()
# menu.add_dish(burger)
# menu.add_dish(pizza)
# interface = Interface(menu)

# mock_inputs.side_effect = ['1', 'order', '1']

# actual = capsys.interface.start_ordering()

# expected = """Your order:

# No items in order.

# Total: £0.00

# Please enter item number to remove from your order.
# Please enter 'menu' to return to the menu.
# please enter 'place' to place your order."""

# '''
# Given a menu and a user inputting 1 then order then place
# the customer is asked to enter their phone number
# '''
# #@patch('builtins.input')
# #def test_
# burger = Dish("Burger", 599)
# pizza = Dish("Pizza", 1099)
# menu = Menu()
# menu.add_dish(burger)
# menu.add_dish(pizza)
# interface = Interface(menu)

# mock_inputs.side_effect = ['1', 'order', 'place']

# actual = capsys.interface.start_ordering()

# expected = "Please enter a mobile number for confirmation."

# '''
# Given a menu and a user inputting 1 then order then place then a mobile number
# the customer recieves confirmation that the order has been placed in th console
# '''
# #@patch('builtins.input')
# #def test_
# burger = Dish("Burger", 599)
# pizza = Dish("Pizza", 1099)
# menu = Menu()
# menu.add_dish(burger)
# menu.add_dish(pizza)
# interface = Interface(menu)

# mock_inputs.side_effect = ['1', 'order', 'place', "07000000000"]

# actual = capsys.interface.start_ordering()

# expected = """Your order has been placed we will send a text to 
# 07000000000 to confim an expected dlivery time."""

# '''
# Given a menu and a user inputting 1 then order then place then a mobile number
# the customer recieves confirmation that the order has been placed as a message
# '''
# #@patch('builtins.input')
# #def test_
# burger = Dish("Burger", 599)
# pizza = Dish("Pizza", 1099)
# menu = Menu()
# menu.add_dish(burger)
# menu.add_dish(pizza)
# interface = Interface(menu)
# client = Mock()
# interface.order_processer = OrderProcessor( "test_SID" , "test_Auth", client)


# mock_inputs.side_effect = ['1', 'order', 'place', "07000000000"]


# client.messsages.create.assert_called_with(to="+447000000000", from_="+447000000001", body="Thank you! Your order was placed and will be delivered before 18:52")