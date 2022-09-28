# 選択ソート
Num = [8,5,2,4]
print(Num)
for i in range(len(Num)-1):
    min_i = i
    for j in range(i,len(Num)):
        if Num[j] < Num[min_i]:
            min_i=j
    Num[i], Num[min_i] = Num[min_i], Num[i]
    print(Num)