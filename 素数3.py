# 素数判定
# 入力した整数が素数かどうかを判定するプログラム

import numpy

x = int(input('整数 = '))
tf = True

for i in range(2,x):
    if x%i ==0:
        print(x,"は素数ではない")
        tf = False
        break
if tf:
    print(x,"は素数である")
