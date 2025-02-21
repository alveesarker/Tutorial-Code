# Missing Number
"""
x = int(input())
a, b, c = map(int, input().split())
done = a + b + c
d = x - done
print(d)
"""

# Mixed Fractions
"""
a, b = map(int, input().split())
print(a//b, a % b, b)
"""

# Math and Watermelons
"""
m, k = map(int, input().split())
print(m % k)
"""

# Leap Years
"""
year = int(input())
if year % 4 == 0 and year % 400 != 0:
    print("Yes")
else:
    print("No")
"""

# Proper Leap Years
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Yes")
else:print("No")