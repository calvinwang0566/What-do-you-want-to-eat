# _*_ coding:utf8_*_
import tkinter as tk
import tkinter.ttk as tt
import tkinter.font as tkFont
import datetime
# from PIL import ImageTK
import os


class Food(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f = tkFont.Font(size = 16, family = "微軟正黑體")

        # 日期
        self.lbldate = tk.Label(self, text = " 日期: " + str(datetime.date.today()), height = 1, width = 100, font = f)

        # # # 圖片
        # # self.imageMain = ImageTk.PhotoImage(file = "temp.png")

        # 篩選
        self.lblitem = tk.Label(self, text = "篩選:" , height = 10, width = 5, font = f)

        
        # 心情
        self.labemotion = tk.Label(self, text = '心情:', justify=tk.RIGHT, width=5)
        self.stdemotion = ('好','還好','不好')
        self.comemotion = tt.Combobox(self, width=5, values= self.stdemotion)

        # 人數
        self.labpeople = tk.Label(self, text = '人數:', justify=tk.RIGHT, width=5)
        self.stdpeople = ('1','2~5','5~')
        self.compeople = tt.Combobox(self, width=5, values= self.stdpeople)

        # 預算
        self.lblbudget = tk.Label(self, text = "預算:" , height = 1, width = 5, font = f)
        self.txtbudget = tk.Text(self, height = 1, width = 5, font = f)

        # output的list
        self.cvsMain = tk.Canvas(self, width = 800, height = 600, bg = "white")

        # grid 們
        self.lbldate.grid(row = 0, column = 0, sticky = tk.W)
        # # self.imageMain.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
        self.lblitem.grid(row = 3, sticky = tk.W)
        self.labemotion.grid(row = 4, column = 1, sticky = tk.W)
        self.comemotion.grid(row = 4, column = 2, sticky = tk.W)
        self.labpeople.grid(row = 4, column = 3, sticky = tk.W)
        self.compeople.grid(row = 4, column = 4, sticky = tk.W)

        self.lblbudget.grid(row = 4, column = 5, sticky = tk.E)
        self.txtbudget.grid(row = 4, column = 6, sticky = tk.NE + tk.SW)

        self.cvsMain.grid(row = 5, column = 0, sticky = tk.NE + tk.SW)




window = Food()
window.master.title("app")
window.mainloop()