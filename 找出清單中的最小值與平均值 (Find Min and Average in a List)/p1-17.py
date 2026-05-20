"""

給定同一個數字清單：numbers = [12, 45, 7, 23, 56, 89, 34]
請撰寫一個程式，利用 迴圈 依序檢查清單中的數字，並找出其中的最小值以及計算出這串數字的平均值。

"""

numbers = [12, 45, 7, 23, 56, 89, 34]

minnum = numbers[0]

avg = 0
for i in numbers:
    avg += i
    if i < minnum:
        minnum = i
    
print(minnum)
print(avg/len(numbers))
