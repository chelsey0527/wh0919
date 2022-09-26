def calculate(min, max, step):
    ans = 0
    while min < max+1:
        ans += min
        min += step
    print(ans)

    # 請用你的程式補完這個函式的區塊
    
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0