# センター試験2014 本試
# プログラム1
# N! の素因数のうち d の個数を数えるプログラム

n = int(input('N='))

d=2
c=0
m=n

for j in range(1,n):
    m=m // d
    c=c+m
    if m<d :
        print('繰り返しの回数(j)は',j)
        break
print('素因数',d,'は',c,'個')
