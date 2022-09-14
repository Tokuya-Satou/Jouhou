def func1(kazu):
    kekka = 0
    for i in range(1, kazu+1):
        kekka = kekka + i
    return kekka

x = int(input('正の整数を入力 : '))

print('答えは', func1(x))
