# _*_ coding:utf8_*_
import tkinter as tk
import tkinter.ttk as tt
import tkinter.font as tkFont
import datetime
# from PIL import ImageTK
import os
import urllib.request as req

# 爬天氣資訊
url = "https://www.google.com/search?rlz=1C1NHXL_zh-TWTW729TW729&sxsrf=ACYBGNRD2A4uz2d1AmrqKRyMCCi5FITj0w%3A1576505302892&ei=1o_3XfaLNtvW-Qabu6HoAg&q=%E5%85%AC%E9%A4%A8%E5%A4%A9%E6%B0%A3&oq=%E5%85%AC%E9%A4%A8%E5%A4%A9%E6%B0%A3&gs_l=psy-ab.3..35i39i285i70i256j0i67j0i7i30l8.89745.93220..93573...5.2..0.613.1071.8j5-1......0....1..gws-wiz.......0i71j35i304i39i285i70i256j0i13.CgSlcLv9EZs&ved=0ahUKEwj2zsL0q7rmAhVba94KHZtdCC0Q4dUDCAs&uact=5"

request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
weather = root.find("span", class_ = "vk_gy vk_sh")
degree = root.find("span", class_ = "wob_t")

weatherinfo = weather.string
degreeinfo = degree.string


class Food(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f = tkFont.Font(size = 18, family = "微軟正黑體")
        f1 = tkFont.Font(size = 14, family = "微軟正黑體")

        # 日期
        self.lbldate = tk.Label(self, text = "日期:" + str(datetime.date.today()), height = 1, width = 15, font = f, justify = tk.LEFT)
        self.lbldate.grid(row = 0, column = 0, rowspan=1, sticky = tk.W)

        # 圖片
        # self.imageMain = ImageTk.PhotoImage(file = "pic.png")
        # self.lblimage = tk.Label(image=image)
        # self.lblimage.pack()
        # self.lblimage.grid(row = 1, column = 0,rowspan = 5, sticky = tk.NE + tk.SW)

        # 篩選
        self.lblitem = tk.Label(self, text = "篩選:" , width = 15, font = f1, justify=tk.LEFT)
        self.lblitem.grid(row = 2, column = 0, sticky = tk.W)
        
        # 心情
        self.labemotion = tk.Label(self, text = '心情:', justify=tk.LEFT, width=15, font = f)
        self.stdemotion = ('好','還好','不好')
        self.comemotion = tt.Combobox(self, width=15, values= self.stdemotion)
        self.labemotion.grid(row = 3, column = 0,rowspan=1, sticky = tk.W)
        self.comemotion.grid(row = 3, column = 1, sticky = tk.W)

        # 人數
        self.labpeople = tk.Label(self, text = '人數:', justify=tk.LEFT, width=15, font = f)
        self.stdpeople = ('1','2~5','5~')
        self.compeople = tt.Combobox(self, width=15, values= self.stdpeople)
        self.labpeople.grid(row = 3, column = 2, sticky = tk.W)
        self.compeople.grid(row = 3, column = 3, sticky = tk.W)

        # 預算
        self.lblbudget = tk.Label(self, text = "預算:" , height = 1, width = 15, font = f)
        self.txtbudget = tk.Text(self, height = 1, width = 15, font = f, borderwidth=2, relief="groove")
        self.lblbudget.grid(row = 3, column = 4, sticky = tk.W)
        self.txtbudget.grid(row = 3, column = 5, sticky = tk.NE + tk.SW)

        # 天氣
        self.lblweather = tk.Label(self, text = "天氣:" + weatherinfo, width = 15, font = f, justify = tk.LEFT)
        self.lblweather.grid(row = 4, column = 0, sticky = tk.W)
        self.lblweather = tk.Label(self, text = "溫度:"+ degreeinfo, width = 15, font = f, justify = tk.LEFT)
        self.lblweather.grid(row = 4, column = 1, sticky = tk.W)


        # 確認鍵
        self.btnok = tk.Button(self, text = '確認', height = 1, width = 15, command = self.clickBtn, font = f)
        self.btnok.grid(row = 5, column = 5, sticky = tk.NE +tk.SW)

        # output的list
        self.cvsMain = tk.Canvas(self, width = 800, height = 600, bg = "white")
        # self.cvsMain.grid(row = 4,  sticky = tk.NE + tk.SW)

    def clickBtn(self):
        # 爬蟲組
        pass

window = Food()
window.master.title("app")
window.mainloop()