# from random import randint
from openpyxl import load_workbook

# a = randint(2, 10)
# print(a)

excel_file = load_workbook("students.xlsx")
page = excel_file["Лист1"]

end_row = len(page["A"]) # 7
for i in range(2, end_row + 1): # 8
    mark_1 = page[f"E{i}"].value # page["E2"]
    mark_2 = page[f"F{i}"].value
    mark_3 = page[f"G{i}"].value
    mediana = (mark_1 + mark_2 + mark_3) / 3
    page[f"H{i}"] = mediana
excel_file.save("students.xlsx")