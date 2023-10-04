counter = {}
# {
#   "cup": 7,
#   "python" 3,
# }

while True:
    word = input() # hello
    if word == "end":
        break
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
print(counter)
