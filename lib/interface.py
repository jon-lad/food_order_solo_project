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
        #   ask user if they want to add dish to order
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