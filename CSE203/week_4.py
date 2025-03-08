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
