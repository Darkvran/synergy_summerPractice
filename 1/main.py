import datetime, calendar

user_day = int(input("Enter the day of birth: "))
user_month = int(input("Enter the month of birth: "))
user_year = int(input("Enter the year of birth: "))

user_date = datetime.date(user_year, user_month, user_day)

def get_day_week(u_date):
    return calendar.day_name[u_date.weekday()]

def is_year_leap(u_date):
    return calendar.isleap(u_date.year)

def get_user_age(u_date):
    today = datetime.date.today()
    age = today.year - u_date.year
    if (today.month, today.day) < (u_date.month, u_date.day):
        age -= 1
    return age

def print_digital_date(u_date):
    sprites = {
        '0': ["***", "* *", "* *", "* *", "***"],
        '1': [" * ", "** ", " * ", " * ", "***"],
        '2': ["***", "  *", "***", "*  ", "***"],
        '3': ["***", "  *", "***", "  *", "***"],
        '4': ["* *", "* *", "***", "  *", "  *"],
        '5': ["***", "*  ", "***", "  *", "***"],
        '6': ["***", "*  ", "***", "* *", "***"],
        '7': ["***", "  *", "  *", "  *", "  *"],
        '8': ["***", "* *", "***", "* *", "***"],
        '9': ["***", "* *", "***", "  *", "***"],
        ' ': ["   ", "   ", "   ", "   ", "   "]
    }
    
    date_str = f"{u_date.day:02d} {u_date.month:02d} {u_date.year:04d}"
    
    for i in range(5):
        row = [sprites[char][i] for char in date_str]
        print(" ".join(row))

print(f"\nDay of week: {get_day_week(user_date)}")
print(f"Is leap year: {is_year_leap(user_date)}")
print(f"Age: {get_user_age(user_date)}\n")
print_digital_date(user_date)