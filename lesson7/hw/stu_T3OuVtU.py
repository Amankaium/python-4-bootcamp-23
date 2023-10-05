txt = input("Введите текст: ")
 
words = txt.split() 
 
word_txt = {} 
 
for word in words: 
    if word in word_txt: 
        word_txt[word] += 1 
    else: 
        word_txt[word] = 1 
 
print("Результат подсчета слов:") 
for word, count in word_txt.items(): 
    print(f"{word}: {count}")