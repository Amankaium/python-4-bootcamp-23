i = 0
while True:
    num = (input("Введите число (для завершения пропустите ввод): "))
    if num.isalpha():
        print("Введите корректные данные")
        continue
    if num == '':
        break
    sym = float(num)
    i += sym
    print(i)
