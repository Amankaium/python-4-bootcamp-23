my_file = open("names.txt", mode='r', encoding='utf-8')

# row_1 = my_file.readline()
# print(row_1)
# print(type(row_1))

# row_2 = my_file.readline()
# print(row_2)

txt = my_file.read()
# print(txt)
names_list = txt.split()
print(names_list)
my_file.close()
