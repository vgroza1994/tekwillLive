import time
from datetime import datetime

def calculate_time_remaining(event_date):
    current_date = datetime.now()
    remaining_time = event_date - current_date
    total_seconds = remaining_time.total_seconds()

    days = int(total_seconds // (24 * 60 * 60))
    total_seconds %= (24 * 60 * 60)
    hours = int(total_seconds // (60 * 60))
    total_seconds %= (60 * 60)
    minutes = int(total_seconds // 60)
    total_seconds %= 60
    seconds = int(total_seconds)

    return days, hours, minutes, seconds


def validate_date(date_string):
    try:
        event_date = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
        current_date = datetime.now()
        if (event_date - current_date).days <= 365:
            return event_date
        else:
            print("Data introdusă trebuie să fie în decurs de un an!")
            return None
    except ValueError:
        print("Formatul datelor nu este corect!")
        return None


def main():
    event_date = None
    event_name = input("Introduceți numele evenimentului: ")
    while event_date is None:
        date_string = input("Introduceți data și ora evenimentului (dd/mm/YYYY HH:MM): ")
        event_date = validate_date(date_string)

    print("Calcularea timpului rămas până la evenimentul '{}'".format(event_name))
    while True:
        days, hours, minutes, seconds = calculate_time_remaining(event_date)
        print("{:02d} zile, {:02d} ore, {:02d} minute și {:02d} secunde au rămas până la evenimentul '{}'.".format(days, hours, minutes, seconds, event_name))
        time.sleep(1)

if __name__ == '__main__':
    main()