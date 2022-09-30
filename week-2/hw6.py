# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。

def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    # length = 0
    # for l in nums:
    #     length += 1

    target = 0
    max = 0
    count = 0

    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
            # print(i," = 0，所以 count+1 變成",count)
            #當最後一位是 0 時要停止
            if i == len(nums) - 1:
                if count > max:
                    # print(i,"是最後一位，且 != 0，所以 count ", count," 清空，並且放到 max")
                    # 如果斷掉的時候的 count 0 比 max 大就要替換掉再歸零
                    max = count
                    count = 0
                else:
                    # print(i,"是最後一位，且 != 0，所以 count ", count," 清空")
                    # 沒有比較大，直接歸零
                    count = 0
                
        else:
            if count > max:
                # print(i," != 0，所以 count ", count," 清空，並且放到 max")
                # 如果斷掉的時候的 count 0 比 max 大就要替換掉再歸零
                max = count
                count = 0
            else:
                # print(i," != 0，所以 count ", count," 清空")
                # 沒有比較大，直接歸零
                count = 0
    print(max)


maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3