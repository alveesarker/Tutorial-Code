n = int(input())
budgets = list(map(int, input().split()))
t_amount = 0
remaining_budgets = []

for i in budgets:
    ten_per = i * 0.1
    t_amount += ten_per
    remaining_budgets.append(i - ten_per)

print(t_amount)
print(sum(budgets) - t_amount)
print(remaining_budgets)