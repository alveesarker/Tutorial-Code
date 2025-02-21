# Missing Number
"""
x = int(input())
a, b, c = map(int, input().split())
done = a + b + c
d = x - done
print(d)
"""
from math import trunc

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
"""
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Yes")
else:print("No")
"""

# Clock Math
H, M = map(int, input().split())
"""
angle = abs((30 * H - (11 / 2) * M))
if angle > 180:
    angle = 360 - angle

print(f"{angle:.7f}")
"""

# Byang's Additions
"""
a = int(input())
b = int(input())
carry = 0
has_carry = False
while a > 0 or b > 0:
    digit_sum = a % 10 + b % 10
    carry = digit_sum // 10
    if carry > 0:
        has_carry = True
        break
    a /= 10
    b /= 10

if has_carry:
    print("Yes")
else:print("No")
"""

