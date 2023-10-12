# 開始
# 文字列sを入力する
s = input("文字列を入力してください: ")

# 変数nにsの長さを代入する
n = len(s)

# 変数iを0に初期化する
i = 0

# 変数flagをTrueに初期化する
flag = True

# iがn/2未満か判定する
while i < n/2:
    # s[i]とs[n-i-1]が等しいか判定する
    if s[i] != s[n-i-1]:
        # flagをFalseに代入する
        flag = False
        # ループを抜ける
        break

    # iに1を加える
    i = i + 1

# flagがTrueか判定する
if flag:
    # sは回文であると出力する
    print(s, "は回文です。")
else:
    # sは回文でないと出力する
    print(s, "は回文ではありません。")
# 終了
