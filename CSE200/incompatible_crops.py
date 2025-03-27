row = int(input())
col = int(input())
corps = [list(input()) for _ in range(row)]
count = 0

for i in range(row):
    for j in range(col):
        if corps[i][j] == ".":
            mine = 0
            if j != 0 and corps[i][j - 1] == "*":
                mine += 1
            if j != (col - 1) and corps[i][j + 1] == "*":
                mine += 1
            if i != 0 and corps[i - 1][j] == "*":
                mine += 1
            if i != (row - 1) and corps[i + 1][j] == "*":
                mine += 1
            if mine == 0:
                count += 1

print(count)