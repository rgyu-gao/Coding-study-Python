"""
第十八題延伸：雙指針原地交換法
給定一個清單：elements = [10, 20, 30, 40, 50, 60]
請撰寫一個程式，使用雙指針原地交換法
"""

elements = [10, 20, 30, 40, 50, 60]

print(f"交換前: {elements}")

# 1. 初始化雙指針
left = 0                   # 左指針指向清單的最開頭 (索引 0)
right = len(elements) - 1  # 右指針指向清單的最末尾 (索引 5)

# 當左指針還在右指針的左邊時，繼續執行
while left < right:
    # 同時交換左右指針所指向的元素值
    elements[left], elements[right] = elements[right], elements[left]
    
    # 移動指針，向中間靠攏
    left += 1   # 左指針往右移一步
    right -= 1  # 右指針往左移一步

print(f"交換後: {elements}")
