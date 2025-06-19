from lib.dish import Dish

# '''
# Test Dish initializes with correct name
# '''
# burger = Dish("Burger", 1000)

# actual = burger.name

# expected = burger

# '''
# Test Dish initializes with correct price
# '''
# burger = Dish("Burger", 1000)

# actual = burger.price

# expected = 1000

# '''
# trying to initialise with wrong type of name
# throws an error
# '''
# with pytest.raises(TypeError) as err:

# with pytest.raises(TypeError) as err:
#     burger = Dish(3, 10)

# error_message = str(err.value)

# expected = "Name must be a string."

# '''
# trying to initialise with wrong type of price
# throws an error
# '''
# with pytest.raises(TypeError) as err:

# with pytest.raises(TypeError) as err:
#     burger = Dish("Burger", 10.00)

# error_message = str(err.value)

# expected = "Price must be an Integer."

# '''
# test modifying name to an ivalid type 
# throws an error
# '''
# burger = Dish("Burger", 1000)

# with pytest.raises(TypeError) as err:
#     burger.name = 3

# error_message = str(err.value)

# expected = "Name must be a string."

# '''
# test modifying price to an ivalid type 
# throws an error
# '''
# burger = Dish("Burger", 1000)

# with pytest.raises(TypeError) as err:
#     burger.name = 10.99

# error_message = str(err.value)

# expected = "Price must be an integer."
