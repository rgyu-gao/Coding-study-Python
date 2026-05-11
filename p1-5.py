"""

請撰寫一個程式，讓使用者輸入身高（公分，cm）與體重（公斤，kg），程式會計算並輸出其 BMI 值。
（輸出結果請保留到小數點後兩位）

"""

height = float(input("enter your height(cm):"))
weight = float(input("enter your weight(kg):"))

height_m = height / 100

bmi = weight / (height_m ** 2)

print(f"your height is {height} cm，your weight is {weight} kg")
print(f"the BMI : {bmi:.2f}")