# 正確計算出非 manager 的員工平均薪資

def avg(data):
    # 請用你的程式補完這個函式的區塊
    i = 0
    totalSalary = 0
    totalEmployees = 0
    average = 0
    for i in data["employees"]:
        if i["manager"] == False:
            totalSalary += i["salary"]
            totalEmployees += 1
    average = totalSalary/totalEmployees
    print(average)

avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) 
# 呼叫 avg 函式