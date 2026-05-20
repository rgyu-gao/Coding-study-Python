"""

給定一個清單：elements = [1, 2, 3, 4, 5]
請撰寫一個程式，不要使用 Python 內建的 .reverse() 或 [::-1] 語法，
單純利用迴圈將這個清單的順序反轉過來，讓它最後變成 [5, 4, 3, 2, 1]。

"""

elements = [1, 2, 3, 4, 5]

reverse_list = []
index = len(elements)-1

for i in range(index,-1,-1):
    reverse_list.append(elements[i])

print(f"原始清單: {elements}")
print(f"反轉清單: {reverse_list}")