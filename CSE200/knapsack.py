a, b = map(int, input().split())
bag = []

for i in range(a):
    value, weight = list(map(int, input().split()))
    bag.append((value, weight, value/weight))

bag.sort(key=lambda x: x[2], reverse=True)

for i in range(len(bag)):