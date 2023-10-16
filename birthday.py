from datetime import datetime


users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
         {"name": "Maryna Rolik", "birthday": datetime(1983, 10, 19)},
         {"name": "Inav Tirchak", "birthday": datetime(1989, 9, 11)},
         {"name": "Roman Davydiv", "birthday": datetime(1989, 10, 19)},
         {"name": "Natalia Atroshenko", "birthday": datetime(1963, 10, 18)},
         {"name": "Turchak Narkiyan", "birthday": datetime(2013, 10, 16)}]


def get_birthdays_per_week(users):
    week_day = {"Monday": [], "Tuersday": [], "Wednesday": [], 'Thursday': [],
                 "Friday": []}
    today = datetime.today().date()
        
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        
        if delta_days < 7:
            weekday = birthday_this_year.weekday()
            if weekday in [0, 5, 6]:
                week_day["Monday"].append(name)
            elif weekday == 1:
                week_day["Tuersday"].append(name)
            elif weekday == 2:
                week_day["Wednesday"].append(name)
            elif weekday == 3:
                week_day["Thursday"].append(name)
            elif weekday == 4:
                week_day["Friday"].append(name)

    for key, value in week_day.items():
        if value != []:
            print(f"{key}: {', '.join(value)}")


get_birthdays_per_week(users)
