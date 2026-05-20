"""

給定一個包含數個數字的清單，例如：numbers = [12, 45, 7, 23, 56, 89, 34]
請撰寫一個程式，利用 迴圈 依序檢查清單中的每個數字，並找出其中的最大值印出來。

"""

numbers = [12, 45, 7, 23, 56, 89, 34]

maxnum = numbers[0]

for i in numbers:
    if i > maxnum:
        maxnum = i
        
print(f"清單 {numbers} 中的最大值是: {maxnum}")