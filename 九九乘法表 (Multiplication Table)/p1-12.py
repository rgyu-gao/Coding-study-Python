"""

請印出完整的 九九乘法表。格式要整齊，例如：
2 x 1 = 2
2 x 2 = 4
...
9 x 9 = 81

"""

for i in range(1,10):
    for j in range(1,10):
        n = i * j
        print(f"{i} * {j} = {n}", end='\t') 
    print() # When a row is printed, force the program to wave a line, and then start printing the next row.
