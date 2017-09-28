'''
Created on 2017/09/28

@author: y
'''


import tkinter as Tk


class Application(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('Todo List')
        self.master.geometry('400x300')

        # 変数初期化
        self.ToDoNumber = 0
        self.ToDo = []
        self.txt = []
        self.spent = []
        self.spentNumber = []

        # ウィジェットの生成・配置
        self.create_widgets()

        self.pack()

    def create_widgets(self):
        self.EditBox = Tk.Entry(self, width=30)
        self.EditBox.grid(row=0, column=0)

        Button = Tk.Button(self, text='追加')
        Button.bind('<Button-1>', self.DeleteEntryValue)
        Button.grid(row=0, column=1)

    def DeleteEntryValue(self, event):
        # EditBoxに書かれている文字列をtxtNewに代入
        txtNew = Tk.StringVar()
        txtNew.set(self.EditBox.get())

        # 新たにラベル(ToDoリスト)を作成
        ToDoNew = Tk.Label(self, width=30, textvariable=txtNew)

        # 新たに作成したラベル,txtをリストに追加
        self.txt.append(txtNew)
        self.ToDo.append(ToDoNew)

        # 新しいラベルをToDoリストの末尾に追加
        self.ToDoNumber += 1
        ToDoNew.grid(row=self.ToDoNumber, column=0)
        spentNumberNew = Tk.StringVar()
        spentNumberNew.set('0')
        spentNew = Tk.Label(self, width=2, textvariable=spentNumberNew)
        self.spent.append(spentNew)
        self.spentNumber.append(spentNumberNew)
        spentNew.grid(row=self.ToDoNumber, column=1)

        # EditBoxに書かれている文字列を消去
        self.EditBox.delete(0, Tk.END)


root = Tk.Tk()
app = Application(master=root)
app.mainloop()