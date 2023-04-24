import tkinter
from tkinter import ttk

x = 0  

class Application( tkinter.Frame):
    def __init__( self,master ):
        super().__init__( master )
        self.master.geometry( "850x675")
        self.create_widget()

    def create_widget( self ):
            # ボタンを押したときの動作
        def check_list():
            check = int(self.ent1.get()) + int(self.ent2.get()) + int(self.ent3.get()) + int(self.ent4.get()) + int(self.ent5.get()) + int(self.ent6.get()) + int(self.ent7.get())  # 勉強時間を足す
        #    messagebox.showinfo('合計', check)
            self.lbl1['text'] = check#  勉強時間の合計を表示させる    
        #    self.lbl2['text'] = check 
        #    self.lbl3['text'] = check
        #    self.lbl4['text'] = check
        #    self.lbl5['text'] = check
        #    self.lbl6['text'] = check
        #    self.lbl7['text'] = check
            
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
        
        self.label = tkinter.Label( self.master, text="今日の勉強時間", font=("","15") )
        self.label.place( x=550, y=42 )
        
        self.label = tkinter.Label( self.master, text="今日の勉強時間", font=("","15") )
        self.label.place( x=550, y=131 )
        
        self.label = tkinter.Label( self.master, text="今日の勉強時間", font=("","15") )
        self.label.place( x=550, y=220 )
        
        self.label = tkinter.Label( self.master, text="今日の勉強時間", font=("","15") )
        self.label.place( x=550, y=309 )
        
        self.label = tkinter.Label( self.master, text="今日の勉強時間", font=("","15") )
        self.label.place( x=550, y=398 )
        
        self.label = tkinter.Label( self.master, text="今日の勉強時間", font=("","15") )
        self.label.place( x=550, y=487 )
        
        self.label = tkinter.Label( self.master, text="今日の勉強時間", font=("","15") )
        self.label.place( x=550, y=576 )
        
        self.label = tkinter.Label( self.master, text="(分間)", font=("","15") )
        self.label.place( x=770, y=612 )
        
        self.module=("国語","数学","英語","理科","社会","暗記","課題")
        self.var=tkinter.StringVar(value=self.module)
        
        self.combobox = ttk.Combobox( self.master, values = self.module)
        self.combobox.place(x=175, y=42)
#        self.listbox_1 = tkinter.Listbox( self.master, font=("", "7"))
#        self.listbox_1.place(x=175, y=42)
#        self.listbox_1["listvariable"]=self.var
#        self.listbox_1=tkinter.Listbox(width=50,height=10)
        
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
        self.lbl1 = tkinter.Label(text=x, font=('','60'),)  # ラベル
        self.lbl1.place(x=725, y=530)

        self.ent1 = tkinter.Entry(width=6)  # 勉強時間の入力1
        self.ent1.place(x=600, y=80)
        
        self.ent2 = tkinter.Entry(width=6)
        self.ent2.place(x=600, y=169)
        
        self.ent3 = tkinter.Entry(width=6)
        self.ent3.place(x=600, y=258)
        
        self.ent4 = tkinter.Entry(width=6)
        self.ent4.place(x=600, y=347)
        
        self.ent5 = tkinter.Entry(width=6)
        self.ent5.place(x=600, y=436)
        
        self.ent6 = tkinter.Entry(width=6)
        self.ent6.place(x=600, y=525)
        
        self.ent7 = tkinter.Entry(width=6)
        self.ent7.place(x=600, y=614)

        self.btn = tkinter.Button(self.master, text='今週の勉強時間', command=check_list)
        self.btn.place(x=723, y=500)

if __name__ == "__main__":
    root = tkinter.Tk()
    myapp = Application( master=root )
    myapp.mainloop()