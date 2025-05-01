class Max_min:
    def __init__(self, numbers, max, min):
        self.numbers = numbers
        self.max = max
        self.min = min

    def find_max_min(self):
        for i in self.numbers:
            if i > self.max:
                self.max = i
            if i < self.min:
                self.min = i
        print(f'Max: {self.max}')
        print(f'Min: {self.min}')

f = Max_min([10, 20, 50, 1, 40, 2, 100], 0, 999)
f2 = Max_min([12, 48, 29, 29, 89, 100, 129], 0, 999)
f.find_max_min()
f2.find_max_min()


print(fruits[0])
print(fruits[-1])



"elderberry" "grap" "cherry","apple", ,
fruits[1] = "grap"

if "apple" in fruits:
    print("Found")
else:
    print("not found")