"""

請撰寫一個程式，讓使用者輸入圓的半徑 (r)，並計算出該圓的面積。
（請將 π 固定取值為 3.14159)

"""

π = 3.14159

radius = float(input("please enter circle radius(r):"))

area = (radius ** 2) * π

print(f"when radius is {radius},circle area is {area:.2f}.")


# also can use math module 
'''
import math
print(math.pi) # 會輸出 3.141592653589793
'''

