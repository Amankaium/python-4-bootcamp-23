
baya = input("Введите текст: ") 
 
words = baya.split() 
 
word_baya = {} 
 
for word in words: 
    if word in word_baya: 
        word_baya[word] += 1 
    else: 
        word_baya[word] = 1 
 
print("Результат подсчета слов:") 
for word, count in word_baya.items(): 
    print(f"{word}: {count}")