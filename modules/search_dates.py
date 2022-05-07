import datetime as dt
from dateutil.relativedelta import *


class SearchDates:

    """
    This class houses function search_dates
    provides users travel search dates based
    upon the time user submits form
    """

    def __init__(self):
        self.date = dt.datetime.today()
        self.month_six = dt.timedelta(days=6 * 30)
        self.month_three = dt.timedelta(days=3 * 30)
        self.month_one = dt.timedelta(days=30)
        self.week_2 = dt.timedelta(days=14)

    def search_dates(self, selected_date):

        start_date = self.date.strftime("%d/%m/%Y")
        to_date = start_date

        if selected_date == "6 months":
            future = self.date + self.month_six
            to_date = future.strftime("%d/%m/%Y")

        if selected_date == "3 months":
            future = self.date + self.month_three
            to_date = future.strftime("%d/%m/%Y")

        if selected_date == "1 months":
            future = self.date + self.month_one
            to_date = future.strftime("%d/%m/%Y")

        if selected_date == "2 weeks":
            future = self.date + self.week_2
            to_date = future.strftime("%d/%m/%Y")


        dates_for_travel = {
            'start_search': start_date,
            'end_search': to_date
        }

        return dates_for_travel
