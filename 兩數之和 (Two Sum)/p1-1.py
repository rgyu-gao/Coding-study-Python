"""

請撰寫一個程式，讓使用者輸入兩個數字，程式會計算這兩個數字的總和，並將結果印出來。

"""

num1 = int(input("input your first number:"))
num2 = int(input("input your second number:"))

result = num1 + num2

print(f"{num1}+{num2}={result}") # use f-string to simplyfy the sentence
