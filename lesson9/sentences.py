# посчитать и вывести кол-во предложений в тексте

# Ввод:
# "Hello. My name is Kaium. I am python programmer."

# Вывод:
# 3

# 1
# txt = input()
# q = 0
# for s in txt:
#     if s in [".", '!', '?']:
#         q += 1
# print(q)

# 2
# txt = input() # "Hello. My name is Kaium. I am python programmer."
# sentences = txt.split(".") # ["Hello", "My name is Kaium",  "I am python programmer", ""]
# print(sentences)
# print(len(sentences)-1)

# 3
txt = input()
print(txt.count('.'))
