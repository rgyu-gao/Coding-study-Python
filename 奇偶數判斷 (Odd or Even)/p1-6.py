"""

請撰寫一個程式，讓使用者輸入一個整數，程式會判斷該數字是奇數 (Odd) 還是 偶數 (Even)，並將結果印出來。

"""

n = int(input("please enter one interger:"))

if n % 2 == 0:
    print(f"{n} is even.")
else:
    print(f"{n} is odd.")
