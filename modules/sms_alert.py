import security
from twilio.rest import Client


class SMSAlert:

    """
    This class houses function set_up which provides the set-up to send sms travel alert.
    """

    def __init__(self):
        self.sms_number = security.sms_number
        self.account_sid = security.sms_sid
        self.token = security.sms_token

    def set_up(self, name, number, dep_city, dep_code, arri_code, arri_city, price, purchase_link, outbound_date):
        client = Client(self.account_sid, self.token)

        message = client.messages.create(
            body=f"Hi, {name}. Check out the deal we found! {dep_city} ({dep_code}) - {arri_city} ({arri_code} "
                 f"1. {dep_code} - {arri_code} {outbound_date[0]} ${price[0]}) {purchase_link[0]}" 
                 f"2. {dep_code} - {arri_code} {outbound_date[1]} ${price[1]}) {purchase_link[1]}" 
                 f"3. {dep_code} - {arri_code} {outbound_date[2]} ${price[2]}) {purchase_link[2]}",
            from_=self.sms_number,
            to=f'+1{number}'
        )

        print(message.sid)
