"""

請撰寫一個程式，讓使用者輸入三個數字，程式會比較這三個數字的大小，並將其中的最大值印出來。

"""

n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
n3 = int(input("enter third number:"))

if n1>n2 and n1>n3:
    print(f"{n1} is maximum value.")
elif n2>n1 and n2>n3:
    print(f"{n2} is maximum value.")
elif n3>n1 and n3>n2:
    print(f"{n3} is maximum value.")

# use math module
'''
result = max(a, b, c)
print(f"{result} is maximum value.")
'''
