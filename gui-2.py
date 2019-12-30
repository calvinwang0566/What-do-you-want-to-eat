# _*_ coding:utf8_*_
import tkinter as tk
import tkinter.ttk as tt
import tkinter.font as tkFont
from tkinter import messagebox
import datetime
import os
from PIL import Image
import webbrowser

# 爬蟲
import urllib.request as req
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

# 讀取food panda資料
import pandas as pd
df = pd.read_csv("panda.csv", encoding = 'utf-8')

# gui主體
class Food(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f = tkFont.Font(size = 18, family = "微軟正黑體")
        f1 = tkFont.Font(size = 20, family = "微軟正黑體", weight="bold")
        f2 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 日期
        self.lbldate = tk.Label(self, text = str(datetime.date.today()), height = 1, width = 15, font = f2, fg ='SteelBlue', justify = tk.LEFT, anchor=tk.NW)
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
        self.lblline = tk.Label(self, image=self.imageline, anchor = tk.CENTER)
        self.lblline.grid(row = 4,columnspan = 2)
        os.remove("line2.png")

        # 分隔線
        lline = Image.open( "line.png" )
        line3 = line.resize( (350, 1), Image.BILINEAR )
        line3.save( "line3.png" )
        self.imageline2 = tk.PhotoImage(file="line3.png")
        self.lblline2 = tk.Label(self, image=self.imageline2, anchor=tk.CENTER)
        self.lblline2.grid(row = 15, columnspan = 2)
        os.remove("line3.png")

        
        # 心情
        self.labelmood = tk.Label(self, text = '心情：', justify = tk.LEFT, width=15, font = f1, anchor=tk.NW)
        self.stdemood = ('好','還好','不好')
        self.commood = tt.Combobox(self, width=15, values= self.stdemood)
        self.labelmood.grid(row = 6, sticky = tk.W)
        self.commood.grid(row = 7, sticky = tk.W)

        # 人數
        self.labpeople = tk.Label(self, text = '人數：', justify=tk.LEFT, width=15, font = f1, anchor = tk.NW)
        self.stdpeople = ('1','2~5','5~')
        self.compeople = tt.Combobox(self, width=15, values= self.stdpeople)
        self.labpeople.grid(row = 8, sticky = tk.W)
        self.compeople.grid(row = 9, sticky = tk.W)

        # 種類
        self.lbltype = tk.Label(self, text = "種類：" , height = 1, width = 15, font = f1,anchor=tk.NW)
        self.stdtype = ("三明治", "中港", "飲料", "火鍋", "早餐", "便當", "炸雞", "素食", "甜點", "滷味", "餃子", "麵類", "百貨美食節", "粥&湯", "鐵板燒", "FS_SOGO88", "日韓", "黎巴嫩料理", "咖哩", "東南亞", "美式料理", "Pizza比薩", "其他歐系料理")
        self.comtype = tt.Combobox(self, width=15, values = self.stdtype)
        self.lbltype.grid(row = 10,  sticky = tk.W)
        self.comtype.grid(row = 11, sticky = tk.W)

        # 空行
        self.labemotion1 = tk.Label(self, text = '', height=1, width=15, font = f1,anchor=tk.NW)
        self.labemotion1.grid(row = 12, sticky = tk.W)

        self.labemotion2 = tk.Label(self, text = '', height=1, width=15, font = f1,anchor=tk.NW)
        self.labemotion2.grid(row = 14, sticky = tk.W)


        # 天氣
        self.lblweather = tk.Label(self, text = weatherinfo, width = 15, font = f2, fg = 'SteelBlue', justify = tk.LEFT, anchor = tk.NW)
        self.lblweather.grid(row = 2, sticky = tk.W)
        self.lblweather = tk.Label(self, text = degreeinfo + "°C", width = 15, font = f2, fg = 'SteelBlue', justify = tk.LEFT, anchor = tk.NW)
        self.lblweather.grid(row = 3, sticky = tk.W)


        # 確認鍵
        ok = Image.open( "ok.png" )
        ok2 = ok.resize( (140, 50), Image.BILINEAR )
        ok2.save( "ok2.png" )
        self.imageok = tk.PhotoImage(file="ok2.png")
        self.btnok = tk.Button(self, image = self.imageok, command = self.clickBtn, anchor = tk.CENTER, cursor = "hand2")
        self.btnok.grid(row = 13)
        os.remove("ok2.png")



        # 結果
        self.cvsMain = tk.Canvas(self, width = 800, height = 600, bg = "white")
        # self.cvsMain.grid(row = 15,  sticky = tk.NE + tk.SW)

    # 確認按鈕功能
    def clickBtn(self):
        f = tkFont.Font(size = 18, family = "微軟正黑體")
        f1 = tkFont.Font(size = 20, family = "微軟正黑體", weight="bold")
        f2 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 抓出各個下拉選單的內容，轉換成數字
        if self.commood.get() == "好":
            mood = 1
        elif self.commood.get() == "還好":
            mood = 2
        elif self.commood.get() == "不好":
            mood = 3
        
        if self.compeople.get() == "1":
            people = 1
        elif self.compeople.get() == "2~5":
            people = 2
        elif self.compeople.get() == "5~":
            people = 3

        food_type = self.comtype.get()
        
        # 篩選出符合的餐廳
        try:    
            # 若有符合所有條件的
            mood_filter = df["心情(好、普、爛)"] == mood
            people_filter = df["適合人數(1、2-4、5)"] == people
            df_new = df[mood_filter & people_filter]
            df_new["type"] = df_new["分類"].str.find(food_type)
            food_filter = df_new["type"] == 0
            
            df_food = df_new[food_filter]   # 符合食物種類的餐廳
            total = len(df_food.index)
            df_random = df_food.sample(n = 1)   # 隨機挑選

            restaurant_name = df_random["店名"].to_string(index = False).strip()
            restaurant_star = df_random["星級"].to_string(index = False)
            restaurant_comment = df_random["評論數"].to_string(index = False)
            # print(restaurant_name, restaurant_star, restaurant_comment)

            # 跳出小視窗推薦+"(1 out of"+str(total)+")"
            # yes_no = messagebox.askquestion("推薦你吃！", message = df_random["店名"].to_string(index = False).strip() + "\n(總共"+ str(total) + "項中1項)" + "\n星級：" + df_random["星級"].to_string(index = False) + "\n評論數：" + df_random["評論數"].to_string(index = False) + "\n" + "\n是否需要店家連結")
            
            self.top = tk.Toplevel()

            self.name_lbl = tk.Label(self.top, text = "店名：" + restaurant_name, font = f, fg="blue", cursor="hand2")
            self.name_lbl.pack()

            self.star_lbl = tk.Label(self.top, text = "星級：" + restaurant_star, font = f2)
            self.star_lbl.pack()

            self.comment_lbl = tk.Label(self.top, text = "評論數：" + restaurant_comment, font = f2)
            self.comment_lbl.pack()
            
            self.name_lbl.bind("<Button-1>", lambda e: callback())

        except:    
            messagebox.showerror(title = "Error", message = "沒有符合條件的餐廳")

            # 沒有都符合的話，以食物種類為主
            # df["type"] = df["分類"].str.find(food_type)
            # food_filter = df["type"] == 0
            # df_food = df[food_filter]
            # df_random = df_food.sample(n = 1)

            # yes_no = messagebox.askquestion("推薦你吃！", message = df_random["店名"].to_string(index = False).strip() + "\n(未有符合條件之餐廳，隨機選擇)" + "\n星級：" + df_random["星級"].to_string(index = False) + "\n評論數：" + df_random["評論數"].to_string(index = False) + "\n" + "\n是否需要店家連結")

def callback():
    webbrowser.open_new("https://www.foodpanda.com.tw/restaurants/lat/25.0173405/lng/121.5397518/city/%E5%A4%A7%E5%AE%89%E5%8D%80/address/%25E8%2587%25BA%25E7%2581%25A3%25E5%25A4%25A7%25E5%25AD%25B8%252C%252010617%25E5%258F%25B0%25E7%2581%25A3%25E5%258F%25B0%25E5%258C%2597%25E5%25B8%2582%25E5%25A4%25A7%25E5%25AE%2589%25E5%258D%2580%25E7%25BE%2585%25E6%2596%25AF%25E7%25A6%258F%25E8%25B7%25AF%25E5%259B%259B%25E6%25AE%25B51%25E8%2599%259F/%25E7%25BE%2585%25E6%2596%25AF%25E7%25A6%258F%25E8%25B7%25AF%25E5%259B%259B%25E6%25AE%25B5/1%2520%25E8%2587%25BA%25E7%2581%25A3%25E5%25A4%25A7%25E5%25AD%25B8?postcode=10617")
            
window = Food()
window.master.title("NTU Food Recommender")
window.master.geometry('400x700')
window.master.iconbitmap("dish.ico")
window.mainloop()