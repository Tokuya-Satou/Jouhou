# 素数判定
# 入力した整数が素数かどうかを判定するプログラム

import numpy

x = int(input('整数 = '))
tf = True

sqrtx = int(numpy.sqrt(x))

for i in range(2,sqrtx+1):
    if x%i == 0:
        print(str(x) + "は素数ではありません : " +str(x) +'=' + str(x//i) + ' / ' + str(i))
        tf = False
        break
    else:
        continue
if tf:
    print(str(x) + "は素数です")

    
