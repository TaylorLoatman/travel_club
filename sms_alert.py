import security


class SMSAlert:
    def __init__(self):
        self.sms_number = security.sms_number
        self.account_sid = security.sms_sid
        self.token = security.sms_token

    def set_up(self, name, number, dep_city, dep_code, arri_code, arri_city, price, purchase_link, outbound_date):
        client = Client(self.account_sid, self.token)

        message = client.messages.create(
            body=f"Hi, {name}. Check out the deal we found! {dep_city} ({dep_code}) - {arri_city} ({arri_code} "
                 f"{outbound_date} ${price}) {purchase_link}",
            from_=self.sms_number,
            to=f'+1{number}'
        )

        print(message.sid)
