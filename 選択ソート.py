# 実教教科書 p140 選択法による整列
# 配列 a を昇順で並び変える。

a=[88,43,25,37,51,101,1,45,20]

print(a)

# 配列の左側から選択していく
for i in range(0,len(a)):
    tmp = a[i]
    tmp_no = 0
# 最小値とその列番号を記録
    for j in range(i,len(a)):
        if tmp >= a[j]:
            tmp = a[j]
            tmp_no = j
# 記録した数値と現在の数字を入れ替える
    print(i,'番目の',a[i],'と',tmp_no,' 番目の',tmp,'を入れ替えます')        
    a[tmp_no] = a[i]
    a[i] = tmp
    print(a)
