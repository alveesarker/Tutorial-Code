from contextlib import nullcontext


# def function(a):
#     print(a)

# function()


# a = 5
# b = 4
# print(a + b)
# c = 3
# d = 2
# print(c + d)

# def add(a, b):
#     print(a + b)
#
# add(3, 6)
# add(3, 2)
# add(6, 98)




def my_function(a):
    if a == 0:
        return
    print(a)
    my_function(a - 1)
    prin(a)

# 0 -> null
# 1 -> 1 1
# 2 -> 2 1 1 2
# 3 -> 3 2 1 1 2 3


my_function(10)


# i = 1
# while i < 10:
#     print(i)
#     i += 1
