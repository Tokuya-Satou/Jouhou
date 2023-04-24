import tkinter

x = 0  

class Application( tkinter.Frame):
    def __init__( self,master ):
        super().__init__( master )
        self.master.geometry( "850x675")
        self.create_widget()

    def create_widget( self ):
            # ボタンを押したときの動作
        def check_list():
            check = int(self.ent1.get()) # + int(self.ent2.get())  # 勉強時間を足す
        #    messagebox.showinfo('合計', check)
            self.lbl1['text'] = check  #  勉強時間の合計をっ表示させる    
        
        self.label = tkinter.Label( self.master, text="月", font=("","20") )
        self.label.place( x=50, y=42 )
        
        self.label = tkinter.Label( self.master, text="火", font=("","20") )
        self.label.place( x=50, y=131 )
        
        self.label = tkinter.Label( self.master, text="水", font=("","20") )
        self.label.place( x=50, y=220 )
        
        self.label = tkinter.Label( self.master, text="木", font=("","20") )
        self.label.place( x=50, y=309 )
        
        self.label = tkinter.Label( self.master, text="金", font=("","20") )
        self.label.place( x=50, y=398 )
        
        self.label = tkinter.Label( self.master, text="土", font=("","20") )
        self.label.place( x=50, y=487 )
        
        self.label = tkinter.Label( self.master, text="日", font=("","20") )
        self.label.place( x=50, y=576 )
        
        self.module=("国語","数学","英語","理科","社会","暗記","課題")
        self.var=tkinter.StringVar(value=self.module)
        
        self.listbox_1 = tkinter.Listbox( self.master, font=("", "7"))
        self.listbox_1.place(x=175, y=42)
        self.listbox_1["listvariable"]=self.var
        self.listbox_1=tkinter.Listbox(width=50,height=10)
        
        self.listbox_2 = tkinter.Listbox( self.master, font=("", "7"))
        self.listbox_2.place(x=175, y=131)
        self.listbox_2["listvariable"]=self.var
        self.listbox_2=tkinter.Listbox(width=50,height=10)
        
        self.listbox_3 = tkinter.Listbox( self.master, font=("", "7"))
        self.listbox_3.place(x=175, y=220)
        self.listbox_3["listvariable"]=self.var
        self.listbox_3=tkinter.Listbox(width=50,height=10)
        
        self.listbox_4 = tkinter.Listbox( self.master, font=("", "7"))
        self.listbox_4.place(x=175, y=309)
        self.listbox_4["listvariable"]=self.var
        self.listbox_4=tkinter.Listbox(width=50,height=10)
        
        self.listbox_5 = tkinter.Listbox( self.master, font=("", "7"))
        self.listbox_5.place(x=175, y=398)
        self.listbox_5["listvariable"]=self.var
        self.listbox_5=tkinter.Listbox(width=50,height=10)
        
        self.listbox_6 = tkinter.Listbox( self.master, font=("", "7"))
        self.listbox_6.place(x=175, y=487)
        self.listbox_6["listvariable"]=self.var
        self.listbox_6=tkinter.Listbox(width=50,height=10)
        
        self.listbox_6 = tkinter.Listbox( self.master, font=("", "7"))
        self.listbox_6.place(x=175, y=576)
        self.listbox_6["listvariable"]=self.var
        self.listbox_6=tkinter.Listbox(width=50,height=10)
# ラベル・入力・ボタンの追加        
        self.lbl1 = tkinter.Label(text=x, font=('','55'),)  # ラベル
        self.lbl1.place(x=400, y=250)

        self.ent1 = tkinter.Entry(width=6)  # 勉強時間の入力1
        self.ent1.place(x=350, y=50)

        self.btn = tkinter.Button(self.master, text='決定', command=check_list)
        self.btn.place(x=200, y=200)

if __name__ == "__main__":
    root = tkinter.Tk()
    myapp = Application( master=root )
    myapp.mainloop()