num = {}
word = input("")
t = word.split(" ")
for i in t:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1
for key in num:
        print(key, num[key])    

print(num)
