# 參考影片: https://www.youtube.com/watch?v=sUzR3QVBKIo

# 解決 request 失敗問題
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# # python 網路連線的內建模組
# import urllib.request as request
# src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
# with request.urlopen(src) as response:
#     # 可以用中文解碼增加可閱讀性
#     data=response.read().decode("utf-8") 
# print(data)


# 串接擷取資料
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組處理 json 資料格式
# print(data)

# 取得特定資料值
dlist=data["result"]["results"]
# for company in clist:
#     print(company["stitle"],",",company["MRT"])

# 把資料存在檔案中

import re

with open("testdata.csv", "w", encoding="utf-8") as file:
    for desti in dlist:

        # 過濾 2015（含）之後
        # 取日期的前面 4 個值，進行篩選
        spXpostDate = desti["xpostDate"]
        xpostDateYear = int(spXpostDate[:4])
        if (xpostDateYear >= 2015):
            # print("---- 這位>=2015 -----\n")
            file.write(desti["stitle"]+",")

            # 取得地址中的區
            add = desti["address"].split('  ')[1].split('區')[0]
            # (假設用 py 輸出 print(add,"區,",sep = '') #把多餘的空格黏回來)
            file.write(add+"區,")
        
            # 輸出精度、緯度、圖案網址
            file.write(desti["longitude"]+","+desti["latitude"]+",")
            file.write(desti["file"].split(".jpg")[0]+".jpg\n\n")
        # else:
            # print("---- < 2015 -----\n")


