dct = {}
word = input().split()
for i in word:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
print(dct)