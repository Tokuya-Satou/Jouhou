kakaku = [580, 970, 430, 820, 760]

saisyo = kakaku[0]

for x in kakaku:
    if x < saisyo:
        saisyo = x
        
print('最安値 : ', saisyo)