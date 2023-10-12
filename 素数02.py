
import numpy

x = 10000

prime =[]

print(str(x) + 'までの素数を表示')

for i in range(2, int(x+1)):
    sqrti = int(numpy.sqrt(i))
    tf = True
    for j in range(2, sqrti+1):
        if i%j ==0:
            tf = False
            break
    if tf:
        prime.append(i)

co = 0
for i in prime:
    co = co + 1
    if co%10 == 0:
        print(i)
    else:
        print(i, end='\t')
# print(prime)
