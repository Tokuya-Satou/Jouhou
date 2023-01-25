# センター試験2013 本試
# プログラム2
# 3進数を表示する その2 下の位から順に表示

import math

m = int(input('M='))

p = int(math.log10(m)/math.log10(3)) +1 

for i in range(1,p+1):
    print(m-(m//3)*3)
    m = m//3

