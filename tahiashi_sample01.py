import tkinter

x = "7000"

class Application(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master = None)
        self.master.geometry("800x600")
        self.create_widget()

    def create_widget(self):
        self.Label_1 = tkinter.Label( self.master, text='今月の', font=('','30'),) #文字
        self.Label_1.place(x=45, y=25)
        self.Label_2 = tkinter.Label( self.master, text='使える金額', font=('','30'),)
        self.Label_2.place(x=45, y=65)
        self.Label_3 = tkinter.Label( self.master, text=x, font=('','55'),) # 文字大きく #金額固定
        self.Label_3.place(x=320, y=60)
        self.Label_4 = tkinter.Label( self.master, text='円', font=('','45'),)
        self.Label_4.place(x=500, y=60)
        self.Label_5 = tkinter.Label( self.master, text='円', font=('','18'),)
        self.Label_5.place(x=420, y=200)
        self.Label_6 = tkinter.Label( self.master, text='消費額', font=('','18'),)
        self.Label_6.place(x=80, y=200)

        def btn_click():
            num_1 = int(x)
            num = int(txt_1.get())
            num_sum = num_1 -num
            txt_1.delete(0, tkinter.END)
            self.Label_3['text'] = num_sum

        self.button = tkinter.Button(self.master, text='OK', command=btn_click) # テキストボックスのボタン
        self.button.place(x=480, y=200)

        txt_1 = tkinter.Entry(width = 30) # テキストボックス
        txt_1.place(x=200, y=210)

        txt_1.insert(0, 7000)

if __name__ == '__main__':
    root = tkinter.Tk()
    myapp = Application(master=root)
    myapp.mainloop()

