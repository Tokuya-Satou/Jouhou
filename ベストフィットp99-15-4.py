def func4(kazu):
    kekka = []
    for i in range(1, kazu + 1):
        if kazu % i == 0:
            kekka.append(i)
    return kekka

x = int(input('正の整数を入力 : '))
print('答えは', func4(x))
