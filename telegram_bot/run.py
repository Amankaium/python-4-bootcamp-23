from bot_class import TelegramBot

token = "6450383163:AAHb6Do-tMkORRBWdQjAyZrXyWyq1-1teC0"
chat_id = "270623373" # Kaium chat id

if __name__ == "__main__":
    
    bot = TelegramBot(token)
    # bot.send_message(chat_id, "hello from bot oop")

    # bot.sync_chats()
    # bot.spam("test Kaium")

    # file_name = "test_1.xlsx"
    # bot.create_chats_excel(file_name)
    # print(bot.get_chats_excel())

    # photo_url = "https://leonardo.osnova.io/5569a907-bbcf-5657-9fcb-a472aa78165f/-/preview/2100/-/format/webp/"
    # bot.send_photo(chat_id, photo_url)

    # sticker_id = "CAACAgQAAxkBAAOxZTifRgh2rKwhEw_8lRgentV21k0AAukAA7nRqgGxhH8Un915vTAE"
    sticker_id = "CAACAgQAAxkBAAEKmSFlOJ9rYW2YD6wLiYjwiWH38TcxigAC6QADudGqAbGEfxSf3Xm9MAQ"
    sticker_id = "CAACAgIAAxkBAAEKmSplOJ-X2wNVuEjNliel0H3dw3s_UQACtAAD9wLID2Uu3kpwpiGRMAQ"
    # sticker_id = "AAMCBAADGQEAA7FlOJ9GCHasrCETD_yVGB6e1XbWTQAC6QADudGqAbGEfxSf3Xm9AQAHbQADMAQ" # не работает 
    # sticker_id = "AQAD6QADudGqAXI" # тоже не работает 
    bot.send_sticker(chat_id, sticker_id)
