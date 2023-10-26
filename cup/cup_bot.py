import telebot
from time import sleep
from excel import ExcelFile

TOKEN = "6450383163:AAHb6Do-tMkORRBWdQjAyZrXyWyq1-1teC0" # свой токен
chat_id = "270623373" # свой id чата
tb = telebot.TeleBot(TOKEN)
excel_object = ExcelFile("cups.xlsx")


while True:
    print("updating...")

    # синхронизация сообщений
    matrix = []
    for update in tb.get_updates():
        matrix.append([
            update.update_id,
            update.message.text,
        ])    
    excel_object.write_cells("messages", matrix)

    # обработка сообщений
    messages = excel_object.get_messages()
    cup_names = excel_object.get_cup_names()
    cup_numbers = excel_object.get_cup_numbers()
    for message, value in messages.items():
        if value["status"] != "+":
            if value["text"] == "/list":
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                lst = []
                for number in cup_numbers:
                    btn = telebot.types.KeyboardButton(number)
                    lst.append(btn)
                markup.add(*lst)
                tb.send_message(chat_id, cup_names, reply_markup=markup)
            elif value["text"] in cup_numbers:
                cup_info, img_path = excel_object.get_cup_info(value["text"])
                tb.send_message(chat_id, cup_info)
                with open(img_path, 'rb') as img_file:
                    tb.send_photo(chat_id, img_file)
            value["status"] = "+"

    
    # сохраняем сообщения
    excel_object.update_messages(messages)
    sleep(3)
