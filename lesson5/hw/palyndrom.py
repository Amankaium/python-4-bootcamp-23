# Напишите программу, которая проверяет, является ли введенная строка палиндромом.
# Палиндромом называется строка, которая читается одинаково слева направо и справа налево,
# игнорируя пробелы и регистр символов. Пример палиндрома: "А роза упала на лапу Азора".

txt = input()
formated = txt.replace(" ", "")
print(formated)
lower_case = formated.lower()
print(lower_case)

# 1
# reversed = lower_case[::-1]
# print(lower_case == reversed)

# 2
# i = 0
# is_palyndom = True
# while i < len(lower_case):
#     first = lower_case[i] # 1
#     last = lower_case[len(lower_case)-i-1] # последний
#     if first != last:
#         is_palyndom = False
#         print("Не палиндром")
#         break
#     i += 1
# print(is_palyndom)

# 3
txt = input()
print(txt.replace(" ", "").lower() == txt.replace(" ", "").lower()[::-1])
