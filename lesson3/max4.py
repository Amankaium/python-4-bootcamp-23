# найти максимум из 4 чисел
a = int(input()) # 4
b = int(input()) # 5
c = int(input()) # 9
d = int(input()) # 12

if a > c and a > b and a > d:  # False
    print(a) 
elif b > c and b > a and b > d: # False
    print(b)
elif c > a and c > b and c > d: # False
    print(c)
elif d > a and d > b and d > c: # True
    print(d)
