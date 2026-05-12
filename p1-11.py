"""

請撰寫一個程式，計算從 1 加到 100 的所有整數總和(即1+2+3+4+...+100 ），並將最後的結果印出來。

"""

total = 0
for i in range(1,101):
    total += i
print(total)

# Gaussian summation formula
'''
n = 100
total = (1 + n) * n // 2
print(total) # 結果同樣是 5050，但計算次數從 100 次變成 1 次。
'''