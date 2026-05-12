"""

請撰寫一個程式，讓使用者輸入一個年份（如 2024)，程式會判斷該年份是否為閏年。
閏年的判定規則：
	1.	能被 4 整除，但不能被 100 整除。
	2.	或者，能被 400 整除。

"""

year = int(input("enter one year:"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is 閏年.")
else:
    print(f"{year} is not 閏年.")
