n = 999999
sieve = set(range(2, n + 1))
counter = 0
while sieve:
    prime = min(sieve)
    sieve -= set(range(prime, n + 1, prime))
    counter += 1
    if counter == 10001:
        print(prime)
        break
