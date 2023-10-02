# message = "Hello, how are you?" # str
message = input() # str

# вариант 1
i = 0
counter = 0 # счётчик слов
while i < len(message):
    sym = message[i] # str
    if sym == " ":
        counter += 1
    i += 1
counter += 1
print(counter)

# вариант 2
lst = message.split()
print(len(lst))