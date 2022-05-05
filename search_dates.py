import datetime as dt

class SearchDates:
    def __init__(self):
        self.date = dt.datetime.today() - dt.timedelta(days=1)
        self.days = dt.timedelta(days=6 * 30)

    def search_dates(self):
        start_date = self.date.strftime("%d/%m/%Y")
        future = self.date + self.days
        to_date = future.strftime("%d/%m/%Y")

        dates_for_travel = {
            'start_search': start_date,
            'end_search': to_date
        }

        return dates_for_travel
