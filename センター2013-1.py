# センター試験2013 本試
# プログラム1
# 3進数を表示する その１ 上の位から順に表示

import math

n = int(input('N='))

p = int(math.log10(n)/math.log10(3)) +1 
x = 3**(p-1)

for i in range(1,p+1):
    print(int(n/x))
    n = n -int (n/x)*x
    x = x/3
