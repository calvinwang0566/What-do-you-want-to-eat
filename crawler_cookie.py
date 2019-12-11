import urllib.request as req

def getData(url):
    request = req.Request(url, headers = {
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_ = "title")

    for title in titles:
        print(title.get_text().strip())

    nextLink = root.find("a", string ="‹ 上頁")
    
    return (nextLink["href"])
    
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"

count = 0
while count < 10:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1

