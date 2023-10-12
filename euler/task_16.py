def sum_pow(num, pow):      # создаётся функция sum_pow, num и pow - аргументы
    res = num ** pow        # 32768
    res_str = str(res)      # '32768'
    res_sum = 0
    for num in res_str:     # '32768'
        int_num = int(num)  # 3
        res_sum += int_num
    return res_sum

print(sum_pow(2, 15))
print(sum_pow(2, 1000))
