def func2(kazu):
    kekka = 1
    for i in range(kazu, 0, -1):
        kekka = kekka * i
    return kekka

x = int(input('正の整数を入力 : '))

print('答えは', func2(x))