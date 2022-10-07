# https://www.youtube.com/watch?v=9Z9xKWfNo7k&t=107s
# pip3 install beautifulsoup4

# 解決 request 失敗問題
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 串接擷取資料
import urllib.request as req
import json
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立 request 物件附加 headers 資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 利用 json 模組處理 json 資料格式
# print(data)


# 利用 bs4 解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div", class_="title")
print(titles)



with open("movie.txt", "w", encoding="utf-8") as file:
    resultHL = []
    resultPL = []
    resultFL = []
    # test = []
    for title in titles:
        if title.a != None:
            result = title.a.string
            print(result[0:3])
            # 抓出符合關鍵字的結果，並且分別存進對印的 list
            if result[0:4] == "[好雷]":
                resultHL.append(result)
            if result[0:4] == "[普雷]":
                resultPL.append(result)
            if result[0:4] == "[負雷]":
                resultFL.append(result)
            # 測試到一半影評不見了，暫時用[公告]代替
            # if result[0:4] == "[公告]":
            #     test.append(result)

    # 寫入結果
    for i in resultHL:
        file.write(i+"\n")  
    for i in resultPL:
        file.write(i+"\n")  
    for i in resultFL:
        file.write(i+"\n")  
    # for i in test:
    #     file.write(i+"\n")  