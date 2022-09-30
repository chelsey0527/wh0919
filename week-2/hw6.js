//給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。


function maxZeros(nums){
    // 請用你的程式補完這個函式的區塊

    let target = 0
    let max = 0
    let count = 0

    for (i = 0; i < nums.length; i++){
        if (nums[i] == target){
            count += 1
            if (i == nums.length-1){
                if (count > max){
                    max = count
                    count = 0
                }else{
                    count = 0
                }
            }
        }else{
            if (count > max){
                max = count
                count = 0
            }else{
                count = 0
            }
        }
    }
    console.log(max)
}
    
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3