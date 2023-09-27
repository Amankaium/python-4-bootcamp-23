a = int(input())    # 5
sym = input()       # **
b = int(input())    # 3

if sym == "+":      # X # False
    c = a + b       # X
elif sym == "*":    # X
    c = a * b       # X
elif sym == "/":    # X
    c = a / b       # X
elif sym == "**":   # V # True
    c = a ** b      # V
elif sym == "-":    # X
    c = a - b       # X
else:               # X
    c = "Error!"    # X
print(c)            # 125
