row = int(input("Input number of rows: "))
col = int(input("Input number of columns: "))
multi_list = [[0 for i in range(col)] for a in range(row)]
for u in range(row):
    for j in range(col):
        multi_list[u][j]=u*j
print(multi_list)