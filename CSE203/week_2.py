# Missing Number
x = int(input())
a, b, c = map(int, input().split())
done = a + b + c
d = x - done
print(d)

# Mixed Fractions
a, b = map(int, input().split())
print(a//b, a % b, b)

# Math and Watermelons
m, k = map(int, input().split())
print(m % k)