def seiseki(ten):
    if ten >= 90:
        hyoka = 'S'
    elif ten >= 70:
        hyoka = 'A'
    elif ten >= 50:
        hyoka = 'B'
    elif ten >= 30:
        hyoka = 'C'
    else:
        hyoka = 'D'
    return hyoka

x = int(input('あなたの得点 = '))

while x < 0 or x>100:
    x = int(input('もう一度入力してください \nあなたの得点 = '))

print(seiseki(x))
