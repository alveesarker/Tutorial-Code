def prime_fac(n):
    fact_lst = []
    while n % 2 == 0:
        fact_lst.append(2)
        n //= 2
    for i in range(3, int(n ** .5), 2):
        if n % i == 0:
            fact_lst.append(i)
            n //= i
    if n > 1:
        fact_lst.append(n)