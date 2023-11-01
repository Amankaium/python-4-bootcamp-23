from flask import Flask, render_template
from excel import ExcelFile

excel_object = ExcelFile("cups.xlsx")
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

@app.route("/cups/")
def cups_list():
    cup_names = excel_object.get_cup_names()
    cup_names = cup_names.split("\n")
    return render_template("cup_list.html", cup_names=cup_names)

@app.route("/cup/<number>")
def cup_detail(number):
    cup_info, img_path = excel_object.get_cup_info(number)
    return render_template("cup_detail.html", cup_info=cup_info, img_path=img_path)

app.run()
