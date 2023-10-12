# создать функцию, которая принимает словарь,
# и возвращает список из значений
# Пример:
# info = {"address": "Isanova 103", "floors": 7, "has_parking": True}
# convert(info) # возвращает ["Isanova 103", 7, True] 

def convert(d):
    res = []
    for key in d:
        res.append(d[key])
    return res


info = {"address": "Isanova 103", "floors": 7, "has_parking": True}
r = convert(info)
print(r)
