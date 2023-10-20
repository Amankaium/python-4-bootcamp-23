nums={
    1:'one', # 3
    2:'two', # 3
    3:'three', # 5
    4:'four', # 4
    5:'five',
    6:'six',
    7:'seven', # 5
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen', # 8
    15:'fifteen',
    18:'eighteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    }

# nums.get(5, )

def gen_num(n,dic):
    tmp=''
    t=str(n)

    if dic.get(n,False): #
        return dic[n]
    elif n<20:
        return dic[int(t[1])]+'teen'
    elif n<100:
        tmp=n-int(t[1])
        return dic[tmp]+dic[int(t[1])]
    elif n<1000:
        if t[1:3]=='00':
            return dic[int(t[0])]+'hundred'
        else:
            return dic[int(t[0])]+'hundredand'+gen_num(int(t[1:3]),nums)
    elif n==1000:
        return 'onethousand'

s=0
for i in range(1,1001):
    s+=len(gen_num(i,nums))
print(s)

# 113 # one hundred and thirteen # 21