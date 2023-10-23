# import openpyxl
from openpyxl import load_workbook

file_name = "students.xlsx"
excel = load_workbook(file_name)
list_1 = excel["Лист1"]
# Добавить 2 имени и 2 оценки в excel файл
list_1["A2"] = "Bayaman"
list_1["B2"] = 77
list_1["A3"] = "Elnura"
list_1["B3"] = 99
excel.save(file_name)
