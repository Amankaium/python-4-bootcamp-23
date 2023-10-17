# Создайте класс Video со свойствами: 
# просмотры - 0 
# likes = 100
# subscribers = [ ]
# is_published = True
# и методом subscribe, который выводит текст "Вы успешно подписаны"

class Video:
    views_count = 0
    likes = 100
    subscribers = []
    is_published = True

    def subscribe(self):
        print("Вы успешно подписаны")

i_am_at_zoo = Video()
print(i_am_at_zoo.likes)
i_am_at_zoo.subscribe()
