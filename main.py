from flask import Flask, render_template, request
import time
from flightsearch import FlightSearch
from search_dates import SearchDates
from sms_alert import SMSAlert
from email_alert import EmailAlert

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    flight_search = FlightSearch()
    search_dates = SearchDates()
    sms_alert = SMSAlert()
    email_alert = EmailAlert()

    if request.method == 'POST':
        name = request.form['name']
        choice_communication = request.form['communication']
        communication = request.form['radio-selection']
        from_location = request.form['departure']
        to_location = request.form['city1']
        start_date = search_dates.search_dates()['start_search']
        to_date = search_dates.search_dates()['end_search']

        find_city_dep_code = flight_search.find_code(from_location)
        find_city_arri_code = flight_search.find_code(to_location)

        flight_config = flight_search.flight_information(find_city_dep_code, find_city_arri_code, start_date, to_date)

        time.sleep(5)

        if choice_communication == "phone":
            sms_alert.set_up(name, communication, flight_config['dep_city'], flight_config['dep_code'],
                             flight_config['arrival_code'], flight_config['arrival_city'], flight_config['price'],
                             flight_config['purchase_link'], flight_config['outbound_date'])

        if choice_communication == "email":
            email_alert.send_email(communication, name, flight_config['dep_city'], flight_config['dep_code'],
                             flight_config['arrival_code'], flight_config['arrival_city'], flight_config['price'],
                             flight_config['purchase_link'], flight_config['outbound_date'])

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
