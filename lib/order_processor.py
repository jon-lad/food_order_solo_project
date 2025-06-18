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