sym_kv = 0
kv_sym = 0
for i in range(0, 101):
    sym_kv += i ** 2
    kv_sym += i
    kv_sym1 = (kv_sym ** 2)
dif = kv_sym1 - sym_kv
print(dif)