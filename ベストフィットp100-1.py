kion = [28.6, 28.8, 28.9, 29.0, 29.2, 29.3, 29.4, 29.5, \
    29.6, 29.8, 29.9, 30.0, 30.1, 30.2, 30.3, 30.4, 30.5,\
    30.6, 30.7, 30.9, 31.0, 31.1, 31.2, 31.4, 31.5, 31.7, \
    31.8, 32.0, 32.1, 32.2, 32.3, ]

manatubi = 0
goukei = 0

for x in kion:
    if x> 30.0:
        goukei = goukei + x
        manatubi = manatubi + 1

print('真夏日の日数 : ', manatubi, '真夏日平均 : ', goukei/manatubi)