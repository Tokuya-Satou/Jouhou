# センター試験2014 本試
# プログラム2
# N! の素因数の個数を数えるプログラム

n = int(input('N='))

for d in range(2,n):
    # d が素数か合成数かの確認
    ir = 0
    for k in range(2,d-1):
        if d == (d//k)*k:
            ir = 1
            break
    # d が合成数の時に　ir=1 となり、スキップ
    if ir == 1:
        continue

    c=0
    m=n

    for j in range(1,n):
        m=m // d
        c=c+m
        if m<d :
            #print('繰り返しの回数(j)は',j)
            break
    print('素因数',d,'は',c,'個')

