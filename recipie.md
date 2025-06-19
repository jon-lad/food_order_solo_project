# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## 2. Design the Class Interface
                                          ┌────────────────────────────┐ 
                                          │                            │ 
                                          │  Process order class       │ 
      ┌─────────────────────────┐         │                            │ 
      │                         │         │  message customer()        │ 
      │  interface class        │         │                            │ 
      │                         |─────────►                            │ 
      │   allows user to order  │         │                            │ 
      │   items                 │         │                            │ 
      │                         │         └────────────────────────────┘ 
      │                         |────────┐                               
      └──────────▲────────────▲─┘        │                               
                 │            │         ┌▼──────────────────────────────┬
                 │            └─────────|                               │
 ┌───────────────┼─────────────────┐    │ order class                   │
 │                                 │    │                               │
 │  menu  class                    │    │ list of selected items        │
 │                                 │    │    - add_dish item()          │
 │  list of food items with price  │    │    - remove item()            │
 │     - add_dish item()           │    │    - check items with total() │
 │     - list items()              │    │                               │
 │                                 │    │                               │
 └─────────────────────────────────┘    │                               │
                        ▲               └───────────────────────────────┘
                        │                                              
                        │                                               
                  ┌─────┴─────────────────────-──┐                       
                  │                              │                       
                  │   food class                 │                       
                  │                              │                       
                  │    food name                 │                       
                  │    food price                │                       
                  │                              │                       
                  │                              │                       
                  └──────────────────────────────┘                       

```python
class Dish:
    # User-facing properties:
    #   name: string
    #   price: int

    def __init__(self, name):
        # Parameters:
        #   name: string
        #   price: int (in pence)
        # Side effects:
        #   Sets the name property of the self object
        #   Sets the name property of the self object
        pass # No code here yet

    def __repr__(self):
        #Returns the name and price of the dish as a string
        pass

    def __eq__(self, other)
        #Returns true if atributes are the same

class Menu:
    # User-facing properties:
    #   dishes: list of Dish objects

    def __init__(self):
        # Side effects:
        #   Initialises the menu set
        pass # No code here yet

    def add_dish(self, dish):
        # Parameters:
        #   dish: Dish
        # Side effects:
        #   adds dish to menu list
        pass # No code here yet

    def get_menu(self):
        # Returns:
        #   a list of dishes available
        pass # No code here yet

    def get_dish(self, item_number):
        # Parameters:
        #   item_number: Dish
        # Returns:
        #   a copy of the dish available at position item_number
        pass # No code here yet

class Order:
    def __init__(self):
        # Side effects:
        #   Initialises the ordered list
        pass # No code here yet
    
    def add_dish(self, dish):
        # Parameters:
        #   dish: Dish
        # Side effects:
        #   adds a dish to the order
        pass

    def remove_dish(self, item_number):
        # Parameters:
        #   item_number: int (position of the dish to be removed)
        # Side effects:
        #   adds a dish to the order
        pass # no code here yet

    def get_dishes(self):
        # Returns:
        #   a list of dishes ordered
        pass # No code here yet

    def get_total_price(self):
        # Returns:
        #   the total price of the items in the order
        pass # No code here yet

class Interface:
    def __init__(self, menu):
        # Parameters:
        #   menu: a menu 
        # Side effects:
        #   Sets self.menu to menu
        #   initialises order object
        #   initialises order_processor
        pass

    def start_ordering(self):
        # Side effects:
        #   prints dishes and prices to console
        #   ask user if they want to add_dish dish to order
        #   adds selected dishes
        #   if user asks to see their order calls view_order
        pass

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

class OrderProcessor:
    def __init__(self, account_sid, auth_token, messsage_client):
        # Parameters:
        #   selfaccount_sid: Account SID from twilio
        #   auth_token: authentication token from twilio
        #   message_client: client used to send sms messages should be "from twilio.rest import Client"
        # Side effects:
            # Sets variables in self to parameters
            # Intialises order list
        pass

    def process_order(self, order, phone_number):
        #Parameters:
        #   order: Order object
        #   phone_number: string containing user inputed phone number
        #Side effects:
        #   asks customer for their number
        #   messages customer
        pass
```

