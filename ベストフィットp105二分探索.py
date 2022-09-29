import numbers


NO_DATA = -999
def tansaku2(hairetsu, sagasu, start, end, kaisu):
    kaisu = kaisu +1
    if start > end:
        return NO_DATA, kaisu

    tmp = start + (end - start)//2
    if sagasu < hairetsu[tmp]:
        tmp, kaisu = tansaku2(hairetsu, sagasu, start, tmp-1, kaisu)
    elif sagasu > hairetsu[tmp]:
        tmp, kaisu = tansaku2(hairetsu, sagasu, tmp+1, end, kaisu)
    else:
        return tmp, kaisu
    return tmp, kaisu

numbers = []

for i in range(0,365,1):
    numbers.append(i)

num = int(input('探す数?'))
ans, cnt = tansaku2(numbers, num, 0, len(numbers)-1,0)
print(ans, '番目・探索回数',cnt)