# センター試験2012 本試
# プログラム2
# (M) P (N) が2^N で割り切れるが、2^(N+1)で割り切れない

m = int(input('M='))
l = int(input('L='))

c=0

for n in range(1,l+1):
    x = 1
    for i in range(n):
        x = x*(m+i)
    k = 2*n
    if x-(x//k)*k == 0:
        k=2*k
        if x-(x//k)*k >0:
            c=c+1

print('求める個数は',c)
