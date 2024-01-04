meibo = ['mizutani', 'ito','satou' ,'arai' ,'katou', 'ozawa' , 'irie', 'kawai1']
print ('ソート前',meibo)
flag = True
while flag:
    flag = False
    for i in range(len(meibo)-1):
        if meibo[i] > meibo[i + 1]:
            meibo[i], meibo[i + 1]=meibo[i + 1],meibo[i]
            flag = True
print('ソート後',meibo)