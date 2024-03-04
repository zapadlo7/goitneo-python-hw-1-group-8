from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Поточна дата
    today = datetime.today().date()

    # Словник для зберігання днів народження користувачів за днем тижня
    birthdays_per_week = defaultdict(list)

    # Проходимо по кожному користувачу
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертація Дати

        # Оцінка Дати на Цей Рік
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:  # Якщо день народження вже був цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Переносимо день народження з суботи або неділі на понеділок
        if birthday_this_year.weekday() in [5, 6]:  # 5 - субота, 6 - неділя
            birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

        # Порівняння з Поточною Датою
        delta_days = (birthday_this_year - today).days

        # Додаємо користувача до відповідного дня тижня
        if delta_days < 7:  # Якщо день народження в наступних 7 днях
            birthday_weekday = birthday_this_year.strftime("%A")
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
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 3)},
    {"name": "Jill Valentine", "birthday": datetime(1955, 3, 4)},
    {"name": "Jan Koum", "birthday": datetime(1984, 3, 5)},
    {"name": "Kim Kardashian", "birthday": datetime(1975, 3, 9)}
]

get_birthdays_per_week(users)
