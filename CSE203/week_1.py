#toph problems---
# Copycat
a = input()
print(int(a))

# add them up
a = input()
b = a.split()
c, d = map(int, b)
print(c + d)


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


# tricky ratio
r = float(input())
print(3.14159)

# Third number
a = input().split()
print(a[3])


# adding by three numbers
x = int(input())
a = x - 2

print(1, 1, a)

# simple matrix multiplication
A_11, A_12 = map(int, input().split())
A_21, A_22 = map(int, input().split())
B_11, B_12 = map(int, input().split())
B_21, B_22 = map(int, input().split())

C_11 = A_11 * B_11 + A_12 * B_21
C_12 = A_11 * B_12 + A_12 * B_22
C_21 = A_21 * B_11 + A_22 * B_21
C_22 = A_21 * B_12 + A_22 * B_22

print(C_11, C_12)
print(C_21, C_22)