"""

給定一個包含許多重複數字的清單，例如：
grades = [60, 75, 80, 60, 90, 75, 60, 85, 90]
請撰寫一個程式，讓使用者輸入一個想要查詢的分數（例如 60），
程式會利用 迴圈 去統計這個分數在清單中總共出現了幾次，並將結果印出來。
(注意：請先不要使用內建的 grades.count() 語法唷！)

"""

grades = [60, 75, 80, 60, 90, 75, 60, 85, 90]

n = int(input("輸入一個想要查詢的分數:"))

find = 0
for i in grades:
    if i == n:
        find += 1
print(f"這個分數在清單中總共出現了 {find} 次。")

# 使用 try-except 防止使用者輸入非數字的內容
'''
try:
    n = int(input("輸入一個想要查詢的分數: "))
    
    find = 0
    for i in grades:
        if i == n:
            find += 1
            
    print(f"這個分數在清單中總共出現了 {find} 次。")
    
except ValueError:
    print("錯誤：請輸入純數字，不要輸入文字或留空格！")
'''