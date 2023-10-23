from openpyxl import load_workbook

file_name = "students.xlsx"
excel = load_workbook(file_name)
page = excel["Лист1"]

commands = {
    "1": "Показать студентов",
    "2": "Показать оценки",
    "3": "Средняя оценка"
}

# ввод
print("Выберите команду:")
for key, value in commands.items():
    print(key, value)
input_value = input()

# обработка и вывод
# "Показать студентов"
if input_value == "1":
    for cell in page["A"]:
        if cell.row == 1:
            continue
        print(cell.value)

# Показать оценки
elif input_value == "2":
    for cell in page["B"]:
        if cell.row == 1:
            continue
        print(cell.value)

# Средняя оценка
elif input_value == "3":
    # 1
    sm = 0
    qty = 0
    for cell in page["B"]:
        if cell.row == 1:
            continue
        sm += cell.value
        qty += 1
    print(sm / qty)
    # 2
    marks = [cell.value for cell in page["B"] if cell.row != 1]
    print(sum(marks) / len(marks))
