# Создайте словарь с ключами:
# name
# last_name
# age
# 7 со значение 77
# code_language
# city

profile = {
    "name": "Kaium",
    "code": "python",
    1: 2,
    "age": 29,
    "companies": ["Beeline", "O!", "Aer", "RP"]
}
# выведите весь словарь
print(profile)

# Поменяйте все значения
# на число 3 и
# выведите весь словарь
for k in profile: # t - ключ
    profile[k] = 3
print(profile) 
