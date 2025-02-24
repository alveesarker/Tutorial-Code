"""
Recursion is a programming technique where a function
calls itself directly or indirectly to solve a problem.
It breaks down complex problems into smaller,
more manageable sub problems of the same type.
 """

# function
def my_function_1(a, b):
    return a + b


print("Mahi is a gay.")
result = my_function_1(3, 4)
print("Mahire uno .")
print(result)

# recursion
def my_function_two():
    print("Mahire uno .")
    my_function()
    return
my_function_two()


# base case
def my_function(n):
    if n == 0:
        return
    print(n)
    my_function(n - 1)
    print(n)
my_function(3)

"""
def my_function(3):
    if 3 == 0:
        return
    print(3)
    my_function(3 - 1)
    print(3)
    
    
def my_function(2):
    if 2 == 0:
        return
    print(2)
    my_function(2 - 1)
    print(2)
    
def my_function(1):
    if 1 == 0:
        return
    print(1)
    my_function(1 - 1)
    print(1)
    
def my_function(0):
    if 0 == 0:
        return
    print(3)
    my_function(3 - 1)
    print(3)
"""
# print -- 3 2 1 1 2 3