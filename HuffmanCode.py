# ハフマン符号化のアルゴリズムの勉強
import random

# 出現率の降順に並べ替える関数
# s = string, c = cnt を渡すこと
def sort(s,c, n):
    srcst = []
    srcnm = []
    for i in range(n):
        srcst.append(s[c.index(max(c))])
        srcnm.append(c[c.index(max(c))])
        del s[c.index(max(c))]
        del c[c.index(max(c))]
    return srcst,srcnm

# 2つのノードを結合
# s = string, c = cnt を渡すこと
def join(s,c):
    if len(s) < 2:
        return s,c
    else:
        stmp = [[s[-1], s[-2]]]
        ctmp = [c[-1]+c[-2]]
        return s[:-2] + stmp, c[:-2] + ctmp


bit =50 # int(input('文字数 = '))
n =5 # int(input('文字の種類(~26) : 何種類使用する ? = '))

# 符号化する文字列の作成/初期化 / char は最初の出力用
array = []
char = ""

# string = A~Z の文字を配列に格納
string = [chr(i + ord('A')) for i in range(n)]
# 文字数のカウント用配列の初期化
cnt = [0 for i in range(n)]

# 符号化する文字列の作成
for i in range(bit):
    k = random.randint(1,n)-1
    array.append(string[k])
    cnt[k] = cnt[k] +1

# 符号化する文字列の出力
for i in range(len(array)):
    char = char + array[i] + ' '
print('文字列 : ' , char, 'を符号化する')

# 文字列内の各文字の数を表示
print(str(string) ,'=' ,str(cnt))

srchst = string
srchnm = cnt

# ハフマン木の作成
while len(srchst) > 2:
    src = sort(srchst,srchnm,len(srchst))
    srchst = src[0]
    srchnm = src[1]
    print(srchst, srchnm)

    src = join(srchst,srchnm)
    srchst = src[0]
    srchnm = src[1]
    print(srchst, srchnm)

# ハフマン木の作成：幹の部分を [大、小に入れ替える]
if srchnm[0] < srchnm[1]:
    srchst[0], srchst[1] = srchst[1], srchst[0]
    srchnm[0], srchnm[1] = srchnm[1], srchnm[0]
print(srchst, srchnm)
