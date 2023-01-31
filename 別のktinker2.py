import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.geometry("300x200") 

        #---------------------------------------
        #  ツールバー
        #---------------------------------------
        # ツールバー用Frame
        frame_toolbar = tk.Frame(self.master)
        # ツールボタン
        button1 = tk.Button(frame_toolbar, text = "1", width = 2)
        button2 = tk.Button(frame_toolbar, text = "2", width = 2)
        button3 = tk.Button(frame_toolbar, text = "3", width = 2)
        # ボタンをフレームに配置
        button1.pack(side = tk.LEFT)
        button2.pack(side = tk.LEFT)
        button3.pack(side = tk.LEFT)
        # ツールバーをウィンドの上に配置
        frame_toolbar.pack(fill = tk.X)

        #---------------------------------------
        #  ステータスバー
        #---------------------------------------
        # ツールバー用Frame
        frame_statusbar = tk.Frame(self.master, relief = tk.SUNKEN, bd = 2)
        # ステータスラベル
        label = tk.Label(frame_statusbar, text = "StatusLabel")
        # ラベルをフレームに配置
        label.pack(side = tk.LEFT)
        # ステータスバーをウィンドの下に配置
        frame_statusbar.pack(side = tk.BOTTOM, fill = tk.X)

        #---------------------------------------
        #  右カラム
        #---------------------------------------
        # 右カラム用Frame
        frame_column = tk.Frame(self.master, relief = tk.SUNKEN, bd = 2, width = 100)
        frame_column.propagate(False) # フーレムサイズの自動調整を無効にする
        # チェックボタン
        check1 = tk.Checkbutton(frame_column, text = "Check1")
        check2 = tk.Checkbutton(frame_column, text = "Check2")
        check3 = tk.Checkbutton(frame_column, text = "Check3")
        # チェックボタンをフレームに配置
        check1.pack()
        check2.pack()
        check3.pack()
        # 右カラムをウィンドの右に配置
        frame_column.pack(side = tk.RIGHT, fill = tk.Y)

        #---------------------------------------
        #  残りの領域
        #---------------------------------------
        frame = tk.Frame(self.master, relief = tk.SUNKEN, bd = 2, bg = 'dark cyan')
        frame.pack(expand = True, fill = tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()