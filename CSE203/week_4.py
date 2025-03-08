# Black or White
"""
a, b = input().split()

last_dig_a = int(a[-1])
last_dig_b = int(b[-1])

if (last_dig_a + last_dig_b) % 2 == 0:
    print("Black")
else:
    print("White")
"""


# Formatted Numbers
num = input().strip()
length = len(num)
result = []

for i in range(length):
    if i > 0 and (length - i) % 3 == 0:
        result.append(',')
    result.append(num[i])

formatted_number = ''.join(result)
print(formatted_number)



# Closest pair
import math

N = int(input().strip())

points = [tuple(map(int, input().split())) for _ in range(N)]

min_distance = float('inf')

for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        min_distance = min(min_distance, distance)

print(min_distance)