## 3. Create Examples Intergration Tests

_Make a list of examples of how the class will behave in different situations._

``` python
'''
Given a Dish
we can add it to the menu
'''
menu = Menu()
burger = Dish("Burger", 599)

menu.add_dish(burger)

actual = menu.get_menu()

expected = [burger]

'''
Given multiple of the same Dish
get_menu only returns unique dishes
'''
menu = Menu()
burger = Dish("Burger", 599)

menu.add_dish(burger)
menu.add_dish(burger)

actual = menu.get_menu()

expected = [burger]

'''
Given different Dishes with the same attributes
get_menu only returns unique dishes
'''
menu = Menu()
burger = Dish("Burger", 599)
burger_1 = Dish("Burger", 599)

menu.add_dish(burger)
menu.add_dish(burger_1)

actual = menu.get_menu()

expected = [burger]

'''
Given multiple Dishes
we can select one by item number
'''
menu = Menu()
burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)

menu.add_dish(burger)
menu.add_dish(pizza)

actual = menu.get_dish(1)

expected = burger

assert actual == expected

'''
Given a menu
interface.start_ordering prints menu to the console 
'''
burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)
menu = Menu()
menu.add_dish(burger)
menu.add_dish(pizza)
interface = Interface(menu)

actual = capsys.interface.start_ordering()

expected = """Welcome! Please enter the item number to add_dish to your order.

(1) Burger : £5.99
(2) Pizza : £10.99

Please enter 'order' to see your order."""

'''
Given a menu and a user inputting 2 then 1
interface.start_ordering prints you have ordered a burger
'''
burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)
menu = Menu()
menu.add_dish(burger)
menu.add_dish(pizza)
interface = Interface(menu)

with patch('builtins.input', return_value='1')
    actual = capsys.interface.start_ordering()

    expected = """You have added a burger to your order
    Please enter the item number to add_dish another item to your order.
    Enter 'order' to see your order"""

'''
Given a menu and a user inputting 1 then 2 then 'order'
order is output to the console with total price
'''
#@patch('builtins.input')
#def test_
burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)
menu = Menu()
menu.add_dish(burger)
menu.add_dish(pizza)
interface = Interface(menu)

mock_inputs.side_effect = ['1', 'order']

actual = capsys.interface.start_ordering()

expected = """Your order:

(1) Burger : £5.99
(2) Pizza : £10.99

Total: £16.98

Please enter item number to remove from your order.
Please enter 'menu' to return to the menu.
please enter 'place' to place your order."""

'''
Given a menu and a user inputting 1 then order then menu
order is output to the console with total price
'''
#@patch('builtins.input')
#def test_
burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)
menu = Menu()
menu.add_dish(burger)
menu.add_dish(pizza)
interface = Interface(menu)

mock_inputs.side_effect = ['1', 'order', 'menu']

actual = capsys.interface.start_ordering()

expected = """Welcome! Please enter the item number to add_dish to your order.

(1) Burger : £5.99
(2) Pizza : £10.99

Please enter 'order' to see your order."""

'''
Given a menu and a user inputting 1 then order then 1
an empty order is output to the console with 0 total price
'''
#@patch('builtins.input')
#def test_
burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)
menu = Menu()
menu.add_dish(burger)
menu.add_dish(pizza)
interface = Interface(menu)

mock_inputs.side_effect = ['1', 'order', '1']

actual = capsys.interface.start_ordering()

expected = """Your order:

No items in order.

Total: £0.00

Please enter item number to remove from your order.
Please enter 'menu' to return to the menu.
please enter 'place' to place your order."""

'''
Given a menu and a user inputting 1 then order then place
the customer is asked to enter their phone number
'''
#@patch('builtins.input')
#def test_
burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)
menu = Menu()
menu.add_dish(burger)
menu.add_dish(pizza)
interface = Interface(menu)

mock_inputs.side_effect = ['1', 'order', 'place']

actual = capsys.interface.start_ordering()

expected = "Please enter a mobile number for confirmation."

'''
Given a menu and a user inputting 1 then order then place then a mobile number
the customer recieves confirmation that the order has been placed in th console
'''
#@patch('builtins.input')
#def test_
burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)
menu = Menu()
menu.add_dish(burger)
menu.add_dish(pizza)
interface = Interface(menu)

mock_inputs.side_effect = ['1', 'order', 'place', "07000000000"]

actual = capsys.interface.start_ordering()

expected = """Your order has been placed we will send a text to 
07000000000 to confim an expected dlivery time."""

'''
Given a menu and a user inputting 1 then order then place then a mobile number
the customer recieves confirmation that the order has been placed in th console
'''
#@patch('builtins.input')
#def test_
burger = Dish("Burger", 599)
pizza = Dish("Pizza", 1099)
menu = Menu()
menu.add_dish(burger)
menu.add_dish(pizza)
interface = Interface(menu)
client = Mock()
interface.order_processer = OrderProcessor( "test_SID" , "test_Auth", client)


mock_inputs.side_effect = ['1', 'order', 'place', "07000000000"]


client.messsages.create.assert_called_with(to="+447000000000", from_="+447000000001", body="Thank you! Your order was placed and will be delivered before 18:52")

```

