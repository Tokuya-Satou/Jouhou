from tkinter import *
from tkinter import ttk

root = Tk()
root.title("はじめてのtkinter")

#オブジェクトの定義
label = ttk.Label(root,text ='Hello Python!')
entry = ttk.Entry(root)
button = ttk.Button(root,text = 'OK')

#レイアウト
label.pack()
entry.pack()
button.pack()

##ウィンドウの表示
root.mainloop()

