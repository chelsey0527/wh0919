//正確計算出非 manager 的員工平均薪資

function avg(data){
    // 請用你的程式補完這個函式的區塊
    let i = 0
    let totalSalary = 0
    let totalEmployees = 0
    let average = 0

    for( i = 0; i < data.employees.length; i++){
        // console.log("----- inside loop -----");
        for (let employees of data.employees) {
            if (employees.manager === false) {
                // console.log("someone is not a manager");
                totalSalary += employees.salary;
                totalEmployees += 1;
            }
          }
    }
    average = totalSalary/totalEmployees;
    console.log(average);
}
    
avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":false
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":true
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":false
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":false
        }
    ]
}); // 呼叫 avg 函式