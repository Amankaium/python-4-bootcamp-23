summa = 0
summa2 = 0
for a in range(1, 101):
    summa = (a ** 2) + summa            
    summa2 = a + summa2
summa3 = int(summa2) ** 2
raz = summa3 - summa
print(raz)
        
        

    
       
