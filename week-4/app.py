from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案的資料夾名稱
    static_url_path="/public" , # 靜態檔案對應的網址路徑  # 不一定要名稱相同
)


# ---------- 建立路徑 / 對應的處理函示 ----------
@app.route("/") 
def index(): 
    return render_template("index.html")


# ---------- 登入頁面 ----------

# 1. flask sessions 版本
@app.route("/signin", methods=["POST"])
def login():
    # POST query String **機密資訊必用**
    userName = request.form["userName"]
    password = request.form["password"]
    session["userName"] = userName
    session["password"] = password
    session["boologin"] = False
    if userName == "" or password == "":
        # 只要是空的就直接跳 error
        message = request.args.get("error", "請輸入帳號、密碼")
        return redirect(url_for("error", message = message))
    else:
        # 非空，檢查帳號密碼是否為 test
        if userName != "test" or password != "test":
            message = request.args.get("error", "帳號、密碼輸入錯誤")
            return redirect(url_for("error", message = message))
        else:
            session["boologin"] = True
            return redirect(url_for("member"))

# 2. 直接操作 cookie 版本
# set cookie
# @app.route('/setcookie', methods = ['POST', 'GET'])
# def setcookie():
#    if request.method == 'POST':
#    user = request.form['nm']
   
#    resp = make_response(render_template('readcookie.html'))
#    resp.set_cookie('userID', user)
   
#    return resp
# get cookie
# @app.route('/getcookie')
# def getcookie():
#    name = request.cookies.get('userID')
#    return '<h1>welcome ' + name + '</h1>'


# ---------- 錯誤頁面 ----------
@app.route("/error")
def error():
    message = request.args.get("message", "預設")
    return render_template("error.html", message=message)


# ---------- 登入，進到 member 頁面 ----------
@app.route("/member")
def member():
    if session["boologin"] == True:
        return render_template("member.html")
    else:
        return redirect(url_for("index"))


# ---------- 登出，進到登入畫面 ----------
@app.route("/signout")
def signout():
    # 登出後將 session 帳密移除，並且是否登入顯示為 False
    session.pop("username", None)
    session.pop("password", None)
    session["boologin"] = False
    return redirect(url_for("index"))

# ---------- dynamic routing 格式設定，讓 js call 頁面時可以成功 ----------
# 1. 透過 js 傳請求到後端
@app.route("/square/<int:answer>")
def square(answer):
    return render_template('square.html', answer=answer)

# 2. 原本的方法，但是比較繞圈 
# 計算結果頁面
# @app.route("/square/<int:answer>")
# def square(answer):
#     number = request.args.get("number", 0)
#     number = int(number)
#     answer = number*number
#     return render_template("square.html",  answer=answer)
# @app.route("/calculateSquare")
# def calculateSquare():
#     number = request.args.get("number", 0)
#     number = int(number)
#     answer = number*number
#     return redirect(url_for("square", answer=answer))


# ---------- flask 的 session 有加密機制，可以自行設定密鑰 ----------
app.secret_key="anystringbutsecret"


app.run(port=3000, debug=True)