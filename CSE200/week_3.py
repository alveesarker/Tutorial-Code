matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[2][1]) -> matrix[row][column]
"""
for i in matrix:
    for j in i:
        print(j, end= ' ')
    print()
"""

# matrix[2][1] = 10
# print(matrix)

col = 3
row = 4

lst = [[0 for _ in range(col)] for _ in range(row)] #List comprehension
print(lst)