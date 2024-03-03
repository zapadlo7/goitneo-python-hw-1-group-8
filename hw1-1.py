from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = datetime.today().date()

    # Створюємо словник для зберігання днів народження користувачів за днем тижня
    birthdays_per_week = defaultdict(list)

    # Проходимо по кожному користувачу
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date

        # Оцінюємо дату на цей рік
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:  # Якщо день народження вже був цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Порівнюємо з поточною датою
        delta_days = (birthday_this_year - today).days

        # Визначаємо день тижня
        if delta_days < 7:  # Якщо день народження в наступному тижні
            birthday_weekday = birthday_this_year.strftime("%A")
            # Користувачів, у яких день народження був на вихідних, привітати в понеділок
            if birthday_weekday in ["Saturday", "Sunday"]:
                birthday_weekday = "Monday"
            # Додаємо користувача до відповідного дня тижня
            birthdays_per_week[birthday_weekday].append(name)

    # Виводимо список користувачів, яких потрібно привітати на наступному тижні
    next_week = today + timedelta(days=(7 - today.weekday()))
    print("Користувачі, яких потрібно привітати на наступному тижні:")
    for day in range(7):
        next_day = next_week + timedelta(days=day)
        day_of_week = next_day.strftime("%A")
        if birthdays_per_week[day_of_week]:
            print(f"{day_of_week}: {', '.join(birthdays_per_week[day_of_week])}")
        

# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 9)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 3, 4)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 3, 3)},
    {"name": "Kim Kardashian", "birthday": datetime(1975, 3, 7)}
]

get_birthdays_per_week(users)
