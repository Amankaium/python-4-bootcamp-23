vvod = input("Введите текст: ")

words = vvod.split()

word_vvod = {}

for word in words:
    if word in word_vvod:
        word_vvod[word] += 1
    else:
        word_vvod[word] = 1

print("Результат подсчета слов:")
for word, count in word_vvod.items():
    print(f"{word}: {count}")
