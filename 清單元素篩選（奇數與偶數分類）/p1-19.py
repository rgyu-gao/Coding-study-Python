"""

給定一個包含隨機整數的清單，例如：
numbers = [14, 27, 8, 43, 91, 52, 30, 11]
請撰寫一個程式，建立兩個全新的空清單：odds（存放奇數）與 evens（存放偶數）。
利用迴圈檢查 numbers 中的每一個數字，並將它們正確地分流到這兩個新清單中，最後印出這兩個清單。

"""

numbers = [14, 27, 8, 43, 91, 52, 30, 11]

odds = []
evens = []

for i in numbers:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

print(f"odds list is {odds}.")
print(f"evens list is {evens}.")

# 清單解析式 (List Comprehension)
'''
numbers = [14, 27, 8, 43, 91, 52, 30, 11]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
'''
