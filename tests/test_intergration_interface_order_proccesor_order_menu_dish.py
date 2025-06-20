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
interface prints menu to the console 
'''

def test_interface_prints_menu(capsys):
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)
    menu = Menu()
    menu.add_dish(burger)
    menu.add_dish(pizza)
    interface = Interface(menu)

    with patch('builtins.input') as mock_inputs:
        mock_inputs.side_effect = ['a']
        interface.start_ordering()

    actual = capsys.readouterr().out.strip().splitlines()

    assert actual[-6] == "Welcome! Please enter the item number to add to your order."
    assert actual[-4] == "    (1) Burger : £5.99"
    assert actual[-3] == "    (2) Pizza : £10.99"
    assert actual[-1] == "Enter 'order' to see your order, or 'quit' to exit."  

'''
Given a menu and a user inputting 1
interface.start_ordering prints you have ordered a burger
'''
def test_adding_item_to_order_prints_confirmation(capsys):
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)
    menu = Menu()
    menu.add_dish(burger)
    menu.add_dish(pizza)
    interface = Interface(menu)
    
    with patch('builtins.input') as mock_inputs:
        mock_inputs.side_effect = ['1', 'quit']
        interface.start_ordering()
    
    actual = capsys.readouterr().out.strip().splitlines()
    
    assert actual[-3] == "You have added a Burger to your order"
    assert actual[-2] == "Please enter the item number to add another item to your order."
    assert actual[-1] == "Enter 'order' to see your order, or 'quit' to exit."

'''
Given a menu and a user inputting 1 then 2 then 'order'
order is output to the console with total price
'''
def test_entring_order_prints_order(capsys):
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)
    menu = Menu()
    menu.add_dish(burger)
    menu.add_dish(pizza)
    interface = Interface(menu)

    with patch('builtins.input') as mock_inputs:
        mock_inputs.side_effect = ['1', '2', 'order', 'quit']
        interface.start_ordering()

    actual = capsys.readouterr().out.strip().splitlines()

    assert actual[-10] == "Your order:"
    assert actual[-8] == "    (1) Burger : £5.99"
    assert actual[-7] == "    (2) Pizza : £10.99"
    assert actual[-5] == "Total: £16.98"
    assert actual[-3] == "Enter item number to remove from your order."
    assert actual[-2] == "Enter 'menu' to return to the menu."
    assert actual[-1] == "Enter 'place' to place your order, or 'quit' to exit."


'''
Given a menu and a user inputting 1 then order then 1
an empty order is output to the console with 0 total price
'''
def test_removing_item_removes_from_order(capsys):
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)
    menu = Menu()
    menu.add_dish(burger)
    menu.add_dish(pizza)
    interface = Interface(menu)

    with patch('builtins.input') as mock_inputs:
        mock_inputs.side_effect = ['1', 'order', '1', 'quit']
        interface.start_ordering()

    actual = capsys.readouterr().out.strip().splitlines()

    assert actual[-8] == "Your order:"
    assert actual[-5] == "Total: £0.00"
    assert actual[-3] == "Enter item number to remove from your order."
    assert actual[-2] == "Enter 'menu' to return to the menu."
    assert actual[-1] == "Enter 'place' to place your order, or 'quit' to exit."

'''
Given a menu and a user inputting 1 then order then place
the customer is asked to enter their phone number
'''

def test_placing_order_asks_for_phone_number(capsys):
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)
    menu = Menu()
    menu.add_dish(burger)
    menu.add_dish(pizza)
    interface = Interface(menu)
    client = Mock()
    interface._order_processor = OrderProcessor(client)

    with patch('builtins.input') as mock_inputs:
        mock_inputs.side_effect = ['1', 'order', 'place', '']
        interface.start_ordering()

    actual = capsys.readouterr().out.strip().splitlines()

    assert actual[-3] ==  "Please enter a mobile number for confirmation."

'''
Given a menu and a user inputting 1 then order then place then a mobile number
the customer recieves confirmation that the order has been placed in th console
'''
def test_placing_order_confirmed_in_terminal(capsys):
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)
    menu = Menu()
    menu.add_dish(burger)
    menu.add_dish(pizza)
    interface = Interface(menu)
    client = Mock()
    interface._order_processor = OrderProcessor(client)

    with patch('builtins.input') as mock_inputs:
        mock_inputs.side_effect = ['1', 'order', 'place', '07000000000']
        interface.start_ordering()

    actual = capsys.readouterr().out.strip().splitlines()

    assert actual[-2] == "Your order has been placed we will send a text to"
    assert actual[-1] == "07000000000 to confim an expected delivery time." 

'''
Given a menu and a user inputting 1 then order then place then a mobile number
the customer recieves confirmation that the order has been placed as a message
'''

def test_place_sends_message_to_customer():
    burger = Dish("Burger", 599)
    pizza = Dish("Pizza", 1099)
    menu = Menu()
    menu.add_dish(burger)
    menu.add_dish(pizza)
    interface = Interface(menu)
    client = Mock()
    interface._order_processor = OrderProcessor(client)

    with patch('builtins.input') as mock_inputs:
        mock_inputs.side_effect = ['1', 'order', 'place', '07000000000']
        interface.start_ordering()

    client.messages.create.assert_called_with(to="+447000000000", from_="+15005550006", body="Thank you! Your order was placed and will be delivered before 18:52")