# найти и вывести первую цифру
txt = input() # he!llo! 1 !world!

i = 0
while i < len(txt):
    sym = txt[i]
    i += 1
    if sym == "!":
        continue
    if sym.isdigit(): # True если 1
        print(sym)
        break
    print(sym)
    
