input_str = input("input X, Y: ")


dimensions = [int (x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]

multilist = [[0 for col in range(colNum)] for now in range(rowNum)]
for now in range (rowNum):
    for col in range (colNum):
        multilist[now][col] = now * col
    print(multilist)