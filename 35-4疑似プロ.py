def sum(n):
    x = 0
    for i in range(n+1):
        x = x + i
    return x

x = int(input('整数 = '))

print('1から',x,'までの和 = ',sum(x))
