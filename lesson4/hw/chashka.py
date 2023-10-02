# ввод
q = int(input())

# обработка
if q % 10 == 1 and not (11 <= q <= 14):
    word = "чашка"
elif (q % 10 == 2 or q % 10 == 3 or q % 10 == 4) and not 11 <= q <= 14:
    word = "чашки"
else:
    word = "чашек"

# вывод
print(f"{q} {word}")
