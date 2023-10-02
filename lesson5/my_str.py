word = "hello world!"

# обращение к символу
print(word[0])
print(word[1])

# обращение ко всем символам
i = 0
while i < len(word):
    print(word[i])
    i += 1

# перевод в список
lst = list(word)

# разделение по отступам
lst_2 = word.split()

# срез
print(word[6:11]) # world
print(word[6:]) # world!
print(word[:7]) # world!
print(word[:]) # hello world!
print(word[6:11:2]) # wrd
print(word[::2]) # hlowrd
print(word[::3]) # hlwl
print(word[::-1]) # !dlrow olleh

