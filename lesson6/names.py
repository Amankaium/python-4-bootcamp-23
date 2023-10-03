# Вам даётся список имён
names_lst = ["Steve", "Tom", "Bruce"]
# Надо вывести текст к каждому имени:
# "he is Steve"
# "he is Tom"
# ...
for i in range(len(names_lst)):
    print(f"he is {names_lst[i]}")

for name in names_lst:
    print(f"he is {name}")
