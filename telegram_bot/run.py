from bot_class import TelegramBot

token = "6450383163:AAHb6Do-tMkORRBWdQjAyZrXyWyq1-1teC0"
bot = TelegramBot(token)

chat_id = "270623373" # Kaium chat id
# bot.send_message(chat_id, "hello from bot oop")

# bot.sync_chats()
# bot.spam("test Kaium")

# file_name = "test_1.xlsx"
# bot.create_chats_excel(file_name)
# print(bot.get_chats_excel())

photo_url = "https://leonardo.osnova.io/5569a907-bbcf-5657-9fcb-a472aa78165f/-/preview/2100/-/format/webp/"
bot.send_photo(chat_id, photo_url)
