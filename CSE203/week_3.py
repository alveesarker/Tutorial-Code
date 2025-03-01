"""
n = int(input())
for i in range(n):
    if i == n - 1:
        print("*" + " *" * (n - 1))
    else:
        print(" " * (n - i -2) + " *" * (i + 1))
"""

n = float(input())
n_int = int(n)
perc = n_int // 10
print("[" + "+" * perc + "." * (10 - perc) + "]" + " " + str(n_int) + "%")

