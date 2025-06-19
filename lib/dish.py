class Dish:
    # User-facing properties:
    #   name: string
    #   price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def format(self):
        pounds, pence = divmod(self.price, 100)
        return f"{self.name} : £{pounds}.{pence}"

    def __repr__(self):
        #Returns the name and price of the dish as a string
        return f"{self.name}:{self.price}"
    
    def __hash__(self) -> int:
        return hash((self.name, self.price))

    def __eq__(self, other):
        #Returns true if atributes are the same
        return self.name == other.name and self.price == other.price