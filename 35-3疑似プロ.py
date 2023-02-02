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

print(seiseki(x))
