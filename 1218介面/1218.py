# _*_ coding:utf8_*_
import tkinter as tk
import tkinter.ttk as tt
import tkinter.font as tkFont
import datetime
import os
from PIL import Image

class Food(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f = tkFont.Font(size = 18, family = "微軟正黑體")
        f1 = tkFont.Font(size = 20, family = "微軟正黑體", weight="bold")

        # 日期
        self.lbldate = tk.Label(self, text = str(datetime.date.today()), height = 1, width = 15, font = f, fg ='SteelBlue', justify = tk.LEFT,anchor=tk.NW)
        self.lbldate.grid(row = 1, sticky = tk.W)

        # 圖片
        
        logo = Image.open( "pic.png" )
        logo2 = logo.resize( (400, 150), Image.BILINEAR )
        logo2.save( "pic2.png" )
        self.imageMain = tk.PhotoImage(file="pic2.png")
        self.lblimage = tk.Label(self, image=self.imageMain, anchor=tk.CENTER)
        self.lblimage.grid(row = 0, columnspan = 2, sticky = tk.NE +tk.SW)
        os.remove("pic2.png")

        # 分隔線
        line = Image.open( "line.png" )
        line2 = line.resize( (350, 1), Image.BILINEAR )
        line2.save( "line2.png" )
        self.imageline = tk.PhotoImage(file="line2.png")
        self.lblline = tk.Label(self, image=self.imageline, anchor=tk.CENTER)
        self.lblline.grid(row = 3,columnspan = 2)
        os.remove("line2.png")
        
        # 心情
        self.labemotion = tk.Label(self, text = '心情:', justify=tk.LEFT, width=15, font = f1,anchor=tk.NW)
        self.stdemotion = ('好','還好','不好')
        self.comemotion = tt.Combobox(self, width=15, values= self.stdemotion)
        self.labemotion.grid(row = 4, sticky = tk.W)
        self.comemotion.grid(row = 5, sticky = tk.W)

        # 人數
        self.labpeople = tk.Label(self, text = '人數:', justify=tk.LEFT, width=15, font = f1,anchor=tk.NW)
        self.stdpeople = ('1','2~5','5~')
        self.compeople = tt.Combobox(self, width=15, values= self.stdpeople)
        self.labpeople.grid(row = 6, sticky = tk.W)
        self.compeople.grid(row = 7, sticky = tk.W)

        # 預算
        self.lblbudget = tk.Label(self, text = "預算:" , height = 1, width = 15, font = f1,anchor=tk.NW)
        self.stdbudget = ('~200','200~500','500~')
        self.combudget = tt.Combobox(self, width=15, values= self.stdbudget)
        self.lblbudget.grid(row = 8,  sticky = tk.W)
        self.combudget.grid(row = 9, sticky = tk.W)

        # 空行
        self.labemotion = tk.Label(self, text = '', height=1, width=15, font = f1,anchor=tk.NW)
        self.labemotion.grid(row = 10, sticky = tk.W)


        # 天氣
        self.lblweather = tk.Label(self, text = str(self.weatherinfo()), width = 15, font = f, fg='SteelBlue', justify=tk.LEFT,anchor=tk.NW)
        self.lblweather.grid(row = 2, sticky = tk.W)
        self.lblweather = tk.Label(self, text = "溫度:"+ str(self.degreeinfo()), width = 15, font = f, fg='SteelBlue' ,justify=tk.LEFT,anchor=tk.NW)
        self.lblweather.grid(row = 2, sticky = tk.W)


        # 確認鍵
        ok = Image.open( "ok.png" )
        ok2 = ok.resize( (140, 50), Image.BILINEAR )
        ok2.save( "ok2.png" )
        self.imageok = tk.PhotoImage(file="ok2.png")
        self.btnok = tk.Button(self, image = self.imageok, command = self.clickBtn,anchor=tk.CENTER)
        self.btnok.grid(row = 11)
        os.remove("ok2.png")


        # 分隔線
        lline = Image.open( "lline.png" )
        line3 = lline.resize( (350, 1), Image.BILINEAR )
        line3.save( "line3.png" )
        self.imageline2 = tk.PhotoImage(file="line3.png")
        self.lblline2 = tk.Label(self, image=self.imageline2, anchor=tk.CENTER)
        self.lblline2.grid(row = 12)
        os.remove("line3.png")

        # 結果
        self.cvsMain = tk.Canvas(self, width = 800, height = 600, bg = "white")
        # self.cvsMain.grid(row = 13,  sticky = tk.NE + tk.SW)

    def clickBtn(self):
        # 爬蟲組
        pass
    def weatherinfo(self):
        pass
    def degreeinfo(self):
        pass 

        
   

window = Food()
window.master.title("app")
window.master.geometry('400x700')
window.mainloop()