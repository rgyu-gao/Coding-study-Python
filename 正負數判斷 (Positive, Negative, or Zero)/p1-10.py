"""

請撰寫一個程式，讓使用者輸入一個數字，程式會判斷並輸出該數字是正數 (Positive)、負數 (Negative) 還是 零 (Zero)。

"""

n = int(input("enter one number:"))

if n > 0:
    print(f"{n} is positive.")
elif n < 0:
    print(f"{n} is negative.")
else:
    print(f"{n} is zero.")
