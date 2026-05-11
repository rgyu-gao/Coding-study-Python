"""

請撰寫一個程式，讓使用者輸入攝氏溫度 (°C)，程式會自動將其轉換為華氏溫度 (°F) 並輸出。
轉換公式: F = C * 9/5 + 32

"""

C = float(input("enter °C :"))
F = (C * 9/5) + 32

print(f"°F is {F:.1f} equal to °C is {C}.")
