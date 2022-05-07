import smtplib
import security


class EmailAlert:
    """
     To send user email alert
    """

    def __init__(self):
        self.sender = security.sender
        self.password = security.email_pw

    def send_email(self, sender, name, dep_city, dep_code, arri_code, arri_city, price, purchase_link, outbound_date):
        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.sender, password=self.password)
            connection.sendmail(
                from_addr=self.sender,
                to_addrs=sender,
                msg=f"Subject:We Got the Dealzzzzz\n\nHi, {name}.\n Check out the deal we found! {dep_city} ({dep_code}) - {arri_city} ({arri_code})\n 1. {outbound_date[0]} ${price[0]} {purchase_link[0]}\n 2. {outbound_date[1]} ${price[1]} {purchase_link[1]}\n 3. {outbound_date[2]} ${price[2]} {purchase_link[2]}"
            )
