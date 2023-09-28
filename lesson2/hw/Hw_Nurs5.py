print("Введите количество баллов от 0 до 100")
py = int(input("Владение python: "))
datb = int(input("Владение базами данных: "))
dj = int(input("Владение  django: "))

if py and datb and dj <= 100 and py and datb and dj > 0:
    rat = (py * 5) + (datb * 4) + (dj * 3)
    if rat <= 1200 and rat >= 1000:
        message = "Вы нам подходите"
    elif rat <= 1000 and rat >= 500:
        message = "Мы с вами свяжемся"
    else:
        message = "К сожалению, вы не прошлии"
    print(f"Рейтинг - {rat}")
    print(message)
else:
    print("Пожалуйста, введите корректные показатели от 0 до 100.")