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
"""
H, M = map(int, input().split())
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

# Little Subarray Sum
"""
n, a, b = map(int, input().split())
lst = list(map(int, input().split()))

s = 0
for i in range(a, b+1):
    s += lst[i]
print(s)
"""

# N = int(input())
# b = bin(N)
# b = b.replace("0b", "")
# print(b)

start = 0
end = 10
step = 2
for i in range(start, end, step):
    start = 5
    end = 50
    step = 6
    print(i,end="-")

