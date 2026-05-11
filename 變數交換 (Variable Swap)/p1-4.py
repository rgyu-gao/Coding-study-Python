"""

假設現在有兩個變數 a = 10 和 b = 20。
請撰寫程式碼交換這兩個變數的值，使得最後 a 變成 20，而 b 變成 10。

"""
a = 10
b = 20
temp = a
a = b
b = temp
print(f"the end: a = {a}, b = {b}")

# It only takes one line to complete the exchange.
'''
a = 10
b = 20
a, b = b, a
print(f"交換後: a = {a}, b = {b}")

'''
