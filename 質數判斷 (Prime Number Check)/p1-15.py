"""

請撰寫一個程式，讓使用者輸入一個大於 1 的整數，程式會判斷該數字是否為質數 (Prime Number)。
（質數定義：除了 1 和自己以外，不能被任何整數整除的數）

"""

n = int(input("enter one integer(more than 1):"))

for i in range(2,n):
    if n % i == 0:
        print(f"{n} is not Prime Number.")
        break # Improve performance
else:
    print(f"{n} is Prime Number.")

# Engineering emization
'''
for i in range(2, int(n**0.5) + 1):
'''
