# 実教教科書 p144 二分探索のプログラム改

a= [1, 20, 25, 37, 43, 45, 51, 88, 101]
n=len(a)

print('番号','\t','データ')
for i in range(0,n):
    print(i,'\t',a[i])
print('')

s= int(input('探索値の入力 : '))

i=0; j=n-1

while i <= j:
    m=int((i+j)/2)
    if a[m] == s:
        print(s,'は',m,'番目に存在')
        break
    elif a[m]>s:
        print(s,'は',m,'番目から',j+1,'番目にはありません')
        j=m-1
    else:
        print(s,'は',i,'番目から',m,'番目にはありません')
        i=m+1
