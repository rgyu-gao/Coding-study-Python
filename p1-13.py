"""

請撰寫一個程式，讓使用者輸入一個正整數 n ，計算並輸出 n!（階乘）的結果。
例如：若輸入 5 ，則計算 5×4×3×2×1=120。

"""

n = int(input("enter a positive integer:"))

result = 1
for i in range(n,0,-1):
    result *= i

print(f"The factorial is: {result}")

# use math module
'''
import math
n = int(input("請輸入數字: "))
# 直接把 range 丟進去，它會自動幫你全部乘起來
result = math.prod(range(1, n + 1))
print(f"結果是: {result}")
'''