from flask import Flask
from excel import ExcelFile

excel_object = ExcelFile("cups.xlsx")
app = Flask(__name__)

@app.route("/")
def homepage():
    return 'Hello world'

@app.route("/about/")
def about():
    return "Это сайт для продажи <b> кружек </b>"

@app.route("/cups/")
def cups_list():
    cup_names = excel_object.get_cup_names()
    # <br> - перенос строки
    response_str = cup_names.replace("\n", "<br>")
    return response_str # тип - строка

app.run()
