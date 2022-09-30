// 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
// 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。



function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊
    console.log( multiple(nums))
}

//把全部兩兩相乘
function multiple(nums){
    let total = 0;
    const mNums = [];
    let count = 0;
    // console.log(mNums);
    for(i in nums){
        // console.log("nums-1 = "+ nums.length-1);
        for (j = nums.length-1; j>i; j--){
            // console.log("inside j");
            if (i != j){
                total = nums[i]*nums[j];
                mNums[count] = total;
                // console.log("add: "+mNums[count]);
                count++;
            }
        }
    }
    // return mNums[mNums.length-1];
    // 結果出來了，送去排序
    sort(mNums)
    return mNums[mNums.length-1]
}

function sort(mNums){
    let temp = 0
    for(i in mNums){
        for (j = mNums.length-1; j>i; j--){
            if (mNums[j] < mNums[i]){
                temp = mNums[i];
                mNums[i] = mNums[j];
                mNums[j] = temp
            }
        }
    }
    // console.log(mNums);
}


    
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10