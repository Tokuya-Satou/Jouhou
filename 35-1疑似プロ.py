def sho(x,y):
    q = 0
    r = x
    while r >= y:
        r = r-y 
        q = q+1
    return q,r

x = int(input('割られる数 = '))
y = int(input('割る数 = '))

print('　商 : ',sho(x, y)[0])
print('余り : ',sho(x,y)[1])
