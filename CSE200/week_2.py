# Add Them Up
a, b = map(int, input().split())
print(a + b)


# How Many X's?
print(len(input()))


# Leap Years
year = int(input())
if year % 4 == 0 and year % 400 != 0:
  print("Yes")
else:
  print("No")


# Tricky Ratio
r = int(input())
print(3.14159)



# 2D List
"""
lst = [1, 5, 7, 4, 3, 4.6, True, "hello"]
print(lst[4])
"""

lst = [[1, 2, 4], [5, 3, 0], [3, 8, 6]]
print(lst[2][2]) # -> 6