x = int(input('整数を入力 : '))
flag = False
for  i in range(2,x):
    if x % i ==0:
        flag = True
        break
if flag:
    print('no')    
else:
    print('yes')
        

