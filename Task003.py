from math import sqrt

n = 600851475143
i = 2

while n % i != 0 or any(n // i % j == 0 for j in range(2, int(sqrt(n // i)) + 1)):
    if i == 2:
        i = 3
    elif i == 3:
        i = 5
    else:
        i += (9 - i % 6) // 2
    print(i)
    
print(n // i)
