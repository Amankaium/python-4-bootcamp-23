import telebot

TOKEN = "6450383163:AAHb6Do-tMkORRBWdQjAyZrXyWyq1-1teC0" # свой токен
chat_id = "270623373" # свой id чата
tb = telebot.TeleBot(TOKEN)	

with open('my_img.jpg', 'rb') as photo: # свой путь к файлу
    tb.send_photo(chat_id, photo)
