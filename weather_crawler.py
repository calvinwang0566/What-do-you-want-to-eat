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
temperature = root.find("span", class_ = "wob_t")

print(weather.string)
print(temperature.string)