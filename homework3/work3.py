from datetime import datetime

def user():
    birthdatestr = input("Введите вашу дату рождения (дд/мм/гггг): ")

    try:
        birthdate = datetime.strptime(birthdatestr, '%d/%m/%Y')
    except ValueError:
        print("Неверно. Пожалуйста, введите в формате дд/мм/гггг.")
        return
    
    today = datetime.today()
    year = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        year -= 1

    if year % 10 == 1 and year % 100 != 11:
        word = "год"
    elif 2 <= year % 10 <= 4 and not (12 <= year % 100 <= 14):
        word = "года"
    else:
        word = "лет"

    print(f"Ваш возраст: {year} {word}")

user()
