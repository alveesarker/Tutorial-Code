def nth_prime(n):
    # Estimate an upper bound using the Prime Number Theorem
    # n-th prime is roughly n * log(n) + n * log(log(n)) for n >= 6
    if n < 6:
        upper_bound = 12  # Manually checked to cover primes up to n=5
    else:
        import math
        upper_bound = int(n * (math.log(n) + math.log(math.log(n)))) + 1

    sieve = [True] * (upper_bound + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(upper_bound ** 0.5) + 1):
        if sieve[current]:
            sieve[current * current:: current] = [False] * len(sieve[current * current:: current])

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    if len(primes) >= n:
        return primes[n - 1]
    else:
        # If estimation was too low, increase bound and try again
        return nth_prime(n)  # Alternatively, double the bound and re-run sieve

number = int(input())
print(nth_prime(number))