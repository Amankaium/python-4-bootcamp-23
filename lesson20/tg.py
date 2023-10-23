import requests

url = "https://api.telegram.org/bot6450383163:AAHb6Do-tMkORRBWdQjAyZrXyWyq1-1teC0/"

# получение обновлений (последние сообщения)
# response = requests.get(f"{url}getUpdates")
# data = response.json()
# print(data["result"][-1]["message"]["text"])

# отправка сообщений
chat_id = 6681383056
text = "Привет, Эльдияр!"
requests.get(f"{url}sendMessage?chat_id={chat_id}&text={text}")
