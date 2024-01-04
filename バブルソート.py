num = [9, 3, 6,1]
print(num)

for i in range(len(num)-1,0 ,-1):
    for j in range(i):
        if num[j] > num[j+ 1]:
            num[j], num[j + 1]=num[j + 1], num[j]
        print(num)

