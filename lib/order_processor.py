class OrderProcessor:
    def __init__(self, messsage_client):
        self.__message_client = messsage_client
        self.__orders = []

    def process_order(self, order, phone_number):
        self.__orders.append(order)
        formatted_number = "+44" + phone_number[1:]
        message = self.__message_client.messages.create(
            to= formatted_number,
            from_="+15005550006",
            body="Thank you! Your order was placed and will be delivered before 18:52")
        
        return message