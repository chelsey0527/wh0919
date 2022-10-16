from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
from flask import render_template
# 建立 Application 物件，可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="static", # 靜態檔案的資料夾名稱
    static_url_path="/static" # 靜態檔案對應的網址路徑  # 不一定要名稱相同
) 

# 建立路徑 / 對應的處理函示
@app.route('/')
def index(): # 用來回應網站首頁連線的函示
    return render_template("index", name="小明")
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑",request.path)
    # print("完整的網址", request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    # print("語言偏好", request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))
    # lang = request.headers.get("accpet-language")
    # print("語言偏好", lang)
    # if lang.startswith("en"):
    #     return json.dumps({
    #         "status": "ok",
    #         "text": "hello world"
    #     })
    # else:
    #     return json.dumps({
    #         "status": "ok",
    #         "text": "您好"
    #     })



# 建立路徑 /getSum 對應的處理函示
# 利用要求字串 (Query String) 提供彈性 max=最大數字
# @app.route("/getSum")
# def getSum():
#     maxNumber=request.args.get("max", 100) # 預設 100
#     maxNumber=int(maxNumber)
#     minNumber=request.args.get("min", 0)
#     minNumber=int(minNumber)
#     result = 0
#     for n in range(minNumber,maxNumber+1):
#         result+=n
#     return "結果: "+str(result)


# 建立路徑 /data 對應的處理函示
# @app.route("/data")
# def hangleData():
#     return "My Data"

# 動態路由： 建立路徑 /user/使用者名稱 對應的處理函式
# @app.route("/user/<username>")
# def hangleUser(username):
#     if username == "chelsey":
#         return "安安" + username
#     return "Hello " + username

# 啟動網站伺服器
# 將 port 改成作業要求
app.run(port=3000, debug=True)