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

    def __init__(self, video_name, is_published=True):
        self.name = video_name
        self.is_published = is_published

    def watch(self): # video_2
        self.views_count += 1

    def subscribe(self, human_object):
        self.subscribers = self.subscribers + [human_object]


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return self.name

# видео объекты
i_am_at_zoo = Video("Я в зоопарке")
video_2 = Video("Урок 16. Конструктор")

# объекты людей
asan = Human("Asan", 17)
janar = Human("Janar", 17)
bekzat = Human("Bekzat", 18)

# подписываемся
print(i_am_at_zoo.subscribers)
i_am_at_zoo.subscribe(asan)
i_am_at_zoo.subscribe(bekzat)
print(i_am_at_zoo.subscribers)

print(video_2.subscribers)
video_2.subscribe(janar)
video_2.subscribe(asan)
print(video_2.subscribers)


# print(i_am_at_zoo.views_count)
# i_am_at_zoo.views_count = 7
# print(i_am_at_zoo.views_count)
# i_am_at_zoo.views_count += 2
# print(i_am_at_zoo.views_count) # 9
# i_am_at_zoo.watch()
# print(i_am_at_zoo.views_count) # 10

video_2 = Video("Урок 16. Конструктор")
# print(video_2.views_count) # 0
# video_2.watch()
# print(video_2.views_count)

# secret_video = Video("Мои пароли", False)
# print(secret_video.is_published)
