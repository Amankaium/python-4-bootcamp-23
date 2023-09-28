print("Здравствуйте, напишите Ваш рейтинг от 0 до 100")
a = int(input("Владение Python:"))
if a < 0 or a > 100:
    print("Ошибка")
b = int(input("Владение базами данных:"))
if b < 0 or b > 100:
    print("Ошибка")
c = int(input("Владение Django:"))
if c < 0 or c > 100:
    print("Ошибка")
pyt = a * 5
based = b * 4
dj = c * 3
summa = pyt + based + dj
print(f"Рейтинг- {summa}")
if summa >= 1000 and summa <= 1200:
    print("Вы нам подходите")
elif summa >= 500 and summa < 1000:
    print("Мы с вами свяжемся")
elif summa < 500:
    print("К сожалению, вы не прошли")
else:
    print("Error")

