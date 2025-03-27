row = int(input())
col = int(input())
corps = [input().split() for _ in range(row)]
count = 0

for i in range(row):
    for j in range(col):
        if corps[i][j] == ".":
            mine = 0
            if j != 0 and corps[]