"""

請撰寫一個程式，讓使用者輸入一個整數 n，並印出費氏數列的前 n 個數字。
•	例如：輸入 6，程式應輸出 1, 1, 2, 3, 5, 8。

"""

n = int(input("please enter one integer:"))

a, b = 0, 1
for i in range(n):
    print(b,end=" ")
    temp = b
    b = a + b
    a = temp
print()

# Assign values at the same time
## 這行程式碼會先計算等號右邊的所有結果，再一起分給左邊，所以不會有先後覆蓋的問題。
'''
for i in range(n):
    print(b, end=" ")
    a, b = b, a + b  # a 拿舊的 b，b 拿 a+b，同時完成！
'''