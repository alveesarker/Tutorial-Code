#toph problems---
# Copycat
# a = input()
# print(int(a))

# a = input()
# b = a.split()
# c, d = map(int, b)
# print(c + d)


# Thought Game
def avrg(a, b):
    return (a + b) // 2

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if avrg(a, b) % 2 == 0:
        print("Sadia will be happy.")
    else:
        print("Oops!")