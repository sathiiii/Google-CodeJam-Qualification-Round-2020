T = int(input())
for x in range(1, T + 1):
    N = int(input())
    rowsCount, colsCount, trace = 0, 0, 0
    grid = []
    for i in range(N):
        row = list(map(int, input().split()))
        trace += row[i]
        grid.append(row)
        if len(set(row)) < len(row):
            rowsCount += 1
    for col in zip(*grid):
        if len(set(col)) < len(col):
            colsCount += 1
            
    print("Case #{}: {} {} {}".format(x, trace, rowsCount, colsCount))
