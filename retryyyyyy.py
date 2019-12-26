from selenium import webdriver
import time
import requests
driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver')
driver.get('https://www.foodpanda.com.tw/restaurants/lat/25.0173405/lng/121.5397518/city/%E5%A4%A7%E5%AE%89%E5%8D%80/address/%25E8%2587%25BA%25E7%2581%25A3%25E5%25A4%25A7%25E5%25AD%25B8%252C%252010617%25E5%258F%25B0%25E7%2581%25A3%25E5%258F%25B0%25E5%258C%2597%25E5%25B8%2582%25E5%25A4%25A7%25E5%25AE%2589%25E5%258D%2580%25E7%25BE%2585%25E6%2596%25AF%25E7%25A6%258F%25E8%25B7%25AF%25E5%259B%259B%25E6%25AE%25B51%25E8%2599%259F/%25E7%25BE%2585%25E6%2596%25AF%25E7%25A6%258F%25E8%25B7%25AF%25E5%259B%259B%25E6%25AE%25B5/1%2520%25E8%2587%25BA%25E7%2581%25A3%25E5%25A4%25A7%25E5%25AD%25B8?postcode=10617&verticalTab=restaurants')
time.sleep(3)

for i in range(50): #捲動50次
  driver.execute_script("window.scrollTo(0, {})".format(4000 * (i + 1))) #每次捲動4000的單位
  time.sleep(2) #等待2秒鐘讓頁面讀取


htmltext = driver.page_source


from bs4 import BeautifulSoup
soup = BeautifulSoup(htmltext, 'html.parser')

ATTR = {'class': 'vendor-info'}
res_info = soup.find_all('figcaption', attrs = ATTR)

def crawl(ele):
  info = []     #存每家店家資訊
  L = []     #暫存list
  tmp = ele.get_text().strip()
  tmp.replace(" ", '')
  
  for e in tmp:
    L.append(e)     #把文字元素存進L

  while '\n' in L:     #把符號去除
    L.remove('\n')
  while ' ' in L:
    L.remove(' ')
  while '$' in L:
    L.remove('$')
  
  info_str = ''.join(L)     #變字串
  index = info_str.rfind('N')     #去除運費相關資訊
  if index >= 0:
    info_str = info_str[:index]
  else:
    index2 = info_str.rfind('免')
    info_str = info_str[:index2]
    
  index_name = info_str.rfind(')')     #店名有(分店)
  index3 = info_str.rfind('非')     #店名沒分店沒評價(非店內價)
  index_dot = info_str.rfind('.')     #店名沒分店評價為小數
  index_line = info_str.rfind('/')     #店名沒分店評價為整數
  index4 = info_str.rfind('店')     #店名沒分店沒評價(店內價)
  if index_name >= 0:
    info.append(info_str[:index_name + 1])
    info_str = info_str[index_name + 1:]
  
  elif index_dot >= 0:
    info.append(info_str[:index_dot - 1])
    info_str = info_str[index_dot - 1:]
  
  elif index_line >= 0:
    info.append(info_str[:index_line - 1])
    info_str = info_str[index_line - 1:]
  
  elif index3 >= 0:
    info.append(info_str[:index3])
    info_str = info_str[index3:]
  elif index4 >= 0:
    info.append(info_str[:index4])
    info_str = info_str[index4:]
  else:
    info.append(info_str[:-2])
    info_str = info_str[-2:]
    
  
  index_rating = info_str.find('/')     #評價
  if index_rating >= 0:
    info.append(info_str[:index_rating])
    info_str = info_str[index_rating + 2:]
  else:
    info.append('none')
  
  if len(info_str) > 0:
    try:     
      n = int(info_str[0])
      index_count = info_str.find('非')
      
      if index_count >= 0:
        info.append(info_str[:index_count])
        info_str = info_str[index_count:]
      else:
        index5 = info_str.find('店')
        info.append(info_str[:index5])
        info_str = info_str[index5:]
    except ValueError:
      info.append('none')
  else:
    pass
    
  index6 = info_str.rfind('非')
  index7 = info_str.rfind('店')
  if index6 >= 0:
    info.append(info_str[index6 + 4:])
  elif index7 >= 0:
    info.append(info_str[index7 + 3:])
  else:
    info.append(info_str)
    
  
  
  return info

info_dic = {}
for ele in res_info:
  if crawl(ele)[0] not in info_dic:
    info_dic[crawl(ele)[0]] = crawl(ele)
  #info_list.append(crawl(ele))

#print(info_dic)
  
import csv

with open("C:\\Users\\User\\Desktop\\output.csv", 'w', encoding = 'utf-8', newline = '') as csvfile:
  
  writer = csv.writer(csvfile)
  
  for key in info_dic.keys():
    writer.writerow(info_dic[key])
  