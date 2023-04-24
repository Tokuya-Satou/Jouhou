#----------------------足し算-------------------------------
import tkinter

root = tkinter.Tk()

root.geometry("250x250")

txt = tkinter.Entry(width=20)
txt.place(x=60, y=70)

txt1 = tkinter.Entry(width=20)
txt1.place(x=60, y=90)

def calc():
    a = txt.get()
    b = txt1.get()
    value = int(a)+int(b)
    
    result = tkinter.Label(text=value)
    result.place(x=60, y=110)

calc_button = tkinter.Button(text="今月の勉強時間(分)",command=calc)
calc_button.place(x=60, y=150)

root.mainloop()

#--------------------コンボボックス-------------------------
import tkinter
from tkinter import ttk
from tkinter import messagebox

    #ボタンが押された時の関数
def check_list():
    check = cb.get()
    messagebox.showinfo('結果', check)

#メイン画面を作成
window = tkinter.Tk()

#サイズを設定
window.geometry('300x200')

#タイトルの設定
window.title('Combo box')

#コンボボックスのリスト
list =['国語', '数学', '英語', '理科', '社会', '暗記', '課題',]

#コンボボックスを設置
cb = ttk.Combobox(window, values = list)
cb.pack(pady=50)

#コンボボックスのリストの先頭を表示
cb.set(list[0])

#ボタンを設置
btn = tkinter.Button(window, text='決定', command=check_list)
btn.place(x=140, y=100)

#画面表示
window.mainloop()