_Encode each example as a test. You can add_dish to the above list as you go._

## 3. Create Example Unit Tests
``` python
#Dish
'''
Test Dish initializes with correct name
'''
burger = Dish("Burger", 1000)

actual = burger.name

expected = burger

'''
Test Dish initializes with correct price
'''
burger = Dish("Burger", 1000)

actual = burger.price

expected = 1000

'''
trying to initialise with wrong type of name
throws an error
'''
with pytest.raises(TypeError) as err:

with pytest.raises(TypeError) as err:
    burger = Dish(3, 10)

error_message = str(err.value)

expected = "Name must be a string."

'''
trying to initialise with wrong type of price
throws an error
'''
with pytest.raises(TypeError) as err:

with pytest.raises(TypeError) as err:
    burger = Dish("Burger", 10.00)

error_message = str(err.value)

expected = "Price must be an Integer."

'''
test modifying name to an ivalid type 
throws an error
'''
burger = Dish("Burger", 1000)

with pytest.raises(TypeError) as err:
    burger.name = 3

error_message = str(err.value)

expected = "Name must be a string."

'''
test modifying price to an ivalid type 
throws an error
'''
burger = Dish("Burger", 1000)

with pytest.raises(TypeError) as err:
    burger.name = 10.99

error_message = str(err.value)

expected = "Price must be an integer."

#Menu
'''
Menu Constructs
'''
menu = Menu()

actual = menu.get_menu()

expected = []

'''
Adding a non Dish to the menu
Throws an error
'''
menu = Menu()

with pytest.raises(TypeError) as err:
    menu.add_dish(3)

error_message = str(err.value)

expected = "Only dishes can be added to menu."

#Order
'''
Order Constructs
'''
order = Order()

actual = order.get_dishes()

expected = []

'''
calling remove on a dish which isnt in order 
Throws an error
'''
order = Order()

with pytest.raises(IndexError) as err:
    order.remove_dish(1)

error_message = str(err.value)

actual = "Invalid selection to remove from order"

#OrderProcessor Processor
'''
OrderProcessor Constructs
'''
client = Mock()
order_processor = OrderProcessor("SID", "Auth_key", client)

actual = order_processor._OrderProcessor__client

expected = client

#Interface
'''
OrderProcessor Constructs
'''
menu = Mock()
interface = Interface(menu)

actual = interface._Interface___menu

expected = menu

#TODO
#test menu for get_dish if nothing on menu
#Test order get_total_price with an empty list
#Test interface if menu is empty 
#Test interface if invalid input is entered
#Test interface if removing item not in order
#Test interface if adding item not on menu
#
```
_Encode each example as a test. You can add_dish to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
