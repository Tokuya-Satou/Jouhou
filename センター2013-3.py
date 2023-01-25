# センター試験2013 本試
# プログラム3
# 3進数を表示する その３
# 3進表示とそれを逆に並べた列が一致するかどうかを調べる
# 例 : 202_(10) = 21111_(3) なので'一致しない'
#      203_(10) = 21112_(3) なので'一致する'と出力

import math

n = int(input('N='))

p = int(math.log10(n)/math.log10(3)) +1 
x = 3**(p-1)
ch = 0

m = n

for i in range(1,p//2+1):
    a = n//x
    n = n -(n//x)*x
    x = x/3
    b = m -(m//3)*3
    m = m//3
    if not a == b:
        print('一致しない')
        ch = 1
        break

if ch ==0:
    print('一致する')

