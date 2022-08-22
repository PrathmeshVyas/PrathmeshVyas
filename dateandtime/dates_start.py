from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print(today)
    print(today.day, today.month, today.year)
    # weekday(m=0, s=6)
    print("today weekday is", today.weekday())
    days = ["mon", "tue", "wed", "thru", "fri", "sat", "sunday"]
    print("which is a, days", days[today.weekday()])

    today=datetime.now()
    print("current date and time is", today)

    t=datetime.time(datetime.now())
    print("current time is", t)

main()