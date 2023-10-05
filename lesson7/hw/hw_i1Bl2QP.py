counter = 'moroz i solnse , den chudesny. moroz - ne mojet byt chydesnym'
words = counter.split()
word_counter = {}

for word in words:
    if word in word_counter:
       word_counter[word] += 1
    else:
        word_counter[word] = 1

print(word_counter)
