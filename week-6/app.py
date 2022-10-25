import mysql.connector
import time
import datetime
from flask import Flask, render_template, request, session, redirect, url_for

# ---------- MySQL DB ----------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="website",
    charset="utf8",
)
cursor = mydb.cursor()

app = Flask(
    __name__,
    static_folder="public", # 靜態檔案的資料夾名稱
    static_url_path="/public" , # 靜態檔案對應的網址路徑  # 不一定要名稱相同
)

# ---------- flask 的 session 有加密機制，可以自行設定密鑰 ----------
app.secret_key="anystringbutsecret"

# ---------- 建立路徑 / 對應的處理函示 ----------
@app.route("/") 
def index(): 
    cursor.execute("SELECT * FROM member")
    record = cursor.fetchall()
    print(record)
    return render_template("index.html")

# ---------- 登入功能 ---------- (flask sessions 版本)
@app.route("/signin", methods=["POST"])
def login():
    session["userStatus"] = False
    if request.method == "POST":
        # POST query String **機密資訊必用**
        username = request.form["userName"]
        pw = request.form["password"]
        cursor.execute("SELECT * FROM member WHERE username=%(username)s AND password=%(password)s", {"username": username, "password":pw})
        record = cursor.fetchall()
        # If record exist, put the data into our session with record[column]
        if record:
            # 取第一筆資料即可，資料庫中理應只有唯一用戶
            session["userStatus"] = True
            session["userId"] = record[0][0]
            session["name"] = record[0][1]
            session["userName"] = record[0][2]
            session["password"] = record[0][3]
            return redirect(url_for("member"))
        # No record means username or password incorrect
        else:
            message = request.args.get("error", "帳號或密碼輸入錯誤")
            return redirect(url_for("error", message = message))

# ---------- 註冊功能 ---------- (flask sessions 版本)
@app.route("/signup", methods=["POST"])
def signup():
    session["userStatus"] = False
    if request.method == "POST":
        # POST query String **機密資訊必用**
        name = request.form["name"]
        username = request.form["userName"]
        pw = request.form["password"]
        # executemany when there are several values 
        cursor.execute("SELECT * FROM member WHERE username=%(username)s", {"username": username})
        record = cursor.fetchall()
        # If record exist, put the data into our session with record[column]
        if record:
            print("此帳號已被註冊!!!!!!!!!!!!!!!!!!!")
            # 帳號已被註冊，導向 error 頁面
            message = request.args.get("error", "帳號已經被註冊")
            return redirect(url_for("error", message = message))
        # Username or password incorrect
        else:
            print("------------------ 建立帳戶中 .... -----------------------")
            session["userStatus"] = True
            session["name"] = name
            session["userName"] = username
            session["password"] = pw
            # Set timestamp
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            insert_mem = (
                "INSERT INTO member (name, username, password, follower_count, time)"
                "VALUES(%s, %s, %s, %s, %s)"
            )
            data = (name, username, pw, 0, timestamp)
            cursor.execute(insert_mem, data)
            mydb.commit() # 要有這行才能成功把資料打進去
            print("資料輸入完畢")
            return redirect(url_for("member"))

# ---------- 錯誤頁面 ----------
@app.route("/error")
def error():
    message = request.args.get("message", "預設")
    return render_template("error.html", message=message)

# ---------- 登入，進到 member 頁面 ----------
@app.route("/member")
def member():
    # comment_list = []
    # cursor.execute("SELECT content FROM message ")
    # record = cursor.fetchall()
    # comment_list.append(record)
    # session["messages"] = comment_list
    if session["userStatus"] == True:
        return render_template("member.html", name = session["name"])
        # return render_template("member.html", name = session["name"],messages = session["messages"])
    else:
        return redirect(url_for("index"))

# ---------- 留言功能 ---------- 
# @app.route("/comment", methods=["POST"])
# def comment():
#     if session["userStatus"]==True:
#         # POST query String **機密資訊必用**
#         comm = request.form["comment"]
#         ts = time.time()
#         timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#         insert_mes = (
#             "INSERT INTO message (member_id, content, like_count, time)"
#             "VALUES(%s, %s, %s, %s)"
#         )
#         data = (session["userId"], comm, 0, timestamp)
#         cursor.execute(insert_mes, data)
#         # mydb.commit() # 要有這行才能成功把資料打進去
#         print("資料輸入完畢")
#         print(data)
#         return redirect(url_for("member"))
        

# ---------- 登出，進到登入畫面 ----------
@app.route("/signout" , methods=["GET"])
def signout():
    # 登出後將 session 帳密移除，並且是否登入顯示為 False
    session["userStatus"] = False
    session.pop("name", None)
    session.pop("userName", None)
    session.pop("password", None)
    return redirect(url_for("index"))

app.run(port=3000, debug=True)