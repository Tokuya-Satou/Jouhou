# 誕生日検索　多分完成版
import datetime

# 1月1日から12月31日までのリストを作成
# 2004年なのは閏年のため(2月29日が欲しかったから)
first_day = datetime.date(2004,1,1)
l = [first_day + datetime.timedelta(days=i) for i in range(366)]

# 検索範囲の最大・最小・中間を確認
min_date_no = 0
max_date_no = 365
date_center = (min_date_no + max_date_no)//2

# 検索開始
str_r = str(input('あなたの誕生日は' + str("{0:%m月%d日}".format(l[date_center])) \
    + 'より前ですか？ (y/n/e)'))

# 誕生日が判るまで反復 : 'e'は「exactly（まさに!）」の意味
while min_date_no < max_date_no:
    if str_r == 'y':
        max_date_no = date_center -1
        date_center = (min_date_no + max_date_no)//2
        str_r = str(input(str("{0:%m月%d日}".format(l[date_center])) \
            + 'より前ですか？ (y/n/e)'))
    elif str_r == 'n':
        min_date_no = date_center +1
        date_center = (min_date_no + max_date_no)//2
        str_r = str(input(str("{0:%m月%d日}".format(l[date_center])) \
            + 'より前ですか？ (y/n/e)'))
    elif str_r =='e':
        break
    else:
        str_r = str(input('入力が正しくありません。あなたの誕生日は' \
            + str("{0:%m月%d日}".format(l[date_center])) \
                + 'より前ですか？ (y/n/e)'))
    print('min = ' + str("{0:%m月%d日}".format(l[min_date_no]))  \
        + ' / center = ' + str("{0:%m月%d日}".format(l[date_center])) + \
            ' / max = ' + str("{0:%m月%d日}".format(l[max_date_no])))

print('あなたの誕生日は' + str("{0:%m月%d日}".format(l[date_center])) + 'ですね。')
