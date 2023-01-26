# センター試験2012 本試
# プログラム1
# (M) P (N) が8で割り切れるか
m = int(input('M='))
n = int(input('N='))

x = 1

for i in range(n):
    x = x*(m+i)

if x -(x//8)*8 == 0:
    print('8で割り切れます')
else:
    print('8で割り切れません')

