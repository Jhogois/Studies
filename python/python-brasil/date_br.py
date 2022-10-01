from datetime import datetime, timedelta

class DateBr:
    def __init__(self) -> None:
        self.registration_moment = datetime.today()

    def __str__(self) -> str:
        return self.format_date()
    
    def registration_month(self):
        year_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        registration_month = self.registration_moment.month
        return year_months[registration_month - 1]

    def week_day(self):
        week_day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        week_day = self.registration_moment.weekday()
        return week_day_list[week_day]

    def format_date(self):
        formatted_date = self.registration_moment.strftime("%A, %d/%m/%Y %H:%M")
        return formatted_date

    def registration_time(self):
        registration_time = (datetime.today() + timedelta(days=30)) - self.registration_moment
        return registration_time
