def count_down(n):
    print(n)
    if n == 0:
        return
    else:
        return count_down(n-1)
# count_down(1)
# 2 3 6 2 3 4
#print - 1 0

# 0 -> 0
# 1 -> 1 0
# 2 -> 2 1 0
# 3 -> 3 2 1 0
# 4 -> 4 3 2 1 0


# tup = ("physics", 2001, "Chemistry", 1976, "Rainy Day!", 1997)
# tup2 = (1, 2)
# tup = tup + tup2
# print(tup)
# tup2 = tup2 * 3
# print(tup2)
# tup = ("physics", 2001, "Chemistry", 1976, "Rainy Day!", 1997, 1, 2)
# tup = (1, 2, 1, 2, 1, 2)
# tup3 = (1997, 1, 2, 1, 2, 1)
# tup3 = tup[-3:] + tup2[2:5]
# print(tup3)
# print(tup3[3:5])

def factorial(n):
    if n < 0:
        print("Wrong input")
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)

f = factorial(5)
print(f)