nums = [-5, 81, 32, -62]
profile = {
    "name": "Kaium",
    "code": "python",
    1: 2,
    "age": 29,
    "companies": ["Beeline", "O!", "Aer", "RP"]
}
profile_lst = ["Kaium", "python", 2, 29]

print(profile)

# обращение к элементу
print(profile["age"]) # 29 # "age" - ключ, 29 - значение

# добавление
profile["last_name"] = "Amanbaev" # "last_name" - ключ

# изменение
profile[1] = 7 # 1 - ключ, 7 - новое значение

print(profile)

for t in profile: # t - ключ
    print(t, profile[t])
