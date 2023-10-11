def calc_average(k, *args):
    print(k)
    if args:
        average = sum(*args) / len(*args)
        return average

a = calc_average(17, [5, 6, 10]) # 7
print(a)

c = calc_average(23)
print(c)
