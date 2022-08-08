# 実教教科書 p142 線形探索のプログラム

a=[88,43,25,37,51,101,1,45,20]

n=len(a)

print('番号','\t','データ')
for i in range(0,n):
    print(i,'\t',a[i])
print('')

s= int(input('探索値の入力 : '))

for i in range(0,n):
    if a[i] == s:
        print(s,'は',i,'番目に存在します')
        break
    else:
        print(s,'は',i,'番目までにはありません')
