# def fibonacchi(n):
#     lst = []
#     a = 1
#     b = 1
#     for i in range(n):
#         lst.append(a)
#         a, b = b, a + b
#     print(lst)
#
#     a = 3
#     b = 5
#     lst [1, 1, 2, 3, 5, 8]
#
# def fibonacchi(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibonacchi(n -1) + fibonacchi(n-2)
#
# def print_fib(n):
#     for i in range(1, n + 1):
#         print(fibonacchi(i), end=" ")
#
# print_fib(10)
from itertools import product

productList=[['Tshirt',650,'Jack&Jones'],['Jeans',3090, 'Armani'],['Perfume', 6120,'dolce & gabbana']]
# for i in productList:
#     print(f"Name: {i[0]}")
#     print(f"Brand: {i[2]}")

# prod = ["Tshirt"]
# price = int(input())
# brand = input()
# prod.append(price)
# prod.append(brand)
# productList.append(prod)
# for i in productList:
#     if i[1] < 4000:
#         i[1] += (i[1] * 0.2)
# productList.pop()
# print(productList)


student1 = {
    "name" : "student1",
    "age" : 20,
    "grade" : [40, 50, 60]
}

def grade(st):
    gpa = sum(st["grade"]) / len(st["grade"])
    print(gpa)

grade(student1)