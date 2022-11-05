import mysql.connector
import time
import datetime
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
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
        cursor.execute("SELECT * FROM member WHERE username=%(username)s", {"username": username})
        record = cursor.fetchall()
        # If record exist, put the data into our session with record[column]
        if record:
            message = request.args.get("error", "帳號已經被註冊")
            return redirect(url_for("error", message = message))
        # Username or password incorrect
        else:
            print("------------------ 建立帳戶中 .... -----------------------")
            session["userStatus"] = True
            session["name"] = name
            session["userName"] = username
            session["password"] = pw
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            insert_mem = (
                "INSERT INTO member (name, username, password, follower_count, time)"
                "VALUES(%s, %s, %s, %s, %s)"
            )
            data = (name, username, pw, 0, timestamp)
            cursor.execute(insert_mem, data)
            mydb.commit() # 要有這行才能成功把資料打進去
            return redirect(url_for("member"))

# ---------- 錯誤頁面 ----------
@app.route("/error")
def error():
    message = request.args.get("message", "預設")
    return render_template("error.html", message=message)

# ---------- 登入，進到 member 頁面 ----------
@app.route("/member", methods=["GET"])
def member():
    if session["userStatus"] == True:
        return render_template("member.html", currentname=session["name"])
    else:
        return redirect(url_for("index"))

# ---------- 查詢會員資料 API，return json 資料值 ----------
@app.route("/api/member", methods=["GET","PATCH"])
def api_member():
    # 取得搜尋字串
    if request.method == "GET":
        # 取得附加在 url 中的參數
        qusername = request.args.get("username")
        cursor.execute("SELECT * FROM member WHERE username=%(qusername)s", {"qusername": qusername})
        record = cursor.fetchall()
        fields=cursor.description
        column_list=[]
        if record:
            # 新增屬性 results，將查詢結果送回前端頁面
            # 抓取總欄位
            for i in fields:
                column_list.append(i[0])
            # 把欄位中的資料放進結果列中
            for row in record:
                result = {}
                result[column_list[0]] = row[0]
                result[column_list[1]] = str(row[1])
                result[column_list[2]] = str(row[2])
                data = {
                    "data":{
                        "id" : result[column_list[0]],
                        "name" : result[column_list[1]],
                        "username" : result[column_list[2]] 
                    }
                }
        else:
            data = {
                "data": None
            }
        ans = jsonify(data)
    elif request.method == "PATCH":
        uname = request.json['name']
        fields=cursor.description
        column_list=[]
        if session["userStatus"]:
            data = {
                "ok":True
            }
            cursor.execute("UPDATE member SET name=%(name)s WHERE username=%(username)s;", {"name":uname, "username": session["userName"]})
            mydb.commit() 
        else:
            data = {
                "error":True
            }
        ans = jsonify(data)
    return ans
    

# ---------- 登出，進到登入畫面 ----------
@app.route("/signout" , methods=["GET"])
def signout():
    session["userStatus"] = False
    session.pop("name", None)
    session.pop("userName", None)
    session.pop("password", None)
    return redirect(url_for("index"))

app.run(port=3000, debug=True)