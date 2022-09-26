# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。


def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    multiple(nums)
    print(multiple(nums))
    
#取得大小
def getSize(nums):
    length = 0
    for i in nums:
        length += 1
    # print("length:", length)
    return length

#把全部兩兩相乘
def multiple(nums):
    size = getSize(nums)
    total = 0
    #使用list來存取不固定數量的資料值
    mNums = []
    for i in range(0, size):
            for j in range (size-1, 0, -1):
                if ( i != j ):
                    # print(nums[i]*nums[j])
                    total = nums[i]*nums[j]
                    mNums.append(total)
    # print(mNums) 
    sort(mNums)
    #回傳排序後的結果的最後一位
    return mNums[getSize(mNums)-1] 
    
#排序
def sort(mNums):
    size = getSize(mNums)
    temp = 0
    for i in range(0, size):
        # print("value of i", i)
        for j in range (size-1, i, -1):
            # print("value of j", j)
            if mNums[j] < mNums[i]:
                # print( nums[j], "swap with", nums[i])
                temp = mNums[i]
                mNums[i] = mNums[j]
                mNums[j] = temp
    # print(mNums)    
    

            
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

