import requests
server_response = requests.get("https://jsonplaceholder.typicode.com/users")
# print(server_response.status_code)
data = server_response.json()
# print(data)
print(type(data))
# есть список словарей
# надо получить из него список имён
names = []
for element in data:
    names.append(element["name"])
# print(names)

# есть список имён
# надо его записать в файл
with open('users.txt', 'w') as users_file:
    for name in names:
        users_file.write(f"{name}\n")
