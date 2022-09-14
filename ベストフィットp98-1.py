kuku = [[0] *9 for i in range(9)]

for dan in range(9):
    for kazu in range(9):
        kuku[dan][kazu] = (dan+1)*(kazu+1)
    # (1) -2 の解答
    print(kuku[dan])

