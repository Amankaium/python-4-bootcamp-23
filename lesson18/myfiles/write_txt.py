# with open("names.txt", "w", encoding='utf-8') as my_txt_file:
with open("names.txt", "a", encoding='utf-8') as my_txt_file:
    # txt = my_txt_file.read() # работает только в режиме "r"
    # print(txt)
    my_txt_file.write("Ivan\n")
    my_txt_file.write("Asan\n")
