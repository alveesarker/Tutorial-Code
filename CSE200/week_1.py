# Pattern Design
def pattern_design(n):
  print(" " * ((n *2) + 1) + "+" + ("-" * (n * 6)) + "+")
  for i in range(n*2):
    print(" " *( (n*2) - i) + "/" + " " * (((n * 2) - i - 1) * 3) + "___/" + "__/"  * i + "/" *i)
  print("+" + ("-" * (n * 6)) + "+" + "/" * (n * 2))
  for i in range(n):
    print("|" + " " * (((n*6) - 21) // 2) + "How to Code in Python" + " " * ((((n * 6)-21) - ((n*6) - 21) // 2)) + "|" + "/" * ((n * 2) - (i * 2)))
  print("+" + ("-" * (n * 6)) + "+")
  print(f"Now only ${n * 10}!")
pattern_design(5)


