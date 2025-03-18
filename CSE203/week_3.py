# First problem
print("Hello World!")

n = int(input())
for i in range(n):
    if i == n - 1:
        print("*" + " *" * (n - 1))
    else:
        print(" " * (n - i -2) + " *" * (i + 1))


n = float(input())
n_int = int(n)
perc = n_int // 10
print("[" + "+" * perc + "." * (10 - perc) + "]" + " " + str(n_int) + "%")


# Fair Distribution
a, b = map(int, input().split())
print(a - (b % a))


# Maximum
number = int(input())
lst = map(int, input().split())
print(max(lst))



# Divisors
n = int(input())
print(1)
for i in range(2, int(n/2) + 1):
    if n % i == 0:
        print(i)
print(n)
