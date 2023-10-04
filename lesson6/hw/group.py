
x = 1  
 
for i in range(1, 1000):  # 1000
    for j in range(1, 1000): # 1000
        mult = i * j  
        if str(mult) == str(mult)[::-1]: 
            if mult > x: 
                x = mult 
print(x)

# 1000 * 1000