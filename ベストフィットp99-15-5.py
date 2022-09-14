def func5(kazu):
    if kazu == 0:
        return 1
    return kazu * func5(kazu -1)

x = int(input('正の整数を入力 : '))
print('答えは', func5(x))
