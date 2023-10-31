from flask import Flask
from excel import ExcelFile

excel_object = ExcelFile("cups.xlsx")
app = Flask(__name__)

@app.route("/")
def homepage():
    return '<a href="https://www.youtube.com/"> Клик сюда! </a>'

@app.route("/about/")
def about():
    return "Это сайт для продажи <b> кружек </b>"

@app.route("/contacts/")
def contacts():
    return """<b> Тел.: </b> 23534534534 <br>
        <b>email:</b> codify@gmail.com"""

@app.route("/cups/")
def cups_list():
    cup_names = excel_object.get_cup_names()
    # <br> - перенос строки
    response_str = cup_names.replace("\n", "<br>")
    return response_str # тип - строка

@app.route("/cup/<number>")
def cup_detail(number):
    cup_info, img_path = excel_object.get_cup_info(number)
    cup_info = cup_info.replace("\n", "<br>")
    return f"""{cup_info}
        <br>
        <img src='/static/{img_path}'/>
        """

app.run()
