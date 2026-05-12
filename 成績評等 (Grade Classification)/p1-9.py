"""

請撰寫一個程式，讓使用者輸入一個分數 (0-100)，程式會根據以下規則輸出對應的等級：
•	90 分（含）以上：A
•	80 ~ 89 分：B
•	70 ~ 79 分：C
•	60 ~ 69 分：D
•	60 分以下：F

"""

score = int(input("enter one score (0~100):"))

if score >= 90 and score <= 100:
    print(f"your score is A.")
elif score >= 80 and score < 90:
    print(f"your score is B.")
elif score >= 70 and score < 80:
    print(f"your score is C.")
elif score >= 60 and score < 70:
    print(f"your score is D.")
elif score < 60:
    print(f"your score is F.")
else:
    print("error")
