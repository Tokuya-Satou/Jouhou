import tkinter
from tkinter import ttk
from tkinter import messagebox

def check_list():
    check = int(ent1.get()) + int(ent2.get())  # 勉強時間を足す
#    messagebox.showinfo('合計', check)
    lbl1['text'] = check  #  勉強時間の合計をっ表示させる

#メイン画面を作成
window = tkinter.Tk()

#サイズを設定
window.geometry('800x600')

#タイトルの設定
window.title('Combo box')

#コンボボックスのリスト
list =['国語', '数学', '英語', '理科', '社会', '暗記', '課題',]

#コンボボックスを設置
cb1 = ttk.Combobox(window, values = list)
cb1.pack(pady=10)
cb1.place(x=100, y=50)

cb2 = ttk.Combobox(window, values = list)
cb2.place(x=230, y=50)
cb2.pack(pady=50)

cb3 = ttk.Combobox(window, values = list)
cb3.place(x=250, y=50)
cb3.pack(pady=20)

# 勉強時間の合計
x = 0  #　初期値
lbl1 = ttk.Label(text=x, font=('','55'),)  # ラベル
lbl1.place(x=400, y=250) 

ent1 = ttk.Entry(width=6)  # 勉強時間の入力1
ent1.place(x=250, y=50)


ent2 = ttk.Entry(width=6)  # # 勉強時間の入力2
ent2.place(x=550, y=50)

#コンボボックスのリストの先頭を表示
cb1.set(list[1])
cb2.set(list[0])
#cb3.set(list[3])

#ボタンを設置
btn = tkinter.Button(window, text='決定', command=check_list)
btn.place(x=200, y=200)

#画面表示
window.mainloop()