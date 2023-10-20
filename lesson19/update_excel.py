from openpyxl import load_workbook

excel_file = load_workbook("users_table.xlsx")
page = excel_file["Sheet"]

# чтение
print(page["A7"].value)

# добавление
page["A11"] = "Жанар Айылчиев"
excel_file.save("users_table.xlsx")
