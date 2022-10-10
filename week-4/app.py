from pickle import TRUE
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案的資料夾名稱
    static_url_path="/public" , # 靜態檔案對應的網址路徑  # 不一定要名稱相同
)


# 建立路徑 / 對應的處理函示
@app.route("/") 
def index(): 
    return render_template("index.html")

# 登入頁面
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
            # return render_template("member.html")
            session["boologin"] = True
            print("-----------logged in",session["boologin"])
            return redirect(url_for("member"))


# 錯誤頁面
@app.route("/error")
def error():
    message = request.args.get("message", None)
    return render_template("error.html") + message

# 登入，進到 member 頁面
@app.route("/member")
def member():
    if session["boologin"] == True:
        return render_template("member.html")
    else:
        return redirect(url_for("index"))

# 登出
@app.route("/signout")
def signout():
    # 登出後將 session 帳密移除
    session.pop("username", None)
    session.pop("password", None)
    session["boologin"] = False
    return redirect(url_for("index"))


# flask 的 session 有加密機制，可以自行設定密鑰
app.secret_key="anystringbutsecret"

app.run(port=3000, debug=True